from django.contrib import admin
from beats.models import Beat, BeatCategory, BeatLike


class BeatLikesInLine(admin.TabularInline):
    model = BeatLike
    extra = 1
    # fk_name = "like_to"


@admin.register(BeatLike)
class BeatLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'like_from', 'like_to', 'created',)
    search_fields = ('like_from', 'like_to',)
    readonly_fields = ("created",)


@admin.register(BeatCategory)
class BeatCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_on', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name',)
    list_filter = ('created_on',)
    readonly_fields = ("created_on", 'edit_date',)
    list_per_page = 10


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    inlines = [BeatLikesInLine, ]
    list_display = ('id', 'beat_title', 'beat_link', 'is_promoted', 'num_likes',)
    prepopulated_fields = {"slug": ("beat_title",)}
    search_fields = ("beat_title",)
    list_filter = ('created_on',)
    readonly_fields = ("created_on", 'edit_date',)
    list_per_page = 10
