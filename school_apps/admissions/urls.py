from django.urls import path
from .views import StudentList
app_name = 'admissions'

urlpatterns = [
    path('students/', StudentList, name='student-list')
]
