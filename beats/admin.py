from django.contrib import admin

from beats.models import Beat


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    list_display = ('video_link', )
