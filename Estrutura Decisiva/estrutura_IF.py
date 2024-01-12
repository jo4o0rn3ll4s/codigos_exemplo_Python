# DE FORMA TRADICIONAL
val = int(input('Digite um valor: '))

if val < 10:
    print(f'{val} é MENOR que 10')
elif val > 10:
    print(f'{val} é MAIOR que 10')
else:
    print(f'{val} É 10')


# OU DE FORMA LINEAR
num = int(input('Digite um numero: '))
print(f'o numero {num} é menor que 10' if num < 10 else f'o numero {num} é maior que 10' if num > 10 else 'o numero é o próprio 10')
