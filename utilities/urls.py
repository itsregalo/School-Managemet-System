from django.urls import path

from django.urls import path
from . import views

app_name = 'utils'

urlpatterns = [
    path('sliders/', views.displayThumbnail, name='sliders')
]
