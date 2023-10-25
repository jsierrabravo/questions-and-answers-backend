from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)