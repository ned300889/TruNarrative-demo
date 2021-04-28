from rest_framework.test import APIClient
from django.test import TestCase


class GetTestCase(TestCase):
    def testGet(self):
        client = APIClient()
        client.get('/people', format='json')




