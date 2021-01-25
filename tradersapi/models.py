from .services.chemical_service.models import *
from django.urls import reverse
from django.contrib.auth import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfileModel(models.Model):

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, unique=True)

    class Meta:
        verbose_name = _("UserProfileModel")
        verbose_name_plural = _("UserProfiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
