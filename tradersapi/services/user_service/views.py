from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.response import Response

from tradersapi.models import UserProfileModel, UserPost
from tradersapi.util.permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer, AuthUserSerializer, UserPostSerializer


class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def list(self, request, *args, **kwargs):
        if kwargs.get("current", False):
            return Response(
                self.get_serializer(
                    UserProfileModel.objects.get(owner=request.user)
                ).data
            )
        return super().list(request, *args, **kwargs)


class AuthUserCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()


class UserPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.filter(status="1").order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["created_by", "post_type", "chemical", "chemical_type"]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["request"] = self.request
        return context


class UserPostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.filter(status="1")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
