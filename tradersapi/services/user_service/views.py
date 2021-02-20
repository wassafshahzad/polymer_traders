from rest_framework import generics, permissions
from django.contrib.auth.models import User

from tradersapi.models import UserProfileModel, UserProduct
from .serializers import UserProfileSerializer, AuthUserSerializer, UserProductSerilizer


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


class CreateListUserProduct(generics.ListCreateAPIView):
    serializer_class = UserProductSerilizer
    queryset = UserProduct.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
