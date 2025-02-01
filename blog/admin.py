from django.contrib import admin

from .models import BlogEntry


@admin.register(BlogEntry)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'content', 'preview', 'created_at', 'quantity_views', 'publication_attribute',)
    list_filter = ('created_at', 'header',)
    search_fields = ('created_at', 'header', 'content',)