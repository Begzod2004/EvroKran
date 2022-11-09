from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Contact)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ['title','status','date_create','phone_number']
    list_filter = ['date_create']
    search_fields = ["title"]