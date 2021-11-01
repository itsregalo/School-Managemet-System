from django.urls import path
from .views import *

app_name = 'staffportal'

urlpatterns = [
    path('login/', StaffLogin, name='staff-login'),
    path('logout/', StaffLogOutView, name='staff-logout'),
    path('me/', StaffPortal, name='my-staff-portal'),
]