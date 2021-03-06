from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import connection, models

from common.models import LogicalDelete, Track
from common.utils import dictfetchall, send_order_invoice_email


class LeatherSerial(LogicalDelete):
    name = models.CharField(max_length=50, verbose_name='Name')

    class Meta:
        ordering = ["name"]
        verbose_name = "Leather serial"
        verbose_name_plural = "Leather serials"

    def __str__(self):
        return self.name


class Leather(LogicalDelete):
    code = models.CharField(verbose_name='Code', max_length=30)
    image = models.FileField(
            verbose_name='Image',
            blank=True,
            upload_to='leathers'
            )
    serial = models.ForeignKey(
            to=LeatherSerial,
            on_delete=models.DO_NOTHING,
            related_name='leathers'
            )

    class Meta:
        ordering = ["code"]
        verbose_name = "Leather"
        verbose_name_plural = "Leathers"
        unique_together = ['code', 'serial']

    def __str__(self):
        return self.code


class ProductCategoryQuerySet(models.QuerySet):

    @staticmethod
    def get_with_sub_categories():
        with connection.cursor() as cursor:
            cursor.execute(
                    """
                    select o.name, array_agg(distinct op.name) as sub_categories
                    from order_product p
                             inner join order_product_sub_category opsc on p.id = opsc.product_id
                             inner join order_productsubcategory op on op.id = opsc.productsubcategory_id
                             inner join order_productcategory o on o.id = p.category_id
                    group by p.category_id, o.name;
                    """
                    )
            return dictfetchall(cursor)


class ProductCategory(LogicalDelete):
    name = models.CharField(max_length=50, verbose_name='Name')

    objects = ProductCategoryQuerySet.as_manager()

    class Meta:
        ordering = ["name"]
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name


class ProductSubCategory(LogicalDelete):
    name = models.CharField(max_length=50, verbose_name='Name')
    category = models.ManyToManyField(
            to=ProductCategory,
            related_name='sub_categories'
            )

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'id']
        verbose_name = 'Product Sub category'
        verbose_name_plural = 'Product Sub categories'

    def __str__(self):
        return self.name


class ProductQuerySet(models.QuerySet):

    def get_id_price_mapping(self) -> dict[int, float]:
        return {p.id: p.price for p in self}

    def get_products_by_code(self) -> dict[str, 'Product']:
        return {p.properties['code']: p for p in self}


class Product(LogicalDelete):
    image = models.FileField(verbose_name='Image', upload_to='products')
    price = models.DecimalField(
            verbose_name='Price',
            decimal_places=3,
            max_digits=10,
            null=True,
            blank=True,
            validators=[MinValueValidator(0)]
            )
    properties = models.JSONField(
            'Properties',
            help_text='Stores all of the product specific properties.'
            )
    category = models.ForeignKey(
            to=ProductCategory,
            on_delete=models.DO_NOTHING,
            related_name='products',
            verbose_name='Category'
            )
    sub_category = models.ManyToManyField(
            to=ProductSubCategory,
            related_name='products',
            verbose_name='Sub category',
            )

    objects = ProductQuerySet.as_manager()

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @staticmethod
    def get_id_price_mapping(ids) -> dict[int: float]:
        return Product.objects \
            .only('id', 'price') \
            .filter(id__in=set(ids)) \
            .get_id_price_mapping()


class Order(LogicalDelete, Track):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    phone = models.CharField(verbose_name='Phone', max_length=20)
    address = models.CharField(verbose_name='Address', max_length=254)
    email = models.EmailField(verbose_name='Email', max_length=254, blank=True)

    products = ArrayField(models.JSONField(verbose_name='Product details'))

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_order_invoice_email(self)

    @classmethod
    def sanitize_products_field(cls, products: list[dict]):
        required_fields = [
            'product', 'quantity', 'price', 'code', 'width', 'height', 'length',
            'inner_leather', 'outer_leather', 'notes'
            ]
        for i, unit in enumerate(products):
            sanitized_unit = {}
            for field in required_fields:
                sanitized_unit[field] = unit.get(field)

            products[i] = sanitized_unit

        return products
