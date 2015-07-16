
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
from models import Kml
from django.http import HttpResponseRedirect


def syncKmlsToGalaxy():
    filePath = "/tmp/kml/kmls.txt"
    serverPath = "/var/www/html"
    os.system("sshpass -p 'lqgalaxy' scp "+filePath+" lg@172.26.17.21:"+serverPath)

@csrf_exempt
def syncKmlsFile(request):
    ip_server=os.popen("ipconfig getifaddr en0")
    os.system("rm /tmp/kml/kmls.txt")
    os.system("touch /tmp/kml/kmls.txt")
    file = open("/tmp/kml/kmls.txt",'w')

    for i in Kml.objects.filter(visibility=True):
        file.write("http://"+ ip_server +":8000/static/"+i.url+"\n")

    file.close()
