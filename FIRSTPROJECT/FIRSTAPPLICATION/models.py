from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language= models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=254)
    contact = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Create your models here.
