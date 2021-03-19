from django.shortcuts import render
from selic import utils


def incluir_na_mao(request):
    if request.method == 'POST':
        if utils.validar_mes(request.POST["mes"]):
            mes = int(request.POST["mes"])
        if utils.validar_ano(request.POST["ano"]):
            ano = int(request.POST["ano"])
        if utils.validar_valor(request.POST["valor"]):
            valor = float(request.POST["valor"])
    print(mes + ano + valor)
    return render(request, 'selic/incluir-na-mao.html')


def ola(request):
    contexto = {"nome": "jose", "idade": 100}
    return render(request, 'selic/ola.html', contexto)


def rafael(request):
    contexto = {"nome": "Rafael Gomes", "idade": 17}
    return render(request, 'selic/rafael.html', contexto)

# def rafael(request):
#    return HttpResponse("<p>Rafael Gomes</p>")
