from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import text
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class AcademicSession(models.Model):
    name = models.CharField(max_length=250, unique=True)
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Academic Session"
        verbose_name_plural = "Academic Sessions"
        ordering = ['-name']

    def __str__(self):
        return self.name

class AcademicTerm(models.Model):
    name = models.CharField(max_length=254)
    current = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.name)
        return super(AcademicTerm, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Academic Term"
        verbose_name_plural = "Academic Terms"
        ordering=['-name']

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Student Class"
        verbose_name_plural = "Student Classes"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.name)
        return super(StudentClass, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    event_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_file = models.FileField(upload_to='files/event/%Y/%m/%d',
                                    blank=True, null=True)
    slug = models.SlugField(blank=True)
    event_pic = models.ImageField(upload_to='images/events/%Y/%m/%d/', 
                                default='images/event.jpg')
    pic_thumbnail = ImageSpecField(source='event_pic',
                                   processors = [ResizeToFill(400,257)],
                                   format='JPEG',
                                   options = {'quality':100})
    is_approved = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-event_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.title)
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class NoticeCategory(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Notice Category'
        verbose_name_plural = 'Notice Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.name)
        return super(NoticeCategory, self).save(*args, **kwargs)

class Notice(models.Model):
    title = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/notice/%Y/%m/%d/')
    notice_icon = ImageSpecField(source='image',
                                   processors = [ResizeToFill(150,150)],
                                   format='JPEG',
                                   options = {'quality':100})
    main_icon = ImageSpecField(source='image',
                                   processors = [ResizeToFill(400,245)],
                                   format='JPEG',
                                   options = {'quality':100})
    description = RichTextField()
    date_of_event = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    is_approved = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = "Notices"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Notice, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class NoticeFile(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    file = models.FileField(upload_to='docs/notices/%Y/%m/%d')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

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

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return f"{self.name}"


class SchoolTourRequest(models.Model):
    full_name = models.CharField(max_length=254)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
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
    
    