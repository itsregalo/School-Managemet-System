from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')


def ContactUs(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST['first_name']
        email = request.POST['your-email']
        subject = request.POST['subject']
        message = request.POST['your-message']
        
        if name == "":
            messages.error(request, "Name is required")
            if email == "":
                messages.error(request, "email is required")
                if subject == "":
                    messages.error(request, "subject is reuired")
                    if messages == "":
                        messages.error(request, "Message is required")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                        
        send_mail(subject,message, email,["contact@greengarnetsfilms.com"],fail_silently=True)
        messages.success(request, "Thank you for your feedback")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'contact-us.html')

def AboutUs(request, *args, **kwargs):
    return render(request, 'about-us.html')

def ContactPage(request, *args, **kwargs):
    return render(request, 'contact.html')