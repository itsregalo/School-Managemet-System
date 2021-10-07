from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import text
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.name)
        return super(NewsCategory, self).save(*args, **kwargs)

class Event(models.Model):
    title = models.CharField(max_length=254)
    location = models.CharField(max_length=254)


class News(models.Model):
    title = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/news/%Y/%m/%d/')
    news_icon = ImageSpecField(source='image',
                                   processors = [ResizeToFill(150,150)],
                                   format='JPEG',
                                   options = {'quality':100})
    main_icon = ImageSpecField(source='image',
                                   processors = [ResizeToFill(400,245)],
                                   format='JPEG',
                                   options = {'quality':100})
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
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    