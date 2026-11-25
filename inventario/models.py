from django.db import models
class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    def __str__(self): return self.nombre
class Producto(models.Model):
    nombre=models.CharField(max_length=150)
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    minimo=models.PositiveIntegerField(default=5)
    def __str__(self): return self.nombre
