import re


def validar_ni(ni):
    ni = str(ni)
    ni = re.sub('\\D', '', ni)
    if not ni or (len(ni) != 11 and len(ni) != 14):
        return False
    elif len(ni) == 11:
        return validar_cpf(ni)
    elif len(ni) == 14:
        return validar_cnpj(ni)


def validar_cpf(ni):
    ni = str(ni)
    ni = re.sub('\\D', '', ni)

    if not ni or len(ni) != 11 or ni == ni[::-1]:
        return False

    # Cálculo do 1. dígito verificador
    cpf = ni[:9]
    dv1 = _calcular_digito_verificaro_cpf(cpf)
    cpf += str(dv1)
    # Cálculo do 2. dígito verificador
    dv2 = _calcular_digito_verificaro_cpf(cpf)
    cpf += str(dv2)

    if cpf == ni:
        return cpf
    else:
        return False


def _calcular_digito_verificaro_cpf(cpf):
    soma_pesos = 0
    indice = 0
    if len(cpf) == 9:
        peso_inicial = 10
    else:
        peso_inicial = 11
    for peso in range(peso_inicial, 1, -1):
        soma_pesos += peso * int(cpf[indice])
        indice += 1
    dv = (soma_pesos * 10) % 11
    if dv == 10:
        dv = 0
    return dv


def _calculo_digito_verificador_cnpj(cnpj):
    soma_pesos = 0
    peso = 2
    for dig in cnpj[::-1]:  # início até o final de forma inversa
        soma_pesos += peso * int(dig)
        peso += 1
        if peso > 9:
            peso = 2
    dv = soma_pesos % 11
    if dv == 0 or dv == 1:
        dv = 0
    else:
        dv = 11 - dv
    return dv


def validar_cnpj(cnpj):
    ni = str(cnpj)
    ni = re.sub('\\D', '', ni)

    if not ni or len(ni) != 14 or ni == ni[::-1]:
        return False

    # Cálculo do 1. dígito verificador
    cnpj = ni[:12]
    dv1 = _calculo_digito_verificador_cnpj(cnpj)

    # Cálculo do 2. dígito verificador
    cnpj += str(dv1)
    dv2 = _calculo_digito_verificador_cnpj(cnpj)
    cnpj += str(dv2)

    if cnpj == ni:
        return cnpj
    else:
        return False
