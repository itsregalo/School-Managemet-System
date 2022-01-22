from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from accounts.models import EmailSubscibers
from blog.models import Blog
from django.utils import timezone
# Create your views here.


def IndexView(request, *args, **kwargs):
    notices = Notice.objects.filter(is_approved=True).order_by('-timestamp')[:3]
    events = Event.objects.filter(is_approved=True).order_by('-event_date')[:3]
    context = {
        'notices':notices,
        'latest_news':Blog.objects.last(),
        'events':events
    }
    return render(request, 'index.html', context)

def ApplicationView(request, *args, **kwargs):
    return render(request, 'core/apply-procedure.html')

def AcademyLife(request, *args, **kwargs):
    return render(request, 'core/academy-life.html')

def GalleryView(request, *args, **kwargs):
    images = Gallery.objects.filter(is_approved=True)

    context = {
        'images':images
    }
    return render(request, 'core/gallery.html', context)

def EventListView(request, *args, **kwargs):
    events = Event.objects.filter(is_approved=True)
    context = {
        'events':events
    }
    return render(request, 'core/event-calendar.html', context)

def SchoolTourRequestView(request, *args, **kwargs):
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
    return render(request, 'core/school-tour.html')

def Notices(request, *args, **kwargs):
    notices = Notice.objects.all().order_by('-timestamp')
    context = {
        'notices':notices
    }
    return render(request, 'core/notice-list.html', context)

def DonationPageView(request, *args, **kwargs):
     return render(request, 'core/donate.html')  

def ScholarshipView(request, *args, **kwargs):
    return render(request, 'core/scholarships.html')     

def AlumniView(request, *args, **kwargs):
    return render(request, 'core/alumni.html')

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
    return render(request, 'core/contact.html')

def AboutUs(request, *args, **kwargs):
    return render(request, 'core/about-us.html')

def ContactPage(request, *args, **kwargs):
    return render(request, 'core/contact.html')

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

def handle404(request, exception):
    return render(request, 'core/404.html')