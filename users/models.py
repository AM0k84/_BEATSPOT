from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


class UserFollowing(models.Model):
    following_from = models.ForeignKey("Profile", related_name="following_from", on_delete=models.CASCADE)
    follow_to = models.ForeignKey("Profile", related_name="follow_to", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "users_userfollowing"
        constraints = [models.UniqueConstraint(fields=["following_from", "follow_to"], name="unique_followers")]
        ordering = ("-created",)

    def __str__(self):
        return f"FROM:{self.following_from} TO:{self.follow_to}"


class Profile(AbstractUser, HitCountMixin):
    edit_date = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to="profile_photos")
    short_info = models.TextField(max_length=350, blank=True, null=True)
    localization = models.CharField(max_length=40, null=True, blank=True) #todo: change to smth cool!
    slug = models.SlugField(null=False, unique=True)
    following = models.ManyToManyField("self", through=UserFollowing, related_name="followers", symmetrical=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field="object_pk", related_query_name="hit_count_generic_relation"
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        ordering = ("id",)

    def __str__(self):
        return self.username


class ProviderProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True, verbose_name=_("user profile"))
    background_image = models.ImageField(blank=True, null=True, upload_to="background_image")
    facebook_url = models.URLField(max_length=500, blank=True, null=True)
    soundcloud_url = models.URLField(max_length=500, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    website_url = models.URLField(max_length=500, blank=True, null=True)
    # long_description = HTMLField(_("long description"), max_length=3000, blank=True, null=True)
    # kategorie: wykonawca, producent, wytwórnia, muzyk, woalista, itp.

