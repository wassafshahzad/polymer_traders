from rest_framework import generics, permissions
from tradersapi.models import UserProfileModel
from .serializers import UserProfileSerializer


class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
