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

    def get_queryset(self):
        if self.request.GET.get('created_by', False):
            created = self.request.GET.get('created_by')
            return UserPost.objects.filter(status='1', created_by=created)
        return UserPost.objects.filter(status='1', **self.request.GET)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
