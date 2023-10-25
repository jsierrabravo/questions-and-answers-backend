from apps.profiles.serializers import UserSerializer

from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides a `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer