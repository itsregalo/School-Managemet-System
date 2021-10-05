from django.db import models
from django.db.models.deletion import DO_NOTHING
from academics.models import Class
# Create your models here.


class FeeStructure(models.Model):
    class_name = models.ForeignKey(Class, on_delete=DO_NOTHING)
    date = models.DateField()
    file = models.FileField(upload_to=f'fee_structure/{class_name.name}/%Y')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.class_name.name} - {self.date}"
    
