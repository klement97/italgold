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

    def test_invalid_create_return_bad_request(self):
        invalid_data = get_invalid_order_create_dict()
        response = self.post(data=invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_create_return_bad_field_names(self):
        invalid_data = get_invalid_order_create_dict()
        response = self.post(data=invalid_data, format='json')

        for field in ['first_name', 'last_name', 'phone', 'address']:
            self.assertIn(field, response.data)

    def test_is_order_created_in_db(self):
        request_data = get_valid_order_create_dict()
        response = self.post(data=request_data, format='json')

        order = Order.objects.get(id=response.data['id'])

        for field in ['first_name', 'last_name', 'phone', 'address']:
            self.assertEqual(getattr(order, field), request_data[field])

    def test_num_of_queries(self):
        data = get_valid_order_create_dict()
        query_count = 4  # 3 select (1 inner leather, 1 outer leather, 1 product) and 1 insert
        self.assertNumQueries(query_count, func=self.post, data=data, format='json')
