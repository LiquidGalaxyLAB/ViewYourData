
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
from models import Kml
from django.http import HttpResponseRedirect
from django.shortcuts import render
import subprocess





@csrf_exempt
def syncKML(request):


    id = request.POST['id']
    print "HEY"+str(id)
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
def deleteKML(request):
    id = request.POST['id']
    kml = Kml.objects.filter(id=id)
    kml.delete()
    return HttpResponseRedirect('/VYD/KmlManager/')

@csrf_exempt
def kmlManagerView(request):
    kmls = Kml.objects.all()
    return render(request, 'manage_kml.html', {'kmls': kmls})



def syncKmlsToGalaxy():
    filePath = "/tmp/kml/kmls.txt"
    serverPath = "/var/www/html"
    os.system("sshpass -p 'lqgalaxy' scp "+filePath+" lg@172.26.17.21:"+serverPath)


def syncKmlsFile():

    p = subprocess.Popen("ipconfig getifaddr en0", shell=True, stdout=subprocess.PIPE)
    ip_server = p.communicate()[0]

    os.system("rm /tmp/kml/kmls.txt")
    os.system("touch /tmp/kml/kmls.txt")
    file = open("/tmp/kml/kmls.txt",'w')

    for i in Kml.objects.filter(visibility=True):
        file.write("http://"+ str(ip_server)[0:(len(ip_server)-1)]+":8000/static/"+i.name+"\n")

    file.close()
