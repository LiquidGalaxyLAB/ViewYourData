__author__ = 'Marc'

from models import Kml
from django.forms import ModelForm


class UploadKMLForm(ModelForm):
    class Meta:
        model = Kml
        fields = ["visibility", "file"]