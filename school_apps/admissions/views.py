from django.shortcuts import get_object_or_404, render

from admissions.models import Student

# Create your views here.

def StudentList(request, *args, **kwargs):
    students = Student.objects.filter(has_cleared=False)
    context = {
        'students':students
    }
    return render(request, 'athletics.html', context)


def StudentDetail(request, pk, *args, **kwargs):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student':student
    }
    return render(request, 'admission/sigle-student.html')