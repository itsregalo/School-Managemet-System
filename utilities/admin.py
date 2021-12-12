from django.contrib import admin
from .models import SliderImagem, QuicklinkImages
# Register your models here.

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(SliderImage, SliderImageAdmin)

class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(QuicklinkImages, QuickLinkAdmin)
