from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UrlForm


def submitUrl(request):
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
            # redirect to a new URL:
            return HttpResponseRedirect('/VYD/layers/create/downloadFile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()

    return render(request, 'url_submit.html', {'form': form})

def downloadFile(request):
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
            # redirect to a new URL:
            return HttpResponseRedirect('/VYD/layers/create/downloadFile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()

    return render(request, 'url_submit.html', {'form': form})