from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
from django.views.generic import FormView
from models import Kml
from django.http import HttpResponseRedirect
from django.shortcuts import render
import subprocess

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import UploadKMLForm


@csrf_exempt
def syncKML(request):
    id = request.POST['id']

    if id != "-1":
        print "HEY" + str(id)
        kml = Kml.objects.filter(id=id)[0]
        print kml
        print "Hola"
        if kml.get_visivility():
            kml.visibility = False
            kml.save()
        else:
            kml.visibility = True
            kml.save()

    syncKmlsFile()
    syncKmlsToGalaxy()
    return HttpResponseRedirect('/VYD/KmlManager/kmls')


@csrf_exempt
def deleteKML(request, pk):
    kml = Kml.objects.filter(id=pk)[0]
    print pk
    os.system("rm kmls_management/static/" + str(kml) + ".kml")

    kml.delete()

    return HttpResponseRedirect('/VYD/KmlManager/kmls')


@csrf_exempt
def kmlManagerView(request):
    kmls = Kml.objects.all().order_by('-visibility')
    return render(request, 'manage_kml.html', {'kmls': kmls})


def syncKmlsToGalaxy():
    filePath = "/tmp/kml/kmls.txt"
    serverPath = "/var/www/html"
    os.system("sshpass -p 'lqgalaxy' scp " + filePath + " lg@172.26.17.21:" + serverPath)


def syncKmlsFile():
    p = subprocess.Popen("ipconfig getifaddr en0", shell=True, stdout=subprocess.PIPE)
    ip_server = p.communicate()[0]

    os.system("rm /tmp/kml/kmls.txt")
    os.system("touch /tmp/kml/kmls.txt")
    file = open("/tmp/kml/kmls.txt", 'w')

    for kml in Kml.objects.filter(visibility=True):
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] + ":8000/static/" + str(kml) + "\n")

    file.close()


class FileAddView(FormView):
    form_class = UploadKMLForm
    success_url = "/VYD/KmlManager/kmls"
    template_name = "import_kml.html"

    def form_valid(self, form):
        form.save(commit=True)
        return super(FileAddView, self).form_valid(form)


@csrf_exempt
def import_kml(request):
    # Handle file upload
    if request.method == 'POST':
        kml = Kml(file=request.FILES['file'], visibility=False)
        kml.save()

        # Redirect to the document list after POST
        return HttpResponseRedirect('/VYD/KmlManager/kmls')
    else:
        form = UploadKMLForm()  # A empty, unbound form



    # Render list page with the documents and the form
    return render_to_response(
        'import_kml.html',
        {'form': form},

    )