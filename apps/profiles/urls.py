from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.profiles import views

app_name = 'profiles'

user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', user_list, name='list'),
    path('<int:pk>/', user_detail, name='detail'),
])