from django.urls import reverse
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class UserProfileModel(models.Model):

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, blank=False, null=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    profile_picture = models.ImageField(
        upload_to="upload/", blank=True, null=True, default=static('default_profile_pic.png'))

    class Meta:
        verbose_name = "UserProfileModel"
        verbose_name_plural = "UserProfiles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class UserProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    chemical_product = models.ForeignKey(
        'ChemicalProduct', related_name='user_info', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'UserProfileModel', related_name='products', on_delete=models.CASCADE)
