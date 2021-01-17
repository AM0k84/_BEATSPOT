from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Created(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        abstract = True


class Post(Created):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("-id",)

    def __str__(self):
        return f"{self.title}"
