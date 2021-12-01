from django.test import TestCase
from parts_demand_api.models import DeliveryAddress
from parts_demand_api.models import UserProfile
from parts_demand_api.models import PartsDemand

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

        self.demand = PartsDemand.objects.create(
            part_description='Bateria 9v', 
            delivery_address=self.address,
            email='test@mail.com', 
            phone='71999999999',
            user_profile=self.user,
            status=True
        )

    def test_create(self):
        """Must create a part demand with all attributes"""
        self.assertTrue(PartsDemand.objects.exists())
        self.assertEqual(self.demand.part_description, 'Bateria 9v')
        self.assertEqual(self.demand.delivery_address, self.address)
        self.assertEqual(self.demand.email, 'test@mail.com')
        self.assertEqual(self.demand.phone, '71999999999')
        self.assertEqual(self.demand.user_profile, self.user)
        self.assertEqual(self.demand.status, True)
