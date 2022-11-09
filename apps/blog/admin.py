from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)

class BlogueAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','image','category','description','date_create','is_active']
    list_filter = ['date_create']
    search_fields = ["title"]