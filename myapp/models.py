from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.TextField()