from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
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

@login_required
def add_contact_via_file(request, *args, **kwargs):
        
    contacts = Contact.objects.all()
    
    if request.method == 'POST':        
        contact_resourse = ContactResource()
        dataset = Dataset()
        new_contact = request.FILES.get('contact-file')
        
        if not new_contact.name.endswith('xlsx'):
            messages.error(request, 'The file must be in excel format')
            return render(request, 'app-contact.html')
        
        imported_data = dataset.load(new_contact.read(), format='xlsx')
        for data in imported_data:
            value = Contact(
                data[0], 
                data[1], 
                data[2], 
                data[3],
                data[4]
            )
            value.save()
            messages.success(request, "contacts saved")
    
    context = {
        'contacts':contacts
    }
    
    return HttpResponseRedirect(reverse('mainapp:contacts'))