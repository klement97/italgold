import os

from django.conf import settings

from order.models import Product, ProductCategory


def create_tables():
    folder_dir = os.path.join(settings.BASE_DIR, 'KRAL_KUTU/TABLALAR')
    image_paths = os.listdir(folder_dir)
    category = ProductCategory.objects.get(name='Tabaka')

    tables = []
    for image_name in image_paths:
        code = image_name.split('.')[0].replace(' ', '')
        tables.append(Product(**{
            'image': f'products/{image_name}',
            'price': 25,
            'category': category,
            'properties': {
                'code': code,
                'width': 25,
                'height': 3.7,
                'length': 25,
                }
            }))

    Product.objects.bulk_create(tables)


def create_service_tables():
    folder_dir = os.path.join(BASE_DIR, 'KRAL_KUTU/SERVIS_TABLALARI')
    image_paths = os.listdir(folder_dir)
    category = ProductCategory.objects.get(name__icontains='Tabaka Sh')

    tables = []
    for image_name in image_paths:
        code = image_name.split('.')[0].replace(' ', '')
        tables.append(Product(**{
            'image': f'products/{image_name}',
            'price': 25,
            'category': category,
            'properties': {
                'code': code,
                'width': 35,
                'height': 2,
                'length': 20,
                }
            }))

    Product.objects.bulk_create(tables)


def create_premium_tables():
    folder_dir = os.path.join(BASE_DIR, 'KRAL_KUTU/Premium_tablalar')
    image_paths = os.listdir(folder_dir)
    category = ProductCategory.objects.get(name__icontains='Premium')

    tables = []
    for image_name in image_paths:
        code = image_name.split('.')[0].replace(' ', '')
        tables.append(Product(**{
            'image': f'products/{image_name}',
            'price': 25,
            'category': category,
            'properties': {
                'code': code,
                'width': 35,
                'height': 2,
                'length': 20,
                }
            }))

    Product.objects.bulk_create(tables)
