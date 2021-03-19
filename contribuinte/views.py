from django.shortcuts import render


def incluir_na_mao(request):
    return render(request, "contribuinte/incluir-na-mao.html")
