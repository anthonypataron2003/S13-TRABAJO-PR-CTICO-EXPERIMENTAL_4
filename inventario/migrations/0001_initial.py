from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[migrations.CreateModel(name='Categoria',fields=[('id',models.BigAutoField(primary_key=True,serialize=False)),('nombre',models.CharField(max_length=100,unique=True))]),migrations.CreateModel(name='Producto',fields=[('id',models.BigAutoField(primary_key=True,serialize=False)),('nombre',models.CharField(max_length=150)),('precio',models.DecimalField(max_digits=10,decimal_places=2)),('stock',models.PositiveIntegerField(default=0)),('minimo',models.PositiveIntegerField(default=5)),('categoria',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,to='inventario.categoria'))])]
