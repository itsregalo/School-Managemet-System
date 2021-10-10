from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import text
# Create your models here.

class AcademicSession(models.Model):
    name = models.CharField(max_length=250, unique=True)
    current = models.BooleanField(default=False)
    class Meta:
         ordering = ['-name']

    def __str__(self):
        return self.name

class AcademicTerm(models.Model):
    name = models.CharField(max_length=254)
    current = models.BooleanField(default=False)

    class Meta:
        ordering=['-name']

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name

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
    event_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.title)
        return super(Event, self).save(*args, **kwargs)

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


class SchoolTourRequest(models.Model):
    full_name = models.CharField(max_length=254)
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=13, help_text="e.g 254712860997")
    email = models.EmailField(blank=True, null=True)
    special_request = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'School Tour Request'
        verbose_name_plural = 'School Tour Requests'
        ordering = ['timestamp']

    def __str__(self):
        return self.full_name
    
    