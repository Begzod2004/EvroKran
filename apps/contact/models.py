from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


CONTACT_STATUS = (
    (0,"New"),
    (1,"Prosess"),
    (2,"Canceled"),
    (3,"Finished")
)


class Contact(models.Model):
    title = models.CharField(max_length=65)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def str(self):
        return self.title
