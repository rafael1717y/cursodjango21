from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def ola(request):
    contexto = {"nome": "jose", "idade": 100}
    return render(request, 'selic/ola.html', contexto)


def rafael(request):
    contexto = {"nome": "Rafael Gomes", "idade": 17}
    return render(request, 'selic/rafael.html', contexto)

# def rafael(request):
#    return HttpResponse("<p>Rafael Gomes</p>")
