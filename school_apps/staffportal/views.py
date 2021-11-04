from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from school_apps.admissions.models import Teacher
from .models import *
# Create your views here.


def StaffLogin(request, *args, **kwargs):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "":
            messages.error(request, "Username required")
        if password == "":
            messages.error(request, "Password is required")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_teacher == True:
                login(request, user)
                messages.info(request, "You have successfully logged in")
                if next_page is not None:
                    return HttpResponseRedirect(next_page)
                return redirect('core:index')
            messages.error(request,"You are not a Staff")
            logout(request)
            return render(request,'auth/login.html')       
        messages.error(request,"invalid Login! Try again")
        return render(request,'admin-pages/auth/login.html')
    return render(request,'admin-pages/auth/login.html')

def StaffLogOutView(request, *args, **kwargs):
    logout(request)
    messages.success(request,"You successfully logged out")
    return redirect('core:index')

@login_required
def StaffPortal(request, *args, **kwargs):
    teacher_profile = get_object_or_404(Teacher, user=request.user)

    context = {
        'teacher_profile':teacher_profile
    }
    return render(request, 'staffportal/index.html', context)