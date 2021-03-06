"""sunriseportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='user')),
    path('', include('core.urls', namespace='core')),
    path('academics/', include('school_apps.academics.urls', namespace='academics')),
    path('finance/', include('school_apps.finance.urls', namespace='finance')),
    path('student/', include('school_apps.studentportal.urls', namespace='studentportal')),
    path('staff/', include('school_apps.staffportal.urls', namespace='staff')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('utilities/', include('utilities.urls', namespace='utils')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header="RETECH Academy"
admin.site.site_title="RETECH ACADEMY"

handler404 = 'core.views.handle404'