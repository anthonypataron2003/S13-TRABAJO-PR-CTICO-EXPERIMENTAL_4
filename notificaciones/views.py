from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from django.db.models import F
from inventario.models import Producto
@login_required
def alertas(request):
    if not settings.ENABLE_NOTIFICATIONS: raise Http404
    return render(request,'alertas.html',{'productos':Producto.objects.filter(stock__lte=F('minimo'))})
