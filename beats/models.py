from django.db import models
from embed_video.fields import EmbedVideoField


class Beat(models.Model):
    video_link = EmbedVideoField(blank=False, null=False)
