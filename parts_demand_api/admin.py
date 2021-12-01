from django.contrib import admin

from parts_demand_api import models


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


admin.site.register(models.UserProfile, UserProfileModelAdmin)
