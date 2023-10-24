from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.UserList.as_view(), name='list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)