from pyexpat import model
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255),
    author = models.CharField(max_length=255),
    quantity = models.IntegerField

    def __str__(self):
        return self.title
