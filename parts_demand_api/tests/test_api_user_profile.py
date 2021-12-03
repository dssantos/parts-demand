from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from parts_demand_api.models import UserProfile


PROFILE_URL = '/api/profile/'
PROFILE_ITEM_URL = PROFILE_URL+'1/'


class UserProfileApiTests(TestCase):
    """Ensure authenticated users can manipulate their own profile"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.new_user = {
            'name':'testx', 
            'email':'testx@mail.com', 
            'password':'1'
        }

    def test_list(self):
        request = self.client.get(PROFILE_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        request = self.client.patch(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = self.client.delete(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class NotAuthUserProfileApiTests(TestCase):
    """Ensure no authenticated users can not manipulate profiles objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.new_user = {
            'name':'testx', 
            'email':'testx@mail.com', 
            'password':'1'
        }

    def test_create(self):
        request = self.client.post(PROFILE_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        request = self.client.get(PROFILE_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        request = self.client.put(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
        request = self.client.patch(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        request = self.client.delete(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)


class NotOwnerUserProfileApiTests(TestCase):
    """Ensure that users do not manipulate other profile users"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )

        self.user2 = UserProfile.objects.create(
            name='test2', 
            email='test2@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user2)
        self.new_user = {
            'name':'testx', 
            'email':'testx@mail.com', 
            'password':'1'
        }

    def test_list(self):
        request = self.client.get(PROFILE_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        request = self.client.put(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
        request = self.client.patch(PROFILE_ITEM_URL, self.new_user)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        request = self.client.delete(PROFILE_ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
