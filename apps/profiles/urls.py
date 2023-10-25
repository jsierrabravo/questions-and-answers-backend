from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from apps.profiles import views

app_name = 'profiles'

router = DefaultRouter()
router.register(r'', views.UserViewSet, basename="profiles")

urlpatterns = format_suffix_patterns([
    path('', include(router.urls)),
])