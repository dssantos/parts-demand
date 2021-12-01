from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from parts_demand_api.models import UserProfile


class UserProfileApiTests(APITestCase):

    def setUp(self):
        """Ensure we can create a new account object"""
        url = reverse('userprofile-list')
        data = {'email': 'test@mail.com', 'name': 'Test User', 'password': '1'}
        self.response = self.client.post(url, data, format='json')
    
    def test_create_account(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().name, 'Test User')
    
    def test_retrieve_account(self):
        """Ensure we can create a new account object"""
        response = self.client.get('/api/profile/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'email': 'test@mail.com', 'name': 'Test User'})
