from rest_framework import serializers

from parts_demand_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)


class DeliveryAddressSerialzer(serializers.ModelSerializer):
    """Serializes Delivery Address"""

    class Meta:
        model = models.DeliveryAddress
        fields = (
            'id', 'local_description', 'user_profile', 'postal_code', 
            'street', 'street_number', 'complement', 'district', 'city',
            'state', 'country'
            )
        extra_kwargs = {'user_profile': {'read_only': True}}
