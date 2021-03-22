"""cursodjango21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from selic import views as selic_views
from contribuinte import views as contrib_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ola/', selic_views.ola),
    path('rafael/', selic_views.rafael),
    path('selic/incluir-na-mao/', selic_views.incluir_na_mao, name="selic_incluir_na_mao"),
    path('selic/listar-na-mao/', selic_views.listar_na_mao, name="selic_listar_na_mao"),
    path('contribuinte/incluir-na-mao/', contrib_views.incluir_na_mao, name="contribuinte_incluir_na_mao"),
]
