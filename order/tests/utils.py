from model_bakery import baker

from kral_kutu_backend.api_test_case import faker
from order.models import Leather, Product


def get_valid_order_units_dict():
    return [{
        'product': baker.make(Product).id,
        'quantity': faker.random.randint(1, 10),
        'notes': faker.text()
        }
        for _ in range(faker.random.randint(5, 15))]


def get_invalid_order_units_dict():
    product = baker.make(Product)
    return [{
        'product': product.id + 1,
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
        'order_units': get_valid_order_units_dict()
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
        'order_units': get_invalid_order_units_dict()
        }
