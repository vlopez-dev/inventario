from django.db import models

from area.models import Area


# Create your models here.
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=200)
    descripcion_articulo = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=200)
    id_area = models.name = models.ForeignKey('area.Area', on_delete=models.CASCADE)
    imagen_articulo = models.ImageField(upload_to='%articulo/%imagenes',blank=True)
    cantidad = models.IntegerField()

       
       
       
    def __str__(self):
        return self.nombre_articulo
    
    def add(self):
        self.save
    
    
    
class Movimiento(models.Model):
    id_movimiento=models.AutoField(primary_key=True)
    id_articulo = models.name=models.ForeignKey('articulo.Articulo',on_delete=models.CASCADE)
    id_area = models.name=models.ForeignKey('area.Area',on_delete=models.CASCADE)
    cantidadmovimiento = models.IntegerField()
    motivo = models.CharField(max_length=100)
        
        
        
        
        
       
    def __str__(self):
        return self.motivo
    
    def add(self):
        self.save