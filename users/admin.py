from django.contrib import admin

from .models import Profile, UserFollowing
from django_admin_inline_paginator.admin import TabularInlinePaginated


class FollowsToInLine(TabularInlinePaginated):
    model = UserFollowing
    extra = 2
    fk_name = "follow_to"
    can_delete = False
    per_page = 10


class FollowingFromInLine(TabularInlinePaginated):
    model = UserFollowing
    extra = 2
    fk_name = "following_from"
    can_delete = False
    per_page = 2


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("id", "following_from", "follow_to", "created")
    search_fields = ("following_from__username", "follow_to__username")
    list_filter = ("created",)
    list_per_page = 2


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [FollowsToInLine, FollowingFromInLine]
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
