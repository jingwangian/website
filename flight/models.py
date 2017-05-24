from django.db import models
from cgi import maxlen

# Create your models here.

class EC2Info(models.Model):
    name = models.CharField(max_length=250)
    public_dns = models.CharField(max_length=250)
    public_ip = models.GenericIPAddressField()
    
    def __str__(self):
        return self.name+' -- '+self.public_dns
