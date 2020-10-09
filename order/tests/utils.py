from model_bakery import baker

from kral_kutu_backend.api_test_case import faker
from order.models import Leather, Product, ProductCategory


def create_product():
    return Product.objects.create(
            image=faker.file_name(),
            price=faker.pydecimal(),
            category=baker.make(ProductCategory),
            properties={"code": "P-001"}
            )


def get_valid_products_dict():
    return [{
        'product': create_product().id,
        'quantity': faker.random.randint(1, 10),
        'notes': faker.text(),
        'width': faker.random.randint(15, 35),
        'height': faker.random.randint(1, 5),
        'length': faker.random.randint(15, 35)
        }
        for _ in range(faker.random.randint(5, 15))]


def get_invalid_order_units_dict():
    return [{
        'product': create_product().id + 1,
        'quantity': faker.random.randint(-100, -1),
        'notes': faker.pybool()
        }
        for _ in range(faker.random.randint(5, 15))]


def get_valid_order_create_dict():
    return {
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'phone': faker.phone_number(),
        'address': faker.address(),
        'inner_leather': baker.make(Leather).id,
        'outer_leather': baker.make(Leather).id,
        'products': get_valid_products_dict()
        }


def get_invalid_order_create_dict():
    leather = baker.make(Leather)
    return {
        'first_name': faker.sentence(nb_words=30),
        'last_name': faker.sentence(nb_words=30),
        'phone': faker.sentence(nb_words=20),
        'address': faker.sentence(nb_words=200),
        'inner_leather': leather.id + 1,
        'outer_leather': leather.id + 2,
        'products': get_invalid_order_units_dict()
        }
