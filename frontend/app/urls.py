# my_django_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('ir_registro/', views.ir_registro, name='ir_registro'),
    path('signin/', views.signin, name='signin'),
    path('principal/', views.principal, name='principal')
]