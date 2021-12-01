from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from parts_demand_api import models
from parts_demand_api import serializers
from parts_demand_api import permissions

        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
