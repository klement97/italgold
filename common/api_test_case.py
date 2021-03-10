import json

from django.conf import settings
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase as RestAPITestCase

faker = Faker()


class APITestCase(RestAPITestCase):
    """
    Custom API Test Case Class to use inside API View Tests.
    Provides methods for all operations that handles common assertions.

    url attr. must be set by the Subclass.
    """

    url = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            getattr(self, 'url')
        except AttributeError:
            raise ValueError("no url set in %s" % (self.__class__,))

    @staticmethod
    def get_with_pk(view_name, pk):
        return reverse(view_name, kwargs={'pk': pk})

    def get(self, data=None, **kwargs):
        return self.client.get(self.url, data, **kwargs)

    def post(self, data=None, **kwargs):
        return self.client.post(self.url, data, **kwargs)

    def put(self, data=None, **kwargs):
        return self.client.put(self.url, data, **kwargs)

    def patch(self, data=None, **kwargs):
        return self.client.patch(self.url, data, **kwargs)

    def delete(self, data=None):
        return self.client.delete(self.url, data)

    def create_asserts(self, posted_data, should_be_in_response=None):
        self.response = self.post(
                data=json.dumps(posted_data),
                content_type='application/json'
                )

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        data = self.response.data

        if should_be_in_response is not None:
            for field in should_be_in_response:
                self.assertIn(field, data)
                if field == 'id':
                    # id field is not posted for create operation.
                    continue
                self.assertEqual(data[field], posted_data[field])

    def list_asserts(self, paginated, response_data_count=None):
        page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
        query_params = {'page': 1} if paginated else None

        self.response = self.get(data=query_params)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

        if paginated:
            self.assertIn('results', self.response.data)
            self.assertIn('count', self.response.data)
            results = self.response.data['results']
            count = self.response.data['count']
            self.assertIsInstance(results, list)
            self.assertLessEqual(len(results), page_size)
            if response_data_count:
                self.assertEqual(count, response_data_count)
        else:
            self.assertIsInstance(self.response.data, list)
            if response_data_count:
                self.assertEqual(len(self.response.data), response_data_count)

    def retrieve_asserts(self, url):
        self.response = self.client.get(url)
        pk = int(url.split('/')[-2])

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        data = self.response.data
        self.assertNotIsInstance(data, list)
        self.assertEqual(data['id'], pk)

    def update_asserts(self, url, update_data, instance,
                       should_be_updated=None):
        update_data['id'] = instance.pk
        response = self.client.put(
                path=url,
                data=json.dumps(update_data),
                content_type='application/json'
                )
        instance.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(instance.id, data['id'])

        if should_be_updated is not None:
            for field in should_be_updated:
                self.assertEqual(getattr(instance, field), data.get(field))

    def delete_asserts(self, url, instance, logic=True):
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        if logic:
            instance.refresh_from_db()
            self.assertTrue(instance.deleted)
