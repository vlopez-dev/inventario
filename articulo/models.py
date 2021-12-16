from django.db import models

from area.models import Area





ARTICULOS_TIPO = [
            ('electronico', 'Electrónico'),

            ('mobiliario', 'Mobiliario'),

        ]





class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=30)
    descripcion_articulo = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=30,choices=ARTICULOS_TIPO,default='electronico')
    imagen_articulo = models.ImageField(upload_to='%articulo/%imagenes',blank=True)
    desechable = models.BooleanField()



    def __str__(self):
        return self.nombre_articulo

    def add(self):
        self.save

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)

    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    area_origen = models.CharField(max_length=100)
    area_destino= models.name=models.ForeignKey('area.Area',on_delete=models.CASCADE)

    cantidad_mover = models.IntegerField()




