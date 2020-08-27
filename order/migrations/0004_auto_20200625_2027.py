# Generated by Django 3.0.7 on 2020-06-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200625_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Width'),
        ),
    ]