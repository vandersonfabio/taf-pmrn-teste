"""taf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taf import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.eacf1_masculino, name='eacf1_masculino'),
    path('eacf1_masculino/', views.eacf1_masculino, name='eacf1_masculino'),
    path('eacf6_masculino/', views.eacf6_masculino, name='eacf6_masculino'),
    path('resultado/', views.resultado, name='resultado'),
    path('eacf1_feminino/', views.eacf1_feminino, name='eacf1_feminino'),
    path('eacf6_feminino/', views.eacf6_feminino, name='eacf6_feminino'),
    path('resultado_feminino/', views.resultado_feminino, name='resultado_feminino'),
]
