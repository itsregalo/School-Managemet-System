from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from school_apps.admissions.models import Student
from .models import *
# Create your views here.


@login_required
def StudentPortal(request, *args, **kwargs):
    student_profile = get_object_or_404(Student, user=request.user)

    context = {
        'student_profile':student_profile
    }
    return render(request, 'student-portal/index.html', context)