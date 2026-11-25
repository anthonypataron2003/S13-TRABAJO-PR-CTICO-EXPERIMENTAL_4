from django.urls import path
from .views import alertas
urlpatterns=[path("",alertas,name="alertas")]
