from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[path('entrar/',LoginView.as_view(template_name='login.html'),name='login'),path('salir/',LogoutView.as_view(),name='logout')]
