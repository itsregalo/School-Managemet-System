from .models import Student, Parent, Staff
from django.forms import ModelForm


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'