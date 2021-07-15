from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .task import send_welcome_email_on_signup


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_welcome_email_on_signup.delay(instance.username, instance.email)
