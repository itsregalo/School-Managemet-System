from django.db import models


class Student(models.Model):
    admission_no = models.CharField(unique=True, max_length=10, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    adm_timestamp = models.DateTimeField(auto_now_add=True)
    has_cleared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.admission_no:
            self.admission_no = f"{Student.objects.all.count()+1}"
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=254)
    email = models.EmailField(blank=True, null=True)
    adress = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student.first_name} {self.student.last_name}"
    