from rest_framework import generics, permissions, request
from django.contrib.auth.models import User

from tradersapi.models import UserProfileModel, UserProduct
from tradersapi.util.permissions import IsOwnerOrReadOnly
from .serializers import UserProductSerializer, UserProfileSerializer, AuthUserSerializer


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
    serializer_class = UserProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_queryset(self):
        user = self.request.GET.get('user', None)
        if user:
            return UserProduct.objects.filter(owner=user).order_by('chemical', 'chemical_type', '-created').distinct('chemical', 'chemical_type',)
        else:
            return UserProduct.objects.filter(owner=self.request.user.profile)


class UserProductRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        context['request'] = self.request
        return context
