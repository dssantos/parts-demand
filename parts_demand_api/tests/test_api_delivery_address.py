from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from parts_demand_api.models import UserProfile
from parts_demand_api.models import DeliveryAddress


ROOT_URL = '/api/address/'
ITEM_URL = '/api/address/1/'


class DeliveryAddressApiTests(TestCase):
    """Ensure authenticated users can manipulate their address objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            'local_description':'Escritório',
            'postal_code':'41218770',
            'street':'Albino Fernandes',
            'street_number':'63',
            'complement':'',
            'district':'Novo Horizonte',
            'city':'Salvador',
            'state':'Bahia',
            'country':'Brasil'
        }
        self.request = self.client.post('/api/address/', self.data)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class NotAuthDeliveryAddressApiTests(TestCase):
    """Ensure no authenticated users can not manipulate address objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.data = {
            'local_description':'Escritório',
            'postal_code':'41218770',
            'street':'Albino Fernandes',
            'street_number':'63',
            'complement':'',
            'district':'Novo Horizonte',
            'city':'Salvador',
            'state':'Bahia',
            'country':'Brasil'
        }
        self.request = self.client.post('/api/address/', self.data)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)


class NotOwnerDeliveryAddressApiTests(TestCase):
    """Ensure that users do not manipulate other users' address objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            'local_description':'Escritório da Federação de Comércio',
            'postal_code':'41218770',
            'street':'Albino Fernandes',
            'street_number':'63',
            'complement':'',
            'district':'Novo Horizonte',
            'city':'Salvador',
            'state':'Bahia',
            'country':'Brasil'
        }
        self.request = self.client.post('/api/address/', self.data)
        self.client.logout()

        self.user2 = UserProfile.objects.create(
            name='test2', 
            email='test2@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user2)
        self.data2 = {
            'local_description':'Escritório2',
            'postal_code':'41218770',
            'street':'Albino Fernandes',
            'street_number':'63',
            'complement':'',
            'district':'Novo Horizonte',
            'city':'Salvador',
            'state':'Bahia',
            'country':'Brasil'
        }
        self.request = self.client.post('/api/address/', self.data)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
