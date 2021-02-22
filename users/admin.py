from django.contrib import admin
from django_admin_inline_paginator.admin import TabularInlinePaginated

from .models import Profile, ProviderCategory, ProviderProfile, UserFollowing


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
    per_page = 10


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("id", "following_from", "follow_to", "created")
    search_fields = ("following_from__username", "follow_to__username")
    list_filter = ("created",)
    list_per_page = 10


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [FollowsToInLine, FollowingFromInLine]
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "edit_date",
        "is_active",
        "num_followers",
        "num_followed",
    )
    prepopulated_fields = {"slug": ("username",)}
    search_fields = ("username", "email")
    list_filter = (
        "date_joined",
        "is_active",
    )
    list_per_page = 10


@admin.register(ProviderCategory)
class ProviderCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "created_on", "slug")
    prepopulated_fields = {"slug": ("category_name",)}
    search_fields = ("category_name",)
    list_filter = ("created_on",)


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_profile",
        "created_at",
        "edit_date",
        "provider_category",
        "is_promoted",
    )
    search_fields = (
        "user_profile__username",
        "user_profile__email",
    )
    list_filter = (
        "user_profile__date_joined",
        "user_profile__is_active",
    )
    list_per_page = 10
