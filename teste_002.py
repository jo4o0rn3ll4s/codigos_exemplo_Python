rep = int(input('Escreve o numero de repetições desejadas: '))

for r in range(1,rep+1, 1): #começo, fim, incremento(apenas numero) ou decremento(- o numero)
   
    print('Irei repetir essa frase {} vezes'.format(rep))
    print('Já escrevi {} vezes'.format(r))
