
from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from django.views.decorators.csrf import csrf_exempt

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

            parseManager = ParseManager.getParseManager(url)

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