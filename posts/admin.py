from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "created_on",
        "is_promoted",
    )
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 50
    search_fields = (
        "author__username",
        "title",
    )
    list_filter = (
        "created_on",
        "is_promoted",
    )
