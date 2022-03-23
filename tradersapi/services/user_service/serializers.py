from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


from tradersapi.models import (
    UserProfileModel,
    UserPost,
    ChemicalModel,
    ChemicalTypeModel,
)
from tradersapi.services.user_service.models import ImageModel
from tradersapi.util.util_methods import has_user_profile



class ImageModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ("image",)

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
    images = ImageModelSerialzier(many=False)
    chemical = serializers.SlugRelatedField(
        slug_field="chemical_name", queryset=ChemicalModel.objects.all()
    )
    chemical_type = serializers.SlugRelatedField(
        slug_field="chem_type", queryset=ChemicalTypeModel.objects.all()
    )
    status = serializers.CharField(required=False)

    # remove this fucntion to allow multiple uploads
    def to_internal_value(self, data):
        image = data.pop("images")
        data["images.image"]  = image[0] or None
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def is_valid(self, raise_exception):
        if not has_user_profile(self.context.get("user")):
            raise serializers.ValidationError("Profile Does not Exist")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        profile = self.context.get("user").profile
        status = "1"
        images = validated_data.pop("images")
        post = UserPost.objects.create(
            status=status,
            created_by=profile,
            **validated_data,
        )
        ImageModel.objects.create(**images, content_obj=post)
        return post

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["status"] = instance.get_status_display()
        data["post_type"] = instance.get_post_type_display()
        data["unit"] = instance.get_unit_display()
        data["images"] = ImageModelSerialzier(
            instance.images.all().first(), context = {"request": self.context.get("request")}).data
        return data

    class Meta:
        model = UserPost
        fields = "__all__"
        read_only_fields = ("status",)
        depth=1
