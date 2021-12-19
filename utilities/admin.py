from django.contrib import admin
from .models import (SliderImage, QuicklinkImages, IndexEvent400412,
                        IndexWhyUs700493)
# Register your models here.

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(SliderImage, SliderImageAdmin)

class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(QuicklinkImages, QuickLinkAdmin)

class IndexEventAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(IndexEvent400412, IndexEventAdmin)

class IndexWhyUsAdmin(admin.ModelAdmin):
    list_display = ['name','image','image_thumbnail']

admin.site.register(IndexWhyUs700493, IndexWhyUsAdmin)
