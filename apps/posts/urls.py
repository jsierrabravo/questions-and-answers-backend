from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.posts import views

app_name = 'posts'

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('root/', views.api_root),
    path('', post_list, name='list'),
    path('<int:pk>/', post_detail, name='detail'),
])