from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from accounts.models import EmailSubscibers
# Create your views here.


def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')

def ApplicationView(request, *args, **kwargs):
    return render(request, 'apply-procedure.html')

def AcademyLife(request, *args, **kwargs):
    return render(request, 'academy-life.html')

def GalleryView(request, *args, **kwargs):
    images = Gallery.objects.filter(is_approved=False)

    context = {
        'images':images
    }
    return render(request, 'core/gallery.html', context)

def SchoolTour(request, *args, **kwargs):
    if request.method == 'POST':
        full_name = request.POST.get('your-name')
        date = request.POST.get('tour-date')
        time = request.POST.get('tour-time')
        phone = request.POST.get('your-phone')
        email = request.POST.get('your-email')
        special_request = request.POST.get('special-request')

        if full_name == "":
            messages.error(request, "Field cannot be blank")
            if date == "":
                messages.error(request, "Field cannot be blank")
                if time == "":
                    messages.error(request, "Field cannot be blank")
                    if phone == "":
                        messages.error(request, "Field cannot be blank")
                        if email == "":
                            messages.error(request, "Field cannot be blank")
                            if special_request == "":
                                messages.error(request, "Field cannot be blank")
        new_request = SchoolTourRequest.objects.create(
            full_name=full_name,
            date=date,
            time=time,
            phone=phone,
            email=email,
            special_request=special_request
        )
        new_request.save()

        #SEND MAIL
        subject = 'RETECH ACADEMY TOUR'
        message = 'Thank you for reaching us, We will contact you with the datails you have provided'
        send_mail(subject,message, email,["contact@greengarnetsfilms.com"],fail_silently=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'school-tour.html')

        


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

def EmailSubscribersView(request, *args, **kwargs):
    sub_emails = EmailSubscibers.objects.filter(is_verified=True)
    if request.method == 'POST':
        email = request.POST.get('sub_mail')
        if email == "":
            messages.error(request, 'Cannot be blank')
        if sub_emails.objects.filter(email=email).exists():
            messages.error(request, 'The email is already subscribed')
        new_sub = EmailSubscibers.objects.create(email=email)
        new_sub.save()
        messages.success(request, 'Successfully subscribed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))