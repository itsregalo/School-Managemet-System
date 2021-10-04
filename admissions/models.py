from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

User=settings.AUTH_USER_MODEL
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=DO_NOTHING)
    admission_no = models.CharField(unique=True, max_length=10, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    adm_timestamp = models.DateTimeField(auto_now_add=True)
    has_cleared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.admission_no:
            self.admission_no = f"{Student.objects.all().count()+1}"
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}. {self.first_name} {self.last_name}"

    def parent(self):
        return Parent.objects.filter(student__icontains=self)
    
class Parent(models.Model):
    students = models.ManyToManyField(Student)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=254)
    email = models.EmailField(blank=True, null=True)
    adress = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    