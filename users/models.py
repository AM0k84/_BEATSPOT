from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


class UserFollowing(models.Model):
    following_from = models.ForeignKey(
        "Profile", related_name="following_from", on_delete=models.CASCADE, verbose_name=_("Following from")
    )
    follow_to = models.ForeignKey(
        "Profile", related_name="follow_to", on_delete=models.CASCADE, verbose_name=_("Following to")
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "users_userfollowing"
        constraints = [models.UniqueConstraint(fields=["following_from", "follow_to"], name="unique_followers")]
        ordering = ("-created",)

    def __str__(self):
        return f"FROM:{self.following_from} TO:{self.follow_to}"


class Profile(AbstractUser, HitCountMixin):
    edit_date = models.DateTimeField(_("edited"), auto_now=True)
    profile_photo = models.ImageField(_("avatar"), blank=True, null=True, upload_to="profile_photos")
    short_info = models.TextField(_("short info"), max_length=350, blank=True, null=True)
    localization = models.CharField(
        _("localization"), max_length=40, null=True, blank=True
    )  # todo: change to smth cool!
    slug = models.SlugField(null=False, unique=True)
    following = models.ManyToManyField(
        "self", through=UserFollowing, related_name="followers", verbose_name=_("following"), symmetrical=False
    )
    is_regular_profile = models.BooleanField(_("Is regular users"), default=False)
    is_provider_profile = models.BooleanField(_("Is provider users"), default=False)

    @property
    def num_followers(self):
        return self.followers.all().count()

    @property
    def num_followed(self):
        return self.following.all().count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field="object_pk", related_query_name="hit_count_generic_relation"
    )

    class Meta:
        verbose_name = _("users")
        verbose_name_plural = _("profiles")
        ordering = ("id",)

    def __str__(self):
        return self.username


class ProviderCategory(models.Model):
    category_name = models.CharField(_("category name"), max_length=128)
    created_on = models.DateTimeField(_("created"), auto_now_add=True, null=True)
    edit_date = models.DateTimeField(_("edited"), auto_now=True)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Provider category")
        verbose_name_plural = _("Provider categories")
        ordering = ("id",)

    def __str__(self):
        return self.category_name


class ProviderProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True, verbose_name=_("user users"))
    provider_category = models.ForeignKey(
        ProviderCategory, on_delete=models.CASCADE, related_name="categories", verbose_name=_("provider category")
    )
    created_at = models.DateTimeField(_("created"), auto_now_add=True)
    edit_date = models.DateTimeField(_("editeded"), auto_now=True)
    is_promoted = models.BooleanField(_("is promoted"), default=False)
    background_image = models.ImageField(_("background image"), blank=True, null=True, upload_to="background_image")
    facebook_url = models.URLField(max_length=500, blank=True, null=True)
    soundcloud_url = models.URLField(max_length=500, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    website_url = models.URLField(max_length=500, blank=True, null=True)
    is_verify = models.BooleanField(_("Is verify"), default=False)

    # long_description = HTMLField(_("long description"), max_length=3000, blank=True, null=True)
    # kategorie: wykonawca, producent, wytwórnia, muzyk, woalista, itp.

    class Meta:
        verbose_name = _("Provider users")
        verbose_name_plural = _("Provider profiles")
        ordering = ("id",)

    def __str__(self):
        return self.user_profile.username
