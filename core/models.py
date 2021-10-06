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
    image = models.ImageField(upload_to="images/gallery/%Y/%m/%d")
    image_grid = ImageSpecField(source='image',
                                   processors = [ResizeToFill(400,377)],
                                   format='JPEG',
                                   options = {'quality':100})
    image_thumbnail = ImageSpecField(source='image',
                                   processors = [ResizeToFill(1280,853)],
                                   format='JPEG',
                                   options = {'quality':100})

    def __str__(self):
        return self.name
    