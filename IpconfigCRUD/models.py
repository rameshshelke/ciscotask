from django.db import models

# Create your models here.

class IPDATA(models.Model):
    sapid=models.CharField(max_length=100)
    hostName=models.CharField(max_length=100)
    loopback=models.CharField(max_length=100)
    macid=models.CharField(max_length=100)

    class Meta:
        db_table='ip_info'
