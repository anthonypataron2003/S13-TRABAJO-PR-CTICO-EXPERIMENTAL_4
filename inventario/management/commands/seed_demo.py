from django.core.management.base import BaseCommand
from inventario.models import Categoria,Producto
class Command(BaseCommand):
    help='Crea datos ficticios de ejemplo'
    def handle(self,*args,**kwargs):
        for nombre,cat,precio,stock in [('Teclado','Periféricos',25,12),('Mouse','Periféricos',15,3),('Monitor','Pantallas',150,8),('Cable HDMI','Accesorios',8,2),('Memoria USB','Accesorios',12,20)]:
            c,_=Categoria.objects.get_or_create(nombre=cat)
            Producto.objects.get_or_create(nombre=nombre,defaults={'categoria':c,'precio':precio,'stock':stock,'minimo':5})
        self.stdout.write(self.style.SUCCESS('Datos de ejemplo disponibles.'))
