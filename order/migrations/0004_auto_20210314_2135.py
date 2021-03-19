# Generated by Django 3.1.5 on 2021-03-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210313_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(related_name='products', to='order.ProductSubCategory', verbose_name='Sub category'),
        ),
        migrations.AlterUniqueTogether(
            name='productsubcategory',
            unique_together={('name', 'id')},
        ),
    ]