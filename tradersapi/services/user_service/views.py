from rest_framework import generics, permissions
from django.contrib.auth.models import User

from tradersapi.models import UserProfileModel, UserPost
from .serializers import UserProfileSerializer, AuthUserSerializer, UserPostSerializer


class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context


class AuthUserCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()


class UserPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
