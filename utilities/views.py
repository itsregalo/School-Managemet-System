from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def displayThumbnail(request, *args, **kwargs):
    sliders = SliderImage.objects.all()
    context = {
        'sliders':sliders
    }
    return render('utils/sliders.html', context)