from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.


class NoticeInline(admin.TabularInline):
    model = NoticeFile

class NoticeAdmin(admin.ModelAdmin):
    inlines = [NoticeInline,]


admin.site.register(Notice, NoticeAdmin)

admin.site.register(Gallery)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)
admin.site.register(StudentClass)
admin.site.register(NoticeCategory)
admin.site.register(Event)
admin.site.register(SchoolTourRequest)

