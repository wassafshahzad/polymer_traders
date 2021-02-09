from rest_framework import serializers

from tradersapi.models import UserProfileModel


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ['name', 'company_name', 'phone_number', 'profile_picture']
