#COM UMA VARIAVEL A PARTIR DO USUARIO
i = 1

resp = 's'
while resp != 'n':
    print(i)
    i += 1
    resp = input('Deseja executar novamente s/n: ')


#COM UM VALOR FIXO DE REPETICOES
i=0
while i < 10:
    print(i)
    i+=1


#COM UMA INTERRRUPCAO BREAK
while True:
    if input('s|n') == 'n':
        break
    else
        print('outro loop')
