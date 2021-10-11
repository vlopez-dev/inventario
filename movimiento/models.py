from django.db import models

# Create your models here.
class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_articulo = models.name = models.ForeignKey('articulo.Articulo', on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50)
    
    id_area = models.name = models.ForeignKey('area.Area', on_delete=models.CASCADE)
    motivo = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=True)
    fecha = models.DateTimeField(null=True)
    
    
    


    def add(self):
            self.save


    def __str__(self):
            return self.tipo_movimiento
