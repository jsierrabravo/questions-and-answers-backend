from rest_framework import serializers
from apps.posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail')
    
    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'sub_category', 
                  'question', 'description', 'pub_date']