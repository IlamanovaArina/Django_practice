from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'avatar', 'phone_number', 'country')
    list_filter = ('email',)
    search_fields = ('email',)
