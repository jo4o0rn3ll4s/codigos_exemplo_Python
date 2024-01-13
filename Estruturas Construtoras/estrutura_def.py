#FUNÇÃO QUE SOMA OS ARGUMENTOS A E B    
def soma_dois(a:float, b:float) -> float:
    '''
    a : int() -> primeiro argumento da função
    b : int() -> segundo arguemnto da função

    retorna -> soma de a+b
    '''
    valor = a + b
    return valor


#FUNÇÃO QUE COMPRIMENTA UMA PESSOA QUE PASSE OU NÃO O SOBRENOME
def comprimente(nome = '', sobrenome = '') -> None:
    '''
    [opcional] nome : str() -> argumento que captura o nome da pessoa
    [opcional] sobrenome : str() -> argumento que captura o sobrenome da pessoa

    retorna -> None 
    '''
    print(f'Olá {nome} {sobrenome}, bem vindo!')


#função com inumeros argumentos
def inumeros_argumentos(*argumentos) -> int:
    '''
    argumento : não tipado -> exemplo que mostra que inumeros argumentos podem ser passados sem que haja impecilho de serem de diferentes tipos

    retorna -> numero de argumentos passados na função
    '''
    for elemento in argumentos:
        print(f'Argumento: {elemento}')
    n_elementos = len(argumentos)
    return n_elementos
