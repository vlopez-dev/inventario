from django.db import models

from area.models import Area





ARTICULOS_TIPO = [
            ('electronico', 'Electronico'),

            ('mobiliario', 'Mobiliario'),
            
        ]





class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=30)
    descripcion_articulo = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=30,choices=ARTICULOS_TIPO)
    id_area = models.name = models.ForeignKey('area.Area', on_delete=models.CASCADE)
    imagen_articulo = models.ImageField(upload_to='%articulo/%imagenes',blank=True)
    cantidad = models.IntegerField()



    def __str__(self):
        return self.nombre_articulo
    
    def add(self):
        self.save

class Movimiento(Articulo):
    destino = models.CharField(max_length=50)
    class Meta:
        proxy:True
        