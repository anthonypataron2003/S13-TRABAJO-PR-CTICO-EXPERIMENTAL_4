from django.urls import path
from . import views
urlpatterns=[path('',views.dashboard,name='dashboard'),path('productos/nuevo/',views.editar,name='nuevo'),path('productos/<int:pk>/editar/',views.editar,name='editar'),path('productos/<int:pk>/eliminar/',views.eliminar,name='eliminar'),path('categorias/',views.categorias,name='categorias')]
