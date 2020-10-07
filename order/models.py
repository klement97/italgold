from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import JSONField

from common.models import LogicalDeleteModel, TrackedModel


class LeatherSerial(LogicalDeleteModel):
    name = models.CharField(max_length=50, verbose_name='Name')

    class Meta:
        ordering = ["name"]
        verbose_name = "Leather serial"
        verbose_name_plural = "Leather serials"

    def __str__(self):
        return self.name


class Leather(LogicalDeleteModel):
    code = models.CharField(verbose_name='Code', max_length=30)
    image = models.ImageField(verbose_name='Image', blank=True, upload_to='leathers')
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


class ProductCategory(LogicalDeleteModel):
    name = models.CharField(max_length=50, verbose_name='Name')

    class Meta:
        ordering = ["name"]
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name


class Product(LogicalDeleteModel):
    image = models.ImageField(verbose_name='Image', upload_to='products')
    price = models.DecimalField(verbose_name='Price', decimal_places=3, max_digits=10,
                                validators=[MinValueValidator(0)])
    properties = JSONField('Properties', help_text='Stores all of the product specific properties.')
    category = models.ForeignKey(to=ProductCategory,
                                 on_delete=models.DO_NOTHING,
                                 related_name='products',
                                 verbose_name='Category')

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Order(LogicalDeleteModel, TrackedModel):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    phone = models.CharField(verbose_name='Phone', max_length=20)
    address = models.CharField(verbose_name='Address', max_length=254)
    email = models.EmailField(verbose_name='Email', max_length=254, blank=True)

    products = ArrayField(JSONField(verbose_name='Product details'))
    inner_leather = models.ForeignKey(to=Leather,
                                      on_delete=models.CASCADE,
                                      related_name='inner_orders',
                                      verbose_name='Inner leather',
                                      null=True)
    outer_leather = models.ForeignKey(to=Leather,
                                      on_delete=models.CASCADE,
                                      related_name='outer_orders',
                                      verbose_name='Outer leather',
                                      null=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)
