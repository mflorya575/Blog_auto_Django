from django.contrib import admin
from .models import Post, Comment, CarDealership


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
    fields = ('title', 'slug', 'author', 'body', 'status', 'map_html')


class CarDealershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'car_count', 'approved']
    list_filter = ['approved']
    actions = ['approve_dealerships']

    def approve_dealerships(self, request, queryset):
        queryset.update(approved=True)
    approve_dealerships.short_description = "Одобрить выбранные автосалоны"


admin.site.register(CarDealership, CarDealershipAdmin)
