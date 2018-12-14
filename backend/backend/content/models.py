from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField()