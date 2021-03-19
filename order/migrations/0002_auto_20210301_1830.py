# Generated by Django 3.1.5 on 2021-03-01 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='order.productcategory')),
            ],
            options={
                'verbose_name': 'Product Sub category',
                'verbose_name_plural': 'Product Sub categories',
                'ordering': ['name'],
                'unique_together': {('name', 'category')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='order.productsubcategory', verbose_name='Sub category'),
        ),
    ]