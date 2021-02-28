from tradersapi.models import UserProfileModel


def has_user_profile(user):
    return UserProfileModel.objects.filter(owner=user).exists()
