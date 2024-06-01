from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Banner


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    autocomplete_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'body']
    fields = ('name', 'body', 'post', 'active')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_active')
    search_fields = ('title',)

    # Настройки для отображения изображений в админке (опционально)

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="150" height="300" />')


# class CarDealershipAdmin(admin.ModelAdmin):
#     list_display = ['name', 'address', 'car_count', 'approved']
#     list_filter = ['approved']
#     actions = ['approve_dealerships']
#
#     def approve_dealerships(self, request, queryset):
#         queryset.update(approved=True)
#     approve_dealerships.short_description = "Одобрить выбранные автосалоны"


# admin.site.register(CarDealershipAdmin)
