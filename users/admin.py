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
    prepopulated_fields = {"slug": ("username",)}
    search_fields = ("username", "email")
    list_filter = ("date_joined",)
    list_per_page = 50
