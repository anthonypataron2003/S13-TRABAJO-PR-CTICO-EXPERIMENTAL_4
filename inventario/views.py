from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Sum
from django.views.decorators.http import require_POST
from .models import Producto,Categoria
from .forms import ProductoForm,CategoriaForm
@login_required
def dashboard(request):
    qs=Producto.objects.select_related('categoria').order_by('nombre')
    q=request.GET.get('q','')
    return render(request,'dashboard.html',{'productos':qs.filter(nombre__icontains=q),'q':q,'total':qs.count(),'unidades':qs.aggregate(n=Sum('stock'))['n'] or 0,'categorias':Categoria.objects.count()})
@login_required
def editar(request,pk=None):
    obj=get_object_or_404(Producto,pk=pk) if pk else None
    form=ProductoForm(request.POST if request.method=='POST' else None,instance=obj)
    if request.method=='POST' and form.is_valid(): form.save(); return redirect('dashboard')
    return render(request,'form.html',{'form':form,'titulo':'Editar producto' if obj else 'Nuevo producto'})
@login_required
@require_POST
def eliminar(request,pk):
    get_object_or_404(Producto,pk=pk).delete(); return redirect('dashboard')
@login_required
def categorias(request):
    form=CategoriaForm(request.POST if request.method=='POST' else None)
    if request.method=='POST' and form.is_valid(): form.save(); return redirect('categorias')
    return render(request,'categorias.html',{'form':form,'categorias':Categoria.objects.all()})
