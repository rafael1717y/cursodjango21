def validar_mes(mes):
    try:
        mes = int(mes)
    except ValueError:
        return False
    if 1 <= mes <= 12:
        return True
    else:
        return False


def validar_ano(ano):
    try:
        ano = int(ano)
    except ValueError:
        return False
    if ano >= 2020:
        return True
    else:
        return False


def validar_valor(valor):
    try:
        valor = float(valor)
    except ValueError:
        return False
    if valor >= 0.01:
        return True
    else:
        return False
