from django.http import HttpResponse
from django.shortcuts import render
from .models import Result
from .resources import ResultResource
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required
def add_student_via_file(request, *args, **kwargs):
    results = Result.objects.all()
    
    if request.method == 'POST':        
        result_resourse = ResultResource()
        dataset = Dataset()
        new_student = request.FILES.get('student-file')
        
        if not new_student.name.endswith('xlsx'):
            messages.error(request, 'The file must be in excel format')
            return render(request, 'admin-student-list.html')
        
        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            value = Result(
                data[0], 
                data[1], 
                data[2], 
                data[3],
                data[4]
            )
            value.save()
            messages.success(request, "contacts saved")
    
    context = {
        'results':results
    }
    
    return HttpResponseRedirect(reverse('mainapp:contacts'))