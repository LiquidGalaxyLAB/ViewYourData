__author__ = 'Marc'

from models import Kml
from django.forms import ModelForm

class UploadFileForm(ModelForm):
    class Meta:
        model = Kml
        fields = "__all__"