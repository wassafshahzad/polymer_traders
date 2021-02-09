from rest_framework import serializers

from tradersapi.models import UserProfileModel


class UserProfileSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if self._has_user_profile():
            raise serializers.ValidationError(
                "Profile for this user already exist")
        return super().validate(attrs)

    def _has_user_profile(self):
        return UserProfileModel.objects.filter(owner=self.context.get('user'))

    class Meta:
        model = UserProfileModel
        fields = ['name', 'company_name', 'phone_number', 'profile_picture']
