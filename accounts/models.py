from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.conf import settings




User = settings.AUTH_USER_MODEL
# Create your models here.

STAFF_CHOICES = [
    ("CEO", "CEO"),
    ("Marketing Officer", "Marketing Officer"),
    ("Customer Care","Customer Care"),
    ("Quality Officer", "Quality Officer")
]

class CustomUser(AbstractUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="images/profile/customer")
    profile_pic_thumbnail = ImageSpecField(source='profile_pic',
                                           processors=[ResizeToFill(100,100)],
                                           format='JPEG',
                                           options={'quality':100}
                                           )
    phone = models.CharField(max_length=13, null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username

class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.phone} - {self.user.username}"
    
    
class EmailSubscibers(models.Model):
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
    def no_of_subscribers(self):
        return self.objects.all().count()
    
    
class BestCustomerReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    class Meta:
        verbose_name = "Best Customer Review"
        verbose_name_plural = "Best Customer Reviews"
        
    def __str__(self):
        return user.username