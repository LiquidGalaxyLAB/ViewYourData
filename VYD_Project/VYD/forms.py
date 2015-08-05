__author__ = 'Marc Sole Farre'

from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='url')
