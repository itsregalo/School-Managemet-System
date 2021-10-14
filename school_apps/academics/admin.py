from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(ExamBank)

@admin.register(Result)
class ResultsAdmin(ImportExportModelAdmin):
    list_display = ['student','session','term','current_class','subject']
