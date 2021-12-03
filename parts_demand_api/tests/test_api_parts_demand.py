from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from parts_demand_api.models import UserProfile
from parts_demand_api.models import PartsDemand


ADDRESS_URL = '/api/address/'
ADDRESS_ITEM_URL = ADDRESS_URL+'1/'
DEMAND_URL = '/api/demand/'
DEMAND_ITEM_URL = DEMAND_URL+'1/'


class PartsDemandApiTests(TestCase):
    """Ensure authenticated users can manipulate their demands objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.address = {
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
        self.request = self.client.post(ADDRESS_URL, self.address)
        self.demand = {
            'part_description':'Servo motor',
            'delivery_address':'1',
            'email':'test@mail.com',
            'phone':'71999999999',
            'status': False
        }
        self.request = self.client.post(DEMAND_URL, self.demand)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        request = self.client.get(DEMAND_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        request = self.client.patch(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = self.client.delete(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class NotAuthPartsDemandApiTests(TestCase):
    """Ensure no authenticated users can not manipulate demands objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.address = {
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
        self.request = self.client.post(ADDRESS_URL, self.address)
        self.demand = {
            'part_description':'Servo motor',
            'delivery_address':'1',
            'email':'test@mail.com',
            'phone':'71999999999',
            'status': False
        }
        self.request = self.client.post(DEMAND_URL, self.demand)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list(self):
        request = self.client.get(DEMAND_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        request = self.client.get(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update(self):
        request = self.client.put(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
        request = self.client.patch(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete(self):
        request = self.client.delete(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)


class NotOwnerPartsDemandApiTests(TestCase):
    """Ensure that users do not manipulate other users' demands objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.address = {
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
        self.request = self.client.post(ADDRESS_URL, self.address)
        self.demand = {
            'part_description':'Servo motor',
            'delivery_address':'1',
            'email':'test@mail.com',
            'phone':'71999999999',
            'status': False
        }
        self.request = self.client.post(DEMAND_URL, self.demand)

        self.client.logout()

        self.user2 = UserProfile.objects.create(
            name='test2', 
            email='test2@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user2)
        self.address2 = {
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
        self.request = self.client.post(ADDRESS_URL, self.address2)
        self.demand2 = {
            'part_description':'Servo motor2',
            'delivery_address':'2',
            'email':'test@mail.com',
            'phone':'71999999999',
            'status': False
        }
        self.request = self.client.post(DEMAND_URL, self.demand2)
        #self.assertEqual(self.request.status_code, PartsDemand.objects.all()[1].user_profile.id)

    def test_list(self):
        request = self.client.get(DEMAND_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
        request = self.client.patch(DEMAND_ITEM_URL, self.demand)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        request = self.client.delete(DEMAND_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
