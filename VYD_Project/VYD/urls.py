__author__ = 'Marc'

from django.conf.urls import include, url
from django.contrib import admin
from VYD import views


urlpatterns = [

    url(r'^layers/create/submitUrl', views.submit_url),
    url(r'^layers/create/downloadPage', views.download_page),
    url(r'^layers/create/downloadFile', views.download_file),
    url(r'^layers/create/fileInfo', views.file_info_view),


]
