from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=12)