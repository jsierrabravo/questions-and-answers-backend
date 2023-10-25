from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from apps.posts import views


app_name = 'posts'

router = DefaultRouter()
router.register(r'', views.PostViewSet, basename="posts")

urlpatterns = format_suffix_patterns([
    path('', include(router.urls)),
])