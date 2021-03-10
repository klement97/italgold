from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from sendgrid import SendGridAPIClient

from common.api_test_case import APITestCase
from order.models import Order
from order.tests.utils import get_invalid_order_create_dict, \
    get_valid_order_create_dict


class TestOrderCreate(APITestCase):
    url = reverse('order')

    @patch('order.models.send_order_invoice_email', lambda _: None)
    def test_valid_create(self):
        data = get_valid_order_create_dict()
        self.create_asserts(posted_data=data)

    def test_invalid_create_return_bad_request(self):
        invalid_data = get_invalid_order_create_dict()
        response = self.post(data=invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_create_return_bad_field_names(self):
        invalid_data = get_invalid_order_create_dict()
        response = self.post(data=invalid_data, format='json')

        for field in ['first_name', 'last_name', 'phone', 'address']:
            self.assertIn(field, response.data)

    @patch('order.models.send_order_invoice_email', lambda _: None)
    def test_is_order_created_in_db(self):
        request_data = get_valid_order_create_dict()
        response = self.post(data=request_data, format='json')

        order = Order.objects.get(id=response.data['id'])

        for field in ['first_name', 'last_name', 'phone', 'address']:
            self.assertEqual(getattr(order, field), request_data[field])

    @patch('order.models.send_order_invoice_email',
           lambda *args, **kwargs: None)
    def test_num_of_queries(self):
        data = get_valid_order_create_dict()
        query_count = 3

        self.assertNumQueries(
            query_count,
            func=self.post,
            data=data,
            format='json'
            )

    @patch.object(SendGridAPIClient, 'send')
    def test_email_is_sent_to_manager(self, send: MagicMock):
        self.post(data=get_valid_order_create_dict(), format='json')
        send.assert_called_once()
