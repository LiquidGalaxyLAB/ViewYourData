__author__ = 'Marc'

from django.conf.urls import include, url
from VYD import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

                  url(r'^layers/create/submitUrl', views.submit_url),
                  url(r'^layers/create/downloadPage', views.download_page),
                  url(r'^layers/create/downloadFile', views.download_file),
                  url(r'^layers/create/fileInfo', views.file_info_view),
                  url(r'^layers/create/selectLocation', views.redirect_for_type_location),
                  url(r'^layers/create/selectData', views.select_data_of_header),
                  url(r'^layers/create/loadParseData', views.load_parse_data),
                  url(r'^layers/create/parseData', views.parse_data),
                  url(r'^layers/create/viewDataAndLocation', views.view_data_and_location_selected),
                  url(r'^layers/create/error', views.error_page),
                  url(r'^layers/create/presentationMenu', views.presentation_selector),
                  url(r'^layers/create/makeCircle', views.make_circle_KML),
                  url(r'^layers/create/makeMarker', views.make_marker_KML),
                  url(r'^layers/create/makeDome', views.make_dome_KML),
                  url(r'^layers/create/makeCylinder', views.make_cylinder_KML),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
