from apps.profiles import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# app_name = 'profiles'

router = DefaultRouter()
router.register(r'profiles', views.UserViewSet, basename="profiles")

urlpatterns = [
    path('', include(router.urls)),
]