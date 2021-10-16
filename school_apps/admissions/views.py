from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from admissions.models import Student
from resources import StudentResource
from tablib import Dataset
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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

@login_required
def add_contact_via_file(request, *args, **kwargs):
        
    students = StudentResource.objects.all()
    
    if request.method == 'POST':        
        student_resourse = StudentResource()
        dataset = Dataset()
        new_student = request.FILES.get('student-file')
        
        if not new_student.name.endswith('xlsx'):
            messages.error(request, 'The file must be in excel format')
            return render(request, 'admin-student-list.html')
        
        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            value = Student(
                data[0], 
                data[1], 
                data[2], 
                data[3],
                data[4]
            )
            value.save()
            messages.success(request, "contacts saved")
    
    context = {
        'students':students
    }
    
    return HttpResponseRedirect(reverse('mainapp:contacts'))