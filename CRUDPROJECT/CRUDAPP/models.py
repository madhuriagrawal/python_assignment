from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()

    def __str__(self):
        return self.name



