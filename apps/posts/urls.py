from apps.posts import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# app_name = 'posts'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="posts")

urlpatterns = [
    path('', include(router.urls)),
]