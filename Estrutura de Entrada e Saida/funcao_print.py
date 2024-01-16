print("Esta são maneiras de realizar a apresentação de mensagens na tela")
print('Indifere a utilização de aspas duplas ou simples, seguindo o zen-python, utilizarei mais as aspas simples')
print('''
Podemos utilizar tambem uma sequencia de 3 aspas.
Podem ser simples ou duplas, assim, temos um print que posiciona a mensagem da forma identica a que está sendo escrito

Por exemplo:
    -esta mensagem mesmo está aparecendo igualmente a como está no código
    -observe também que cada detalhe como o pular de linha ou sinais graficos estão identicos
''')
 
 mensagem = 'esta mensagem aqui'

 print(f'Podemos utilizar tambem a marcação "f" antes das aspas para utiliar o que chamamos de f-strings, dessa maneira, concatenamos {mensagem}, aqui dentro do print')
 
 '''
 Forma obsoleta, mas ainda funcional:
    print('Aquela mensagem, agora está {}'.format(mensagem))
 '''