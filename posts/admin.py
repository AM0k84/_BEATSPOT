from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", 'author', "title", 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50
    search_fields = ('author__username', 'title',)




