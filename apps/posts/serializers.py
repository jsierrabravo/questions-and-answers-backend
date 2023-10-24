from rest_framework import serializers
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'sub_category', 'question', 'description', 'pub_date']