from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ['admission_no','first_name','last_name','gender','in_class']

admin.site.register(Parent)
admin.site.register(Staff)
admin.site.register(Teacher)