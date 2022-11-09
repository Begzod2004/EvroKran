from django.db import models

# Create your models here.


class Order(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField(upload_to='objects/')
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.CharField(max_length=20 , default=0)
    description = models.TextField()
    is_active = models.BooleanField(default=True)    
    
    def __str__(self):
        return self.title

