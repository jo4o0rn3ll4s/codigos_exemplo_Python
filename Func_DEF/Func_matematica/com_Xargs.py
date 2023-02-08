def soma(*val):
    """
    :val-> os valores que desejam somar
    :retorna-> a soma de todos os elementos descomprimidos de *val
    """
    resul = 0
    for i in val:
        resul += i
    return resul


def sub(total=0, *val):
    """
    :total-> Valor que será subtraido pelo *val
    :val-> os valores de substradores
    :retorna-> a subtração de todos os elementos descomprimidos de *val
    """
    for i in val:
        total -= i
    return total


def mult(*val):
    """
    :val-> os valores que desejam multiplicar
    :retorna-> o multiplo de todos os elementos descomprimidos de *val
    """
    resul = 1
    for i in val:
        resul *= i
    return resul


def div(total=0, *val):
    """
    :total-> Valor que será dividido pelo *val
    :val-> os valores de divisão
    :retorna-> o valor dividido por todos os elementos descomprimidos de *val
    """
    for i in val:
        total /= i
    return total
