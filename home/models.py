from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
