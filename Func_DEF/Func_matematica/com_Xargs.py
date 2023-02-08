def soma(*val):
    resul = 0
    for i in val:
        resul += i
    return resul

def sub(*val):
    resul = 0
    for i in val:
        resul -= i
    return resul

def mult(*val):
    resul = 0
    for i in val:
        resul *= i
    return resul

def div(*val):
    resul = 0
    for i in val:
        resul /= i
    return resul
