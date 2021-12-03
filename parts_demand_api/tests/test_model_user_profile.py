from django.test import TestCase

from parts_demand_api.models import UserProfile


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.obj = UserProfile.objects.create(
            name='Test User', 
            email='test@mail.com', 
            password='password123'
        )

    def test_create(self):
        self.assertTrue(UserProfile.objects.exists())

    def test_str(self):
        self.assertEqual('Test User', str(self.obj))

    def test_full_name(self):
        self.assertEqual('Test User', self.obj.get_full_name())

    def test_short_name(self):
        self.assertEqual('Test', self.obj.get_short_name())
