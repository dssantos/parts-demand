from parts_demand_api.models import UserProfile
from parts_demand_api.models import DeliveryAddress
from parts_demand_api.models import PartsDemand


# Create users samples
admin = UserProfile.objects.create_user(email='admin@mail.com', name='admin', password='1')
admin.is_superuser=True
admin.is_staff=True
admin.save()

user1 = UserProfile.objects.create_user(email='user1@mail.com', name='user1', password='1')
user1.save()
user2 = UserProfile.objects.create_user(email='user2@mail.com', name='user2', password='1')
user2.save()

# Create delivery addresses samples
address1 = DeliveryAddress.objects.create(
    local_description='Escritório da Federação de Comércio',
    user_profile=user1,
    postal_code='41218770',
    street='Albino Fernandes',
    street_number='63',
    complement='',
    district='Novo Horizonte',
    city='Salvador',
    state='Bahia',
    country='Brasil'
)
address1.save()

address2 = DeliveryAddress.objects.create(
    local_description='Fábrica da Federação de Comércio',
    user_profile=user2,
    postal_code='41213000',
    street='Ulysses Guimarães',
    street_number='186',
    complement='',
    district='Sussuarana',
    city='Salvador',
    state='Bahia',
    country='Brasil'
)
address2.save()

# Create demands samples
demand1 = PartsDemand.objects.create(
    part_description='Servo motor',
    delivery_address=address1,
    email = user1.email,
    phone = '71999991111',
    user_profile = user1,
    status = False
)
demand1.save()

demand2 = PartsDemand.objects.create(
    part_description='Bateria 9v',
    delivery_address=address2,
    email = user2.email,
    phone = '71999992222',
    user_profile = user2,
    status = False
)
demand2.save()
