from django.contrib import admin
from .models import SliderImage
# Register your models here.

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(SliderImage, SliderImageAdmin)
