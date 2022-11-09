from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class AboutCompany(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField( upload_to='about_company/')
    description = models.TextField()
    video = models.FileField(upload_to='videos_uploaded/',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def str(self):
        return self.title
