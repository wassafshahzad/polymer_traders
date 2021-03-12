from django.db.models.enums import Choices
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
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class UserPost(models.Model):
    STATUS_CHOICES = [
        ('1', 'Active'),
        ('2', 'Archived'),
        ('0', 'Processing')
    ]
    TYPE_CHOICES = [
        ('0', 'sell'),
        ('1', 'buy')
    ]

    UNIT = [
        ('1', 'KG'),
        ('2', 'POUND'),
        ('3', 'DRUM'),
        ('4', 'BAG')
    ]
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit = models.CharField(max_length=1, choices=UNIT, default='1')
    created_by = models.ForeignKey(
        'UserProfileModel', related_name='created_by', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, null=False, blank=False)
    post_type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, null=False, blank=False)
    text = models.CharField(max_length=255, null=True, blank=True)
