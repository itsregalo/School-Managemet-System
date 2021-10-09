from django.contrib import admin
from .models import (Gallery, AcademicSession, AcademicTerm,
                        StudentClass, NewsCategory, News, Event)
# Register your models here.


admin.site.register(Gallery)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)
admin.site.register(StudentClass)