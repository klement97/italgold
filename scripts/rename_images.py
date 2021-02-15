import csv
import os

from order.models import Product, ProductCategory


def rename_files():
    path_to_dir = '/home/klementomeri/furnizimi-janar'
    files = os.listdir(path_to_dir)

    for file_name in files:
        if 'jpg' not in file_name:
            continue

        new_file_name = file_name \
            .lower() \
            .strip() \
            .replace(' ', '') \
            .replace('series', '')

        file_path = os.path.join(path_to_dir, file_name)
        new_file_path = os.path.join(path_to_dir, new_file_name)

        os.rename(file_path, new_file_path)


def check_for_image():
    path_to_dir = '/home/klementomeri/furnizimi-janar'
    path_to_file = path_to_dir + '/products.csv'

    missing_images = []
    images = [f for f in os.listdir(path_to_dir) if f.endswith('.jpg')]

    with open(path_to_file, mode='r') as f:
        products = csv.DictReader(f, fieldnames=['code'])
        next(products)

        for product in products:
            code = product['code']
            respective_image = f'{code}.jpg'

            if respective_image not in images:
                missing_images.append({'code': code})

    with open('/home/klementomeri/furnizimi-janar/missing.csv', mode='w') as f:
        csv_file = csv.DictWriter(f, fieldnames=['code'])
        csv_file.writerows(missing_images)


def load_tables():
    path_to_tables = '/home/klementomeri/Pictures/KRAL_KUTU/Catalogue'
    path_to_products_csv = '/home/klementomeri/Pictures/KRAL_KUTU/accessories' \
                           '.csv'
    images = os.listdir(path_to_tables)
    with open(path_to_products_csv, mode='w') as file:
        csv_file = csv.DictWriter(file, fieldnames=['code', 'image', 'price',
                                                    'width', 'length',
                                                    'height'])
        csv_file.writeheader()

        for img in images:
            code = img.replace('.jpg', '')
            code = f'TB{code}' if 'TB' not in code.upper() else code
            price = code.split(' ')[-1] if ' ' in code else None

            csv_file.writerow({
                'code': code,
                'image': img,
                'price': price,
                'width': '23',
                'length': '27',
                'height': '4'
                })


def load_displays():
    path_to_display = '/home/klementomeri/Pictures/KRAL_KUTU/Jewellery Display'
    displays = os.listdir(path_to_display)

    with open(f'/{path_to_display}/displays.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['code', 'image'])
        csv_writer.writeheader()

        for display in displays:
            csv_writer.writerow({
                'code': display.split('.')[0],
                'image': display
                })


def load_boxes():
    path_to_boxes = '/home/klementomeri/Pictures/KRAL_KUTU/KAPAKLI KUTULAR'
    boxes = os.listdir(path_to_boxes)

    with open(f'{path_to_boxes}/boxes.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['code', 'image'])
        csv_writer.writeheader()

        for box in boxes:
            csv_writer.writerow({'code': box.split('.')[0], 'image': box})


def create_tables():
    tables_path = '/home/klementomeri/Pictures/KRAL_KUTU/tables.csv'
    with open(tables_path, 'r') as f:
        tables = csv.DictReader(f, fieldnames=['code', 'image',
                                               'price', 'width',
                                               'length', 'height'])
        next(tables)

        category = ProductCategory.objects.get(name='Table')
        products = []

        for table in tables:
            products.append(Product(**{
                'image': f'products/{table["image"]}',
                'price': float(table['price']) if table['price'] else None,
                'category': category,
                'properties': {
                    'code': table['code'],
                    'width': float(table['width']),
                    'length': float(table['length']),
                    'height': float(table['height'])
                    }
                }))

        Product.objects.bulk_create(products)


def create_displays():
    tables_path = '/home/klementomeri/Pictures/KRAL_KUTU/Jewellery ' \
                  'Display/displays.csv'
    with open(tables_path, 'r') as f:
        tables = csv.DictReader(f, fieldnames=['code', 'image', 'price'])
        next(tables)

        category = ProductCategory.objects.get(name='Display')
        products = []

        for table in tables:
            products.append(Product(**{
                'image': f'products/{table["code"]}.jpg',
                'price': None,
                'category': category,
                'properties': {
                    'code': table['code'],
                    'width': None,
                    'length': None,
                    'height': None
                    }
                }))

        Product.objects.bulk_create(products)


def create_boxes():
    tables_path = '/home/klementomeri/Pictures/KRAL_KUTU/KAPAKLI KUTULAR/boxes.csv'
    with open(tables_path, 'r') as f:
        tables = csv.DictReader(f, fieldnames=['code', 'image'])
        next(tables)

        category = ProductCategory.objects.get(name='Box')
        products = []

        for table in tables:
            products.append(Product(**{
                'image': f'products/{table["image"]}',
                'price': None,
                'category': category,
                'properties': {
                    'code': table['code'],
                    'width': None,
                    'length': None,
                    'height': None
                    }
                }))

        Product.objects.bulk_create(products)


def create_accessories():
    tables_path = '/home/klementomeri/Workspace/ITALGOLD/italgold' \
                  '/csv_files/accessories.csv'
    with open(tables_path, 'r') as f:
        tables = csv.DictReader(f, fieldnames=['codes', 'prices', 'image'])
        next(tables)

        category = ProductCategory.objects.get(name='Accessory')
        products = []

        for table in tables:
            codes = [code.strip() for code in table['codes'].split(',')]
            prices = [float(price.strip())
                      for price in table['prices'].split(',')]

            products.append(Product(**{
                'image': f'products/{table["image"]}',
                'price': None,
                'category': category,
                'properties': {
                    'codes': codes,
                    'prices': prices,
                    'width': None,
                    'length': None,
                    'height': None
                    }
                }))

        Product.objects.bulk_create(products)
