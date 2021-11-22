from django.urls import path

from utilities.models import SliderImage
from . import views

app_name = 'utils'

urlpatterns = [
    path('sliders/', SliderImage, name='sliders')
]
