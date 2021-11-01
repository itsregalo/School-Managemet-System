from django.urls import path
from .views import *

app_name = 'studentportal'

urlpatterns = [
    path('login/', StudentLogin, name='student-login'),
    path('logout/', StudentLogOutView, name='student-logout'),
    path('me/', StudentPortal, name='my-student-portal'),
]