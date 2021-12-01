from django.test import TestCase
from parts_demand_api.models import DeliveryAddress
from parts_demand_api.models import UserProfile

class DeliveryAddressModelTest(TestCase):
    
    def setUp(self):
        self.user = UserProfile.objects.create(
            name='Test User', 
            email='test@mail.com', 
            password='1'
        )
        self.address = DeliveryAddress(
            local_description='Escritório da Federação de Comércio',
            user_profile=self.user,
            postal_code='41218770',
            street='Albino Fernandes',
            street_number='63',
            complement='',
            district='Novo Horizonte',
            city='Salvador',
            state='Bahia',
            country='Brasil'
        )
        self.address.save()

    def test_create(self):
        """Must create a delivery address with all attributes"""
        self.assertTrue(DeliveryAddress.objects.exists())
        self.assertEqual(
            self.address.local_description, 
            'Escritório da Federação de Comércio'
        )
        self.assertEqual(self.address.user_profile, self.user)
        self.assertEqual(self.address.postal_code, '41218770')
        self.assertEqual(self.address.street, 'Albino Fernandes')
        self.assertEqual(self.address.street_number, '63')
        self.assertEqual(self.address.complement, '')
        self.assertEqual(self.address.district, 'Novo Horizonte')
        self.assertEqual(self.address.city, 'Salvador')
        self.assertEqual(self.address.state, 'Bahia')
        self.assertEqual(self.address.country, 'Brasil')
