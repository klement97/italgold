from cerberus import Validator
from django.urls import reverse
from model_bakery import baker
from rest_framework import status

from kral_kutu_backend.api_test_case import KKAPITestCase, faker
from order.json_schemas import product_category_schema, product_schema
from order.models import Product, ProductCategory
from order.tests.utils import create_product


class TestProductRetrieve(KKAPITestCase):

    @classmethod
    def setUpTestData(cls):
        # Baker leaves the image field empty
        # so we have to handle it ourselves
        cls.products = [create_product() for _ in range(5)]

    def setUp(self) -> None:
        self.url = self.get_url_with_pk(
                view_name='product',
                pk=self.products[faker.random.randint(0, 4)].pk
                )
        self.v = Validator(product_schema)

    def test_retrieve(self):
        """
        Ensure that the basic retrieve assertions will pass.
        """
        self.retrieve_assertions(self.url)

    def test_retrieve_non_existent_product(self):
        """
        Ensure that we will receive a 404 response when
        trying to retrieve a non existent product.
        """
        last_pk = Product.objects.only('id').order_by('id').last().id
        self.url = self.get_url_with_pk(
                view_name='product',
                pk=last_pk + 1
                )
        response = self.get()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_json_schema(self):
        """
        Ensure that the response schema is valid.
        """
        response = self.get()

        self.assertTrue(self.v.validate(response.data))

    def test_num_of_queries(self):
        """
        Ensure that the required inner and outer joins are
        applied to the query to minimize queries for the retrieve operation.
        """
        self.assertNumQueries(1, func=self.get)


class TestProductList(KKAPITestCase):
    url = reverse('product')

    @classmethod
    def setUpTestData(cls):
        cls.products = baker.make(Product, _quantity=25, image=faker.file_name(), deleted=False)
        baker.make(Product, _quantity=15, image=faker.file_name(), deleted=True)

    def setUp(self) -> None:
        self.v = Validator(product_schema)

    def test_paginated_list(self):
        """
        Ensure that we can get a paginated response.
        """
        self.list_assertions(paginated=True)

    def test_not_paginated_list(self):
        """
        Ensure that we can get a not paginated response when avoiding page query param.
        """
        self.list_assertions(paginated=False,
                             response_data_count=len(self.products))

    def test_json_schema(self):
        """
        Ensure that the response schema is valid.
        """
        response = self.get()
        [self.assertTrue(self.v.validate(product))
         for product in response.data]

    def test_num_of_queries(self):
        """
        Ensure that the required inner and outer joins are
        applied to the query to minimize the number of queries
        for the list operation.
        """
        self.assertNumQueries(1, self.get)


class TestProductCategoryList(KKAPITestCase):
    url = reverse('product-category')

    @classmethod
    def setUpTestData(cls):
        baker.make(ProductCategory, _quantity=10, deleted=True)
        cls.product_categories = baker.make(ProductCategory,
                                            _quantity=25,
                                            deleted=False)

    def setUp(self) -> None:
        self.v = Validator(product_category_schema)

    def test_not_paginated_list(self):
        self.list_assertions(paginated=False,
                             response_data_count=len(self.product_categories))

    def test_json_schema(self):
        response = self.get()

        [self.assertTrue(self.v.validate(category))
         for category in response.data]

    def test_num_of_queries(self):
        self.assertNumQueries(1, self.get)
