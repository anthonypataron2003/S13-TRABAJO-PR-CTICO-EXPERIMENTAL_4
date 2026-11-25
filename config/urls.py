from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [path('admin/',admin.site.urls),path('cuenta/',include('usuarios.urls')),path('',include('inventario.urls'))]
if settings.ENABLE_REPORTS: urlpatterns.append(path('reportes/',include('reportes.urls')))
if settings.ENABLE_NOTIFICATIONS: urlpatterns.append(path('alertas/',include('notificaciones.urls')))
