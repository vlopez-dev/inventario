from django.db import models

# Create your models here.

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)   






    def add(self):
            self.save


    def __str__(self):
            return self.nombre
