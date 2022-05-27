from operator import mod
from django.db import models

# Create your hero models here.
class Hero(models.Model):
    name = models.CharField(max_length=300)
    alias = models.CharField(max_length=300)