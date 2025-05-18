from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Create new User."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Adding logic to get user active and hash password upon creating"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """List of Users."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Get one User."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Update one User."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Delete one User."""

    queryset = User.objects.all()
    permission_classes = [IsUser]
