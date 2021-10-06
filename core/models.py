from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=254)
    location = models.CharField(max_length=254)


class News(models.Model):
    title = models.CharField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)

class Gallery(models.Model):
    name = models.CharField(max_length=254)
    pic = models.ImageField(upload_to="images/blog")
    pic_thumbnail = ImageSpecField(source='pic',
                                   processors = [ResizeToFill(1920,1080)],
                                   format='JPEG',
                                   options = {'quality':100})