from django.db import models

from area.models import Area





ARTICULOS_TIPO = [
            ('Electronico', 'Electrónico'),

            ('Mobiliario', 'Mobiliario'),
            ('Toner', 'Toner'),


        ]





class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=30)
    descripcion_articulo = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=30,choices=ARTICULOS_TIPO,default='electronico')
    image = models.ImageField(blank=True, upload_to='media/')
    desechable = models.BooleanField(null=True,blank=True)
    



    def __str__(self):
        return self.nombre_articulo

    def add(self):
        self.save

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    # area_origen = models.CharField(max_length=100)
    area_origen = models.name=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='area_origen')
    area_destino= models.name=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='area_destino')

    cantidad_mover = models.IntegerField()




