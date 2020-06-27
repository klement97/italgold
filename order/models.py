from django.core.validators import MinValueValidator
from django.db import models


class LeatherSerial(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Leather serial"
        verbose_name_plural = "Leather serials"
        db_table = 'leather_serial'

    def __str__(self):
        return self.name


class Leather(models.Model):
    code = models.CharField(verbose_name='Code', max_length=30)
    serial = models.ForeignKey(LeatherSerial,
                               on_delete=models.DO_NOTHING,
                               related_name='leathers'
                               )
    image = models.ImageField(verbose_name='Image', blank=True, upload_to='leathers')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["code"]
        verbose_name = "Leather"
        verbose_name_plural = "Leathers"
        db_table = 'leather'
        unique_together = ['code', 'serial']

    def __str__(self):
        return self.code


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"
        db_table = 'product_category'

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    email = models.EmailField(max_length=254, verbose_name='Email', blank=True)
    address = models.CharField(max_length=254, verbose_name='Address', blank=True)

    is_confirmed = models.BooleanField(default=False, verbose_name='Is confirmed')
    deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    date_last_updated = models.DateTimeField(auto_now=True, verbose_name='Date last updated')

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = 'order'

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)


class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='Code', unique=True)
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    image = models.ImageField(verbose_name='Image', upload_to='products')

    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.DO_NOTHING,
                                 related_name='products',
                                 verbose_name='Category'
                                 )
    inner_leather = models.ForeignKey(Leather,
                                      on_delete=models.DO_NOTHING,
                                      related_name='inner_products',
                                      verbose_name='Inner leather'
                                      )
    outer_leather = models.ForeignKey(Leather,
                                      on_delete=models.DO_NOTHING,
                                      related_name='outer_products',
                                      verbose_name='Outer leather'
                                      )

    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=9,
                                validators=[MinValueValidator(0)])
    height = models.DecimalField(verbose_name='Height', null=True,
                                 max_digits=5, decimal_places=2, blank=True,
                                 validators=[MinValueValidator(0)]
                                 )
    width = models.DecimalField(verbose_name='Width', null=True, max_digits=5,
                                decimal_places=2, blank=True,
                                validators=[MinValueValidator(0)]
                                )
    length = models.DecimalField(verbose_name='Length', null=True, max_digits=5,
                                 decimal_places=2, blank=True,
                                 validators=[MinValueValidator(0)]
                                 )

    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = 'product'

    def __str__(self):
        return '%s - %s' % (self.code, self.title)


class OrderUnit(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='order_units',
                              verbose_name='Order'
                              )
    product = models.ForeignKey(Product,
                                on_delete=models.DO_NOTHING,
                                related_name='order_units',
                                verbose_name='Product'
                                )
    inner_leather = models.ForeignKey(Leather,
                                      on_delete=models.DO_NOTHING,
                                      related_name='inner_order_units',
                                      verbose_name='Inner leather'
                                      )
    outer_leather = models.ForeignKey(Leather,
                                      on_delete=models.DO_NOTHING,
                                      related_name='outer_order_units',
                                      verbose_name='Outer leather'
                                      )

    quantity = models.PositiveIntegerField(verbose_name='Quantity',
                                           validators=[MinValueValidator(1)]
                                           )
    price = models.DecimalField(verbose_name='Price', max_digits=9, decimal_places=2,
                                validators=[MinValueValidator(0)]
                                )
    height = models.DecimalField(verbose_name='Height', null=True,
                                 max_digits=5, decimal_places=2,
                                 validators=[MinValueValidator(0)]
                                 )
    width = models.DecimalField(verbose_name='Width', null=True,
                                max_digits=5, decimal_places=2,
                                validators=[MinValueValidator(0)]
                                )
    length = models.DecimalField(verbose_name='Length', null=True,
                                 max_digits=5, decimal_places=2,
                                 validators=[MinValueValidator(0)]
                                 )

    notes = models.CharField(max_length=254, verbose_name='Notes', blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Order unit"
        verbose_name_plural = "Order units"
        db_table = 'order_unit'

    def __str__(self):
        return f'{self.order.id}-{self.product}'
