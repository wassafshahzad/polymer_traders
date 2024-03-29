from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.response import Response

from tradersapi.models import UserProfileModel, UserPost
from tradersapi.util.permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer, AuthUserSerializer, UserPostSerializer
from .filters import UserPostFilter

class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def list(self, request, *args, **kwargs):
        if kwargs.get("current", False) and not request.user.is_anonymous:
            user_profile = get_object_or_404(UserProfileModel, owner= request.user)
            return Response(self.get_serializer(user_profile).data)
        return super().list(request, *args, **kwargs)


class AuthUserCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()


class UserPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.filter(status="1").order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserPostFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["request"] = self.request
        return context


class UserPostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.filter(status="1")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["request"] = self.request
        return context


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
