from django.urls import path
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('<int:pk>/', views.post_detail, name='detail'),
]