#COM A ESTRUTURA NORMAL DE (VALOR INICIAL, CONDIÇÃO, INCREMENTO|DECREMENTO)
rep = int(input('Digite o numero de Repetições desejadas: '))

for i in range(1,rep+1,1):
    print(f'Irei repitir essa frase {rep} vezes\nJá escrevi {i} vezes')


#UTILIZANDO PARA FAZER UMA VARREDURA EM UMA VARIAVEL COMPOSTA
lista = ['a','b','c']

for elemento in lista:
    print(elemento)