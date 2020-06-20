from django.shortcuts import render

# Create your views here.
from IpconfigCRUD.serializers import IPDATASerializer
from IpconfigCRUD.models import IPDATA

from rest_framework.viewsets import ModelViewSet

class IPDATAViewset(ModelViewSet):
    queryset = IPDATA.objects.all()
    serializer_class = IPDATASerializer


from django.shortcuts import render
import json

import subprocess

def get_Ipconfig(req):
    proc = subprocess.check_output("ipconfig").decode('utf-8')
    jsonserialize = json.dumps(proc)
    return render(req,"ipdata.html",{"ipconfigs":json.loads(jsonserialize)})

