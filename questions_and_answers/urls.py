"""
URL configuration for questions_and_answers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.posts.urls import router as posts_router
from apps.profiles.urls import router as profiles_router

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

main_router = DefaultRouter()
main_router.registry.extend(posts_router.registry)
main_router.registry.extend(profiles_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(main_router.urls)),
]
