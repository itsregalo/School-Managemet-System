from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from  core.models import StudentClass
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


SALUTATIONS = [
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss', 'Miss'),
    ('Madam','Madam')
]

GENDER = [
    ('F','Female'),
    ('M','Male'),
    ('Bi','Bisexual'),
    ('Other', 'Other')
]

User=settings.AUTH_USER_MODEL
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    admission_no = models.CharField(unique=True, max_length=10, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER, max_length=100)
    adm_timestamp = models.DateTimeField(auto_now_add=True)
    has_cleared = models.BooleanField(default=False)
    in_class = models.ForeignKey(StudentClass, on_delete=DO_NOTHING, null=True)

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

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salutation = models.CharField(choices=SALUTATIONS, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    teacher_no = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Staff(models.Model):
    STATUS = [("active", "Active"), ("inactive", "Inactive")]

    GENDER = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(max_length=10, choices=STATUS, default="active")
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name}"

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})
    