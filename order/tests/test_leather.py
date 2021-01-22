from cerberus import Validator
from django.urls import reverse
from model_bakery import baker

from kral_kutu_backend.api_test_case import KKAPITestCase, faker
from order.json_schemas import leather_schema, leather_serial_schema


class TestLeatherList(KKAPITestCase):
    url = reverse('leather')

    @classmethod
    def setUpTestData(cls):
        baker.make('Leather', _quantity=10, deleted=True)
        cls.leathers = baker.make('Leather',
                                  _quantity=25,
                                  image=faker.file_name(),
                                  deleted=False)

    def setUp(self) -> None:
        self.v = Validator(leather_schema)

    def test_paginated_list(self):
        self.list_assertions(paginated=True)

    def test_not_paginated_list(self):
        self.list_assertions(paginated=False,
                             response_data_count=len(self.leathers))

    def test_json_schema(self):
        response = self.get()

        for leather in response.data:
            self.assertTrue(self.v.validate(leather))

    def test_num_of_queries(self):
        self.assertNumQueries(1, self.get)


class TestLeatherSerialList(KKAPITestCase):
    url = reverse('leather-serial')

    @classmethod
    def setUpTestData(cls):
        baker.make('LeatherSerial', _quantity=10, deleted=True)
        cls.serials = baker.make('LeatherSerial',
                                 _quantity=25,
                                 deleted=False
                                 )

    def setUp(self) -> None:
        self.v = Validator(leather_serial_schema)

    def test_paginated_list(self):
        self.list_assertions(paginated=True)

    def test_not_paginated_list(self):
        self.list_assertions(paginated=False,
                             response_data_count=len(self.serials))

    def test_json_schema(self):
        response = self.get()

        for serial in response.data:
            self.assertTrue(self.v.validate(serial))
