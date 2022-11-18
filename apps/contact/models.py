from django.db import models



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
    from_i = models.CharField(max_length=50) 
    to_i = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

    def str(self):
        return self.title
