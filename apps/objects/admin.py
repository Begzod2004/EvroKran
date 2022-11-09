from django.contrib import admin
from .models import ObjectImages, Objects, Category

class ObjectImagesInline(admin.TabularInline):
    model = ObjectImages
    extra = 1


class ObjectsAdmin(admin.ModelAdmin):
    inlines = [ObjectImagesInline]
    list_display = ('id', 'title', 'date_created', 'is_active')


admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Category)
