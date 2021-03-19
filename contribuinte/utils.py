import re


def validar_cpf(ni):
    ni = str(ni)
    ni = re.sub('\\D', '', ni)

    if not ni or len(ni) != 11:
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


def validar_cnpj(cnpj):
    pass


print(validar_cpf("052.605.366-65"))
