from django.contrib import admin

from parts_demand_api import models


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


class DeliveryAddressModelAdmin(admin.ModelAdmin):
    list_display = (
        'local_description', 'user_profile', 'postal_code', 'street', 
        'street_number', 'complement', 'district', 'city', 'state', 'country'
        )


admin.site.register(models.UserProfile, UserProfileModelAdmin)
admin.site.register(models.DeliveryAddress, DeliveryAddressModelAdmin)
