from django.contrib import admin

from .models import BlogEntry


@admin.register(BlogEntry)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'content', 'preview', 'created_at', 'quantity_views',)
    list_filter = ('created_at', 'header',)
    search_fields = ('created_at', 'header', 'content',)