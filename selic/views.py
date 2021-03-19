from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ola(request):
    return HttpResponse("<h1>Olá Rafael</h1>")

def rafael(request):
    return HttpResponse("<p>Rafael Gomes</p>")