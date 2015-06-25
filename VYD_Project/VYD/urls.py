__author__ = 'Marc'

from django.conf.urls import include, url
from django.contrib import admin
from VYD import views


urlpatterns = [

    url(r'^layers/create/submitUrl', views.submitUrl),
    #url(r'^layers/create/downloadFile')
]
