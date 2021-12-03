from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is tring to edit their own rofile"""
        if self.request.user.is_staff:
            return True

        return obj.id == request.user.id
        

class UpdateOwnDeliveryAddress(permissions.BasePermission):
    """Allow user to update their own address"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own address"""

        return obj.user_profile.id == request.user.id


class UpdateOwnPartsDemand(permissions.BasePermission):
    """Allow user to update their own demands"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own demands"""
        if (request.method in permissions.SAFE_METHODS):
            return True

        return obj.user_profile.id == request.user.id
