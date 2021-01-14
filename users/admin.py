from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "is_active",
    )
    list_filter = ("date_joined",)
    list_per_page = 50
