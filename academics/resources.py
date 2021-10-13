from import_export import resources
from .models import Result

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result