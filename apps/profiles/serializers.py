
from apps.posts.models import Post
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='posts:detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='posts:detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']