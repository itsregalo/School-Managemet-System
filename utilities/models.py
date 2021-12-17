from django.db import models
from imagekit.models.fields import ImageSpecField
from pilkit.processors.resize import ResizeToFill

# Create your models here.

class SliderImage(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/utils/%Y/%m')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(1800,1119)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class QuicklinkImages(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/utils/%Y/%m')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(800,869)],
                                    format='jpeg',
                                    options={'quality':100})

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

class IndexEvent400412(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/utils/%Y/%m')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(800,869)],
                                    format='jpeg',
                                    options={'quality':100})

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

class IndexWhyUs700493(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/utils/%Y/%m')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(800,869)],
                                    format='jpeg',
                                    options={'quality':100})

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
