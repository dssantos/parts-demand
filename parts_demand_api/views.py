from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from parts_demand_api import models
from parts_demand_api import serializers
from parts_demand_api import permissions

        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)

    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class DeliveryAddressViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating delivery addresses"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.DeliveryAddressSerialzer
    queryset = models.DeliveryAddress.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDeliveryAddress, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the logged user to the user profile field"""
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):
        """restricts the returned address to a given user"""
        queryset = models.DeliveryAddress.objects.filter(
            user_profile=self.request.user
            )
        return queryset
    