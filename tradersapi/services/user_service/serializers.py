from tradersapi.task import send_welcome_email_on_signup
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


from tradersapi.models import (
    UserProfileModel,
    UserPost,
    ChemicalModel,
    ChemicalTypeModel,
)
from tradersapi.util.util_methods import has_user_profile


class UserProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if has_user_profile(self.context.get("user")):
            raise serializers.ValidationError("Profile for this user already exist")
        return UserProfileModel.objects.create(
            owner=self.context["user"], **validated_data
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = UserProfileModel
        fields = ["id", "name", "company_name", "phone_number", "profile_picture"]


class AuthUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)

        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        self.context["token"] = token.key
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["key"] = self.context["token"]
        return data

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class UserPostSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    chemical = serializers.SlugRelatedField(
        slug_field="chemical_name", queryset=ChemicalModel.objects.all()
    )
    chemical_type = serializers.SlugRelatedField(
        slug_field="chem_type", queryset=ChemicalTypeModel.objects.all()
    )
    status = serializers.CharField(required=False)

    def is_valid(self, raise_exception):
        if not has_user_profile(self.context.get("user")):
            raise serializers.ValidationError("Profile Does not Exist")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        profile = self.context.get("user").profile
        status = "1"
        return UserPost.objects.create(
            status=status,
            created_by=profile,
            **validated_data,
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["status"] = instance.get_status_display()
        data["post_type"] = instance.get_post_type_display()
        data["unit"] = instance.get_unit_display()
        return data

    class Meta:
        model = UserPost
        fields = "__all__"
        read_only_fields = ("status",)
