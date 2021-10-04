from django.db import models
from django.utils.text import slugify
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    hod = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

    