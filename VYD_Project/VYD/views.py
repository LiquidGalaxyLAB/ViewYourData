
from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from django.views.decorators.csrf import csrf_exempt
from Utils.PresentationManager.placemark_generator import MarkersTour
from kmls_management.models import Kml

from .forms import UrlForm
from Utils.ParseManager.parse_manager import ParseManager


def submit_url(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            url = form.cleaned_data['url']

            print url

            parseManager = ParseManager.getParseManager(url, True)

            # redirect to a new URL:
            return HttpResponseRedirect('/VYD/layers/create/downloadPage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()

    return render(request, 'url_submit.html', {'form': form})

def download_page(request):
    # if this is a POST request we need to process the form data

    return render(request, 'loading_page.html')

@csrf_exempt
def download_file(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        parseManager = ParseManager.getParseManager("")
        parseManager.parse()
        name = parseManager.get_file_name()
        print name
        type = parseManager.get_type_file()

        request.session['name'] = name
        request.session['type'] = type

        return HttpResponseRedirect('/VYD/layers/create/fileInfo/')

    # if a GET (or any other method) we'll create a blank form
    else:

        return HttpResponseRedirect('/VYD/layers/create/submitUrl/')


def file_info_view(request):
    return render(request, 'file_type.html')

@csrf_exempt
def select_data_of_header(request):

    type_location = request.POST.get(u"\u201dtype_location\u201d")
    data_loc = request.POST.get('data_loc')
    parseManager = ParseManager.getParseManager("")

    print "Location data"

    # I rest 1 for prosecute correctly on the parseManager
    if type_location == "coor":
        print "HEy I'm coordinates"
        parseManager.coor_lat = int(request.POST['location_lat'])-1
        parseManager.coor_lng = int(request.POST['location_lng'])-1
        print "Coor Lat: "+ str(parseManager.coor_lat)
        print "Coor Lng: "+ str(parseManager.coor_lng)

    elif type_location == "name":
        parseManager.extra_location = request.POST['extra_location']
        parseManager.location_name = int(request.POST['location_headers_selected'])-1
        print "Location: " + str(parseManager.location_name)
        print "Extra Location" + parseManager.extra_location

    request.session['headers'] = parseManager.get_header()

    if data_loc == None:
        parseManager.type_loc = type_location
        return render(request, 'data_header_selector.html')
    else:
        parseManager.data_loc = int(data_loc)-1
        print "Data loc: " + str(parseManager.data_loc)
        return HttpResponseRedirect('/VYD/layers/create/loadParseData')



@csrf_exempt
def redirect_for_type_location(request):

    parseManager = ParseManager.getParseManager("")
    request.session['headers'] = parseManager.get_header()

    typelocation = request.POST['type_location']
    if typelocation == "1":
        return render(request, 'location_name_selector.html')
    elif typelocation == "2":
        return render(request, 'location_coordinates_selector.html')


@csrf_exempt
def load_parse_data(request):
    return render(request, 'load_parse_data.html')


@csrf_exempt
def parse_data(request):

    parseManager = ParseManager.getParseManager("")

    if parseManager.type_loc == "name":
        print parseManager.get_data_by_location(parseManager.data_loc, parseManager.location_name, parseManager.extra_location)
    elif parseManager.type_loc == "coor":
        print parseManager.get_data_by_coordinates(parseManager.data_loc, parseManager.coor_lat, parseManager.coor_lng)

    else:
        return render(request, 'error_page.html')

    return HttpResponseRedirect('/VYD/layers/create/viewDataAndLocation/')


@csrf_exempt
def view_data_and_location_selected(request):

    parseManager = ParseManager.getParseManager("")

    request.session['data_set'] = ParseManager.data

    setData=[]
    setCoordinates = []

    for line in parseManager.data[0]:
        print line
        setData.append(line['data'])


    #print "DATA In PARSE MANAGER : "
    #print parseManager.data


    return render(request, 'view_data_location_selected.html', {'data_set': parseManager.data[0]})

@csrf_exempt
def error_page(request):
    return render(request, 'error_page.html')

@csrf_exempt
def presentation_selector(request):
    return render(request, 'presentation_menu.html')

@csrf_exempt
def make_KML(request):

    kml_name = request.POST.get('kml_name')
    icon_marker = request.POST.get('icon_marker')

    parseManager = ParseManager.getParseManager("")

    print parseManager.data

    markerTours = MarkersTour(parseManager.data[0], "Test", "http://3.bp.blogspot.com/-qu3E7CIu4_E/T40o87HKKDI/AAAAAAAAAz8/b4hKRLCJbNs/s1600/wally.png")

    markerTours.makeFile()

    kml_file = Kml(name="Test.kml", visibility=False )
    kml_file.save()
    return HttpResponseRedirect('/VYD/KmlManager/kmls')

