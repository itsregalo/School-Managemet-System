from django.db import models
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=254)
    location = models.CharField(max_length=254)


class News(models.Model):
    title = models.CharField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)