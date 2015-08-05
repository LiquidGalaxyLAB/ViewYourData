__author__ = 'Marc'

from models import Kml
from django import forms

class UploadFileForm(forms.Form):
    class Meta:
        model = Kml