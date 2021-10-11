from django.db import models


# Create your models here.
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=200)
    descripcion_articulo = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=200)
    id_area = models.name = models.ForeignKey('area.Area', on_delete=models.CASCADE)
    imagen_articulo = models.ImageField(upload_to='%articulo/%imagenes',blank=True)

       
       
       
       
def add(self):
    self.save

def __str__(self):
    return self.name
