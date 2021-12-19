from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def displayThumbnail(request, *args, **kwargs):
    sliders = SliderImage.objects.all(),
    quicklinks = QuicklinkImages.objects.all()
    context = {
        'sliders':sliders,
        'quicklinks': quicklinks,
        'IndexEvent': IndexEvent400412.objects.all(),
        'indexwhyus': IndexWhyUs700493.objects.all(),
    }
    return render(request, 'utils/sliders.html', context)