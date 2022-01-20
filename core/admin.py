from django.contrib import admin
from .models import (Gallery, AcademicSession, AcademicTerm,
                        StudentClass, NoticeCategory, Notice, Event,
                        SchoolTourRequest)
# Register your models here.


admin.site.register(Gallery)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)
admin.site.register(StudentClass)
admin.site.register(NoticeCategory)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(SchoolTourRequest)