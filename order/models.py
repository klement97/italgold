from django.db import models

from django.db.models import DO_NOTHING


# ToDO Check Product, OrderUnit related_name to Leather model

class LeatherSerial(models.Model):
    class Meta:
        ordering = ["name"]
        verbose_name = "Leather serial"
        verbose_name_plural = "Leather serials"

    name = models.CharField(max_length=50, verbose_name='Name')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Leather(models.Model):
    class Meta:
        ordering = ["code"]
        verbose_name = "Leather"
        verbose_name_plural = "Leathers"

    code = models.CharField(max_length=100, verbose_name='Leather')
    serial = models.ForeignKey(LeatherSerial, on_delete=DO_NOTHING, related_name='leathers')
    image = models.CharField(max_length=1000, verbose_name='Image', blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class ProductCategory(models.Model):
    class Meta:
        ordering = ["name"]
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    name = models.CharField(max_length=50, verbose_name='Name')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    email = models.CharField(max_length=50, verbose_name='Email', blank=True)
    address = models.CharField(max_length=50, verbose_name='Address', blank=True)
    is_confirmed = models.BooleanField(default=False, verbose_name='Is confirmed')
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Date last update')

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)


class Product(models.Model):
    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    code = models.CharField(max_length=100, verbose_name='Products')
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    image = models.CharField(max_length=1000, verbose_name='Image')
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=9)
    category = models.ForeignKey(ProductCategory, on_delete=DO_NOTHING)
    inner_color = models.ForeignKey(Leather, on_delete=DO_NOTHING, related_name='inner_products',
                                    verbose_name='Inner color')
    outer_color = models.ForeignKey(Leather, on_delete=DO_NOTHING, related_name='outer_products',
                                    verbose_name='Outer color')
    height = models.FloatField(verbose_name='Height', null=True)
    width = models.FloatField(verbose_name='Width', null=True)
    length = models.FloatField(verbose_name='Length', null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.code, self.title)


class OrderUnit(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = "Order unit"
        verbose_name_plural = "Order units"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_units', verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='order_units', verbose_name='Product')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    inner_leather = models.ForeignKey(Leather, on_delete=DO_NOTHING, related_name='inner_order_units',
                                      verbose_name='Inner leather')
    outer_leather = models.ForeignKey(Leather, on_delete=DO_NOTHING, related_name='outer_order_units',
                                      verbose_name='Outer color')
    height = models.FloatField(verbose_name='Height')
    width = models.FloatField(verbose_name='Width')
    length = models.FloatField(verbose_name='Length', null=True)
    notes = models.CharField(max_length=100, verbose_name='Notes', blank=True)

    def __str__(self):
        return self.id
