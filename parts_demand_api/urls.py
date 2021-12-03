from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from parts_demand_api import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('address', views.DeliveryAddressViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
