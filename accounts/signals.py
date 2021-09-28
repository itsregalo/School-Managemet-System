from accounts.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance) 

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    if instance.is_superuser==True:
        instance.adminuser.save()
    if instance.is_staff==True:
        instance.staffuser.save()
    if instance.is_merchant==True:
        instance.merchantuser.save()
    if instance.is_customer==True:
        instance.customeruser.save()
    if instance.is_blogger==True:
        instance.bloggeruser.save()