from django.contrib import admin
from .models import Gallery, AcademicSession, AcademicTerm
# Register your models here.


admin.site.register(Gallery)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)