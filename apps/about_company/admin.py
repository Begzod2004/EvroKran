from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AboutCompany)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title','image','description','video',]
    search_fields = ["title"]