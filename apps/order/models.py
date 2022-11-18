from django.db import models


class Order(models.Model):
    car = models.ForeignKey('objects.Objects', on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)    
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.title