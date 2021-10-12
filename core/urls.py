from django.urls import path
from . views import *

app_name='core'

urlpatterns = [
    path('', IndexView, name='index'),
    path('apply/', ApplicationView, name='apply'),
    path('academy-life/', AcademyLife, name='academy-life'),
    path('gallery/', GalleryView, name='gallery'),
    path('about-us/', AboutUs, name='about-us'),
    path('contact-us/', ContactUs, name='contact-us'),
    path('contact/', ContactPage, name='contact'),
    path('school-tour/', SchoolTourRequestView, name='school-tour'),
    path('donations/', DonationPageView, name='donation'),
    path('scholarships/', ScholarshipView, name='scholarships'),
    path('alumni/', AlumniView, name='alumni'),
    path('events/', EventListView, name='events')
]