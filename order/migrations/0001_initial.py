# Generated by Django 3.1.5 on 2021-02-15 23:16

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=30, verbose_name='Code')),
                ('image', models.ImageField(blank=True, upload_to='leathers', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Leather',
                'verbose_name_plural': 'Leathers',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='LeatherSerial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Leather serial',
                'verbose_name_plural': 'Leather serials',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('properties', models.JSONField(help_text='Stores all of the product specific properties.', verbose_name='Properties')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='order.productcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_last_updated', models.DateTimeField(auto_now=True, verbose_name='Date last updated')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('address', models.CharField(max_length=254, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('products', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(verbose_name='Product details'), size=None)),
                ('inner_leather', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inner_orders', to='order.leather', verbose_name='Inner leather')),
                ('outer_leather', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outer_orders', to='order.leather', verbose_name='Outer leather')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='leather',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='leathers', to='order.leatherserial'),
        ),
        migrations.AlterUniqueTogether(
            name='leather',
            unique_together={('code', 'serial')},
        ),
    ]
