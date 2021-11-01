from django.urls import path
from .views import *

app_name = 'studentportal'

urlpatterns = [
    path('me/', StudentPortal, name='my-student-portal'),
]
