from rest_framework.serializers import ModelSerializer

from IpconfigCRUD.models import IPDATA

class IPDATASerializer(ModelSerializer):
    class Meta:
        model=IPDATA
        fields='__all__'