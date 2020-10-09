from django.urls import reverse
from rest_framework import status

from kral_kutu_backend.api_test_case import KKAPITestCase
from order.models import Order
from order.tests.utils import get_invalid_order_create_dict, get_valid_order_create_dict


class TestOrderCreate(KKAPITestCase):
    url = reverse('order')

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def test_valid_create(self):
        data = get_valid_order_create_dict()
        self.creation_assertions(posted_data=data)

    def test_invalid_create(self):
        invalid_data = get_invalid_order_create_dict()
        response = self.post(data=invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        [self.assertIn(field, response.data)
         for field in ['first_name', 'last_name', 'phone', 'address', 'order_units']]

        order_units = response.data['order_units']
        [self.assertIn(field, unit)
         for field in ['product', 'quantity', 'notes']
         for unit in order_units]

    def test_is_order_created_in_db(self):
        request_data = get_valid_order_create_dict()
        response = self.post(data=request_data, format='json')

        order = Order.objects.get(id=response.data['id'])

        [self.assertEqual(getattr(order, field), request_data[field])
         for field in ['first_name', 'last_name', 'phone', 'address']]

    def test_num_of_queries(self):
        # TODO: Find a way to reduce the number of queries
        data = get_valid_order_create_dict()
        # 1 query per order unit +
        # 4 queries for insert +
        # 1 query for final select +
        query_count = 5 + len(data['order_units'])
        self.assertNumQueries(query_count, func=self.post, data=data, format='json')
