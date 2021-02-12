

from django.contrib.auth.models import User
from rest_framework import serializers
from tradersapi.models import UserProfileModel


class UserProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if self._has_user_profile():
            raise serializers.ValidationError(
                "Profile for this user already exist")
        return UserProfileModel.objects.create(owner=self.context['user'], **validated_data)

    def _has_user_profile(self):
        return UserProfileModel.objects.filter(owner=self.context.get('user')).exists()

    class Meta:
        model = UserProfileModel
        fields = ['name', 'company_name', 'phone_number', 'profile_picture']


class AuthUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email',)
