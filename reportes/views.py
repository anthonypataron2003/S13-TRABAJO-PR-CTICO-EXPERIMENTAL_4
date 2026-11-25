from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.conf import settings
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from inventario.models import Producto
@login_required
def pdf(request):
    if not settings.ENABLE_REPORTS: raise Http404
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="inventario.pdf"'
    rows=[['Producto','Categoría','Precio USD','Stock']]
    for p in Producto.objects.select_related('categoria'): rows.append([p.nombre,p.categoria.nombre,str(p.precio),str(p.stock)])
    table=Table(rows,repeatRows=1,colWidths=[155,135,90,60]);table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#176b65')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.4,colors.grey),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
    SimpleDocTemplate(response).build([Paragraph('Reporte de inventario — Variante B',getSampleStyleSheet()['Title']),Spacer(1,15),table]);return response
