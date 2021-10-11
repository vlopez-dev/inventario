from django.db import models

from empresa.models import Empresa

# Create your models here.

class Area(models.Model):
 id_area= models.AutoField(primary_key=True)
     

 id_empresa = models.name = models.ForeignKey('empresa.Empresa',on_delete=models.CASCADE)
 nombre = models.CharField(max_length=200)









def add(self):
            self.save


def __str__(self):
            return self.nombre
