import csv

from order.models import Product


def get_product_from_dict(product_dict: dict) -> Product:
    return Product(
        properties={
            'code': product_dict['code'].upper(),
            'width': product_dict['width'],
            'length': product_dict['length'],
            'height': product_dict['height'],
            },
        price=product_dict['price'],
        category_id=product_dict['category'],
        image=f'products/{product_dict["image"]}.jpg'
        )


def load_products_csv():
    with open('./csv_files/products.csv') as f:
        field_names = ['code', 'codes', 'width', 'length', 'height', 'price',
                       'prices', 'category',
                       'image']
        file = csv.DictReader(f, fieldnames=field_names)

        new_products = []
        existing_products = Product.objects.get_products_by_code()

        next(file)  # skip header row
        for product in file:
            if existing_products.get(product['code'].upper()) is None:
                print(f'New product: {product}')
                new_products.append(get_product_from_dict(product))

        Product.objects.bulk_create(new_products)
