from django.urls import path
from . views import *

app_name='core'

urlpatterns = [
    path('', IndexView, name='index'),
    path('gallery/', GalleryView, name='gallery'),
    path('about-us/', AboutUs, name='about-us'),
    path('contact-us/', ContactUs, name='contact-us'),
    path('contact/', ContactPage, name='contact')
]