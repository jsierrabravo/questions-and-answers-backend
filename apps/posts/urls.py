from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)