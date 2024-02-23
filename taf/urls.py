from django.contrib import admin
from django.urls import path
from taf import views

urlpatterns = [
    #path('', views.eacf1_masculino, name='eacf1_masculino'),
    path('', views.home, name='home'),
    path('eacf1_masculino/', views.eacf1_masculino, name='eacf1_masculino'),
    path('eacf6_masculino/', views.eacf6_masculino, name='eacf6_masculino'),
    path('resultado/', views.resultado, name='resultado'),
    path('eacf1_feminino/', views.eacf1_feminino, name='eacf1_feminino'),
    path('eacf6_feminino/', views.eacf6_feminino, name='eacf6_feminino'),
    path('resultado_feminino/', views.resultado_feminino, name='resultado_feminino'),
]
