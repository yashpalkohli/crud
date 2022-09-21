from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    deppt = models.CharField(max_length=70)
