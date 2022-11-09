from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Objects(models.Model):
    title = models.CharField(max_length=65)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tonna = models.CharField(max_length=50 , default=0)
    siz = models.CharField(max_length=50, default=0)
    max_tonna = models.CharField(max_length=50) # Qancha kotara olishi
    lenght_strell = models.CharField(max_length=50) # o'q uzunligi
    speed_car = models.CharField(max_length=50) # mashina tezligi
    description = RichTextField()
    is_active = models.BooleanField(default=True)    
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class ObjectImages(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.SET_NULL, null=True, related_name="object_images")
    image = models.ImageField(upload_to="CarsImages", null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'image of {self.object.id}'
