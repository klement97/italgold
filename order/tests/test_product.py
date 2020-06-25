from cerberus import Validator
from model_bakery import baker
from rest_framework import status

from kral_kutu_backend.api_test_case import KKAPITestCase, faker
from order.models import Leather, Product
from order.schemas.product import product_schema


class TestProductRetrieve(KKAPITestCase):

    @classmethod
    def setUpTestData(cls):
        # Baker leaves the image field empty
        # so we have to handle it ourselves
        leather = baker.make(Leather, image=faker.file_name())
        cls.products = baker.make(
            Product, _quantity=5, image=faker.file_name(),
            inner_leather=leather, outer_leather=leather
            )

    def setUp(self) -> None:
        self.url = self.get_url_with_pk(view_name='product', pk=self.products[faker.random.randint(0, 4)].pk)

    def test_retrieve(self):
        self.retrieve_assertions(self.url)

    def test_retrieve_non_existent_product(self):
        last_pk = Product.objects.only('id').order_by('id').last().id
        self.url = self.get_url_with_pk(view_name='product', pk=last_pk + 1)

        response = self.get()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_json_schema(self):
        v = Validator(product_schema)
        response = self.get()

        self.assertTrue(v.validate(response.data))
