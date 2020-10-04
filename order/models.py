from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import JSONField

from common.models import CodedModel, LogicalDeleteModel, ProductClassModel, TrackedModel


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


class Order(LogicalDeleteModel, TrackedModel):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    address = models.CharField(max_length=254, verbose_name='Address')
    email = models.EmailField(max_length=254, verbose_name='Email', blank=True)

    order_units = ArrayField(JSONField())

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)


class Product(LogicalDeleteModel):
    image = models.ImageField(verbose_name='Image', upload_to='products')
    category = models.ForeignKey(
            to=ProductCategory,
            on_delete=models.DO_NOTHING,
            related_name='products',
            verbose_name='Category'
            )
    price = models.DecimalField(verbose_name='Price', decimal_places=3, max_digits=10,
                                validators=[MinValueValidator(0)])

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Table(ProductClassModel, CodedModel):
    height = models.DecimalField(verbose_name='Height', max_digits=4, decimal_places=1,
                                 validators=[MinValueValidator(0)])
    width = models.DecimalField(verbose_name='Width', max_digits=4, decimal_places=1,
                                validators=[MinValueValidator(0)])
    length = models.DecimalField(verbose_name='Length', max_digits=4, decimal_places=1,
                                 validators=[MinValueValidator(0)])


class Accessory(ProductClassModel, CodedModel):
    pass


class Golden(ProductClassModel):
    weight = models.DecimalField(verbose_name='Weight', max_digits=6, decimal_places=2)
    carat = models.CharField(max_length=10)


class Silver(ProductClassModel):
    weight = models.DecimalField(verbose_name='Weight', max_digits=6, decimal_places=2)
