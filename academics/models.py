from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
# Create your models here.


class AcademicSession(models.Model):
    name = models.CharField(max_length=250, unique=True)
    current = models.BooleanField(default=False)
    class Meta:
         ordering = '-name'

    def __str__(self):
        return self.name

class AcademicTerm(models.Model):
    name = models.CharField(max_length=254)
    current = models.BooleanField(default=False)

    class Meta:
        ordering='-name'

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

    
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')
    tsc_no = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    hod = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Class(models.Model):
    name = models.CharField(max_length=254)

class ExamBank(models.Model):
    name = models.CharField(max_length=254)
    examination_date = models.DateTimeField()
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Results(models.Model):
    pass
    

    