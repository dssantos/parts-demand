from django.contrib import admin

from parts_demand_api import models


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


class DeliveryAddressModelAdmin(admin.ModelAdmin):
    list_display = (
        'local_description', 'user_profile', 'postal_code', 'street', 
        'street_number', 'complement', 'district', 'city', 'state', 'country'
        )

class PartsDemandModelAdmin(admin.ModelAdmin):
    list_display = (
        'part_description', 'delivery_address', 'email', 
        'phone', 'user_profile', 'status'
        )


admin.site.register(models.UserProfile, UserProfileModelAdmin)
admin.site.register(models.DeliveryAddress, DeliveryAddressModelAdmin)
admin.site.register(models.PartsDemand, PartsDemandModelAdmin)
