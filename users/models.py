from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    profile_photo = models.ImageField(blank=True, null=True, upload_to="profile_photos")

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
