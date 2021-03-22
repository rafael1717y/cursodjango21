from django.shortcuts import render
from contribuinte import utils
from .models import Contribuinte


def incluir_na_mao(request):
    contexto = {}

    if request.method == 'POST':
        contato = request.POST['contato']
        ni_valido = utils.validar_ni(request.POST['ni'])
        if ni_valido:
            ni = ni_valido
        else:
            contexto['erro_ni'] = f'0 ni {request.POST["ni"]} é inválido.'
        if request.POST['nome']:
            nome = request.POST['nome']
        else:
            contexto['erro_nome'] = "O nome não pode ficar em branco."
        if not contexto:
            contribuinte = Contribuinte()
            contribuinte.ni = ni
            contribuinte.nome = nome
            contribuinte.contato = contato
            contribuinte.save()
            contexto['sucesso'] = 'Contribuinte incluído com sucesso.'
    return render(request, "contribuinte/incluir-na-mao.html", contexto)
