

from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from tradersapi.models import UserProfileModel, UserProduct
from ..chemical_service.serializers import ChemicalProductSerializer
from tradersapi.util.util_methods import has_user_profile


class UserProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if self.has_user_profile(self.context.get('user')):
            raise serializers.ValidationError(
                "Profile for this user already exist")
        return UserProfileModel.objects.create(owner=self.context['user'], **validated_data)

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


class UserProductSerilizer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    chemical_product = ChemicalProductSerializer()

    def create(self, validated_data):
        if not has_user_profile(self.context.get('user')):
            raise serializers.ValidationError(
                "Complete User Profile Before adding products")
        return super().create(**validated_data)

    class Meta:
        model = UserProduct
        fields = ['owner', 'chemical_product']
