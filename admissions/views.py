from django.shortcuts import render

from admissions.models import Student

# Create your views here.

def StudentList(request, *args, **kwargs):
    students = Student.objects.filter(has_cleared=False)
    context = {
        'students':students
    }
    return render(request, 'athletics.html', context)