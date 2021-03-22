from django.shortcuts import render
from selic import utils
from .models import Selic


def listar_na_mao(request):
    contexto = {'lista': Selic.objects.all()}
    return render(request, 'selic/listar-na-mao.html', contexto)


def incluir_na_mao(request):
    contexto = {}
    if request.method == 'POST':
        if utils.validar_mes(request.POST['mes']):
            mes = int(request.POST["mes"])
        else:
            contexto['erro_mes'] = f'O mês {request.POST["mes"]} é inválido.'
        if utils.validar_ano(request.POST["ano"]):
            ano = int(request.POST["ano"])
        else:
            contexto['erro_ano'] = f'O ano {request.POST["ano"]} é inválido.'
        if utils.validar_valor(request.POST["valor"]):
            valor = float(request.POST["valor"])
        else:
            contexto['erro_valor'] = f'O valor {request.POST["valor"]} é inválido.'

        if not contexto:
            selic = Selic()
            selic.mes = mes
            selic.ano = ano
            selic.ano_mes = int(str(ano) + str(mes).zfill(2))
            selic.valor = valor
            selic.save()
            contexto['sucesso'] = 'Selic incluída com sucesso.'

    return render(request, 'selic/incluir-na-mao.html', contexto)


def ola(request):
    contexto = {"nome": "jose", "idade": 100}
    return render(request, 'selic/ola.html', contexto)


def rafael(request):
    contexto = {"nome": "Rafael Gomes", "idade": 17}
    return render(request, 'selic/rafael.html', contexto)

# def rafael(request):
#    return HttpResponse("<p>Rafael Gomes</p>")
