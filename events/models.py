from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    available_seats = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
