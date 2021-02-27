

from django.contrib.auth.models import User
from rest_framework import serializers
from tradersapi.models import UserProfileModel, UserProduct
from tradersapi.serializers import ChemicalSerializer, ChemicalTypeSerializer
from tradersapi.util.util_methods import has_user_profile


class UserProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if has_user_profile(self.context.get('user')):
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


class UserProductSerializer(serializers.ModelSerializer):

    chemical_detail = ChemicalSerializer(source='chemical', read_only=True)
    chemical_type_detail = ChemicalTypeSerializer(
        source='chemical_type', read_only=True)
    owner = UserProfileSerializer(read_only=True)

    class Meta:
        model = UserProduct
        fields = ['chemical', 'chemical_type',
                  'quantity', 'price_per_bad', 'owner', 'chemical_detail', 'chemical_type_detail']

        extra_kwargs = {
            'chemical': {'write_only': True},
            'chemical_type':  {'write_only': True}
        }

    def validate(self, attrs):
        if not has_user_profile(self.context.get('user')):
            raise serializers.ValidationError(
                detail='User Profile does not exist')
        return super().validate(attrs)

    def create(self, validated_data):
        owner = UserProfileModel.objects.get(owner=self.context.get('user'))
        return UserProduct.objects.create(owner=owner, **validated_data)
