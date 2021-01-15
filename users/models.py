from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


class Profile(AbstractUser, HitCountMixin):
    edit_date = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to="profile_photos")
    info = models.TextField(max_length=350, blank=True, null=True)
    localization = models.CharField(max_length=40, null=True, blank=True)
    facebook_url = models.URLField(max_length=500, blank=True, null=True)
    soundcloud_url = models.URLField(max_length=500, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    website_url = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field="object_pk", related_query_name="hit_count_generic_relation"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
