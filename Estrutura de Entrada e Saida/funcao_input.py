#Quando utilizado, a função input retorna o valor com o tipo string
nome = input('Qual o seu nome?- ')
#Para retornar um numero, é necessario o uso de um iterador:
#int() para retornar um numero inteiro
idade = int(input('Qual a sua idade?- '))
#float() para retornar um numero com ponto flutuante (numero real)
peso = float(input('Quanto você pesa?- '))

print(f'Olá {nome}, você esta com {idade} anos e tem {peso}kg.')
#Temos tambem o tipo booleano, quando existe algum valor no input, retorna True, quando há nada, False
confirm = bool(input('Certo? " "-Não "Qualquer tecla"-Sim'))

print(confirm)