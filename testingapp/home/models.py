# Create your models here.
from django.db import models


class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class data(models.Model):
    aname = models.CharField(max_length=250)
    aimage = models.ImageField(upload_to='pics')
    adesc = models.TextField()

    def __str__(self):
        return self.aname
