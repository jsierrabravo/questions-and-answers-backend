from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]