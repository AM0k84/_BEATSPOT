from django.contrib import admin

from .models import Profile, UserFollowing


class FollowsToInLine(admin.TabularInline):
    model = UserFollowing
    extra = 2
    fk_name = 'follows_to'
    can_delete = False


class FollowingFromLine(admin.TabularInline):
    model = UserFollowing
    extra = 2
    fk_name = 'following_from'
    can_delete = False


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("id", 'following_from', 'follows_to', 'created')
    search_fields = ("following_from__username", 'follows_to__username')
    list_filter = ('created',)
    list_per_page = 50


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        FollowsToInLine, FollowingFromLine
    ]
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
