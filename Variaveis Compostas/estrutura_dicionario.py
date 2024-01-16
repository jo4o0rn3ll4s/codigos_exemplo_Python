#crio um dicionario chamado ficha, com informações nome e idade
ficha = dict(nome= 'João', idade= 20)

#pesquiso por nome. caso não haja ponho como Juan
print(ficha.setdefault('nome', 'Juan'))
#pesquiso por habilitação, caso não haja ponho AB. Como não há, é adicionado a ficha
print(ficha.setdefault('habilitação', 'AB'))

#mostro os valores de chave, que são os nomes de indice
print(ficha.keys())
#mostra os valores dentro do dicionario
print(ficha.values())

#Faz a adição da chave e valor estado civil, solteiro a ficha
ficha.update({'estado civil':'solteiro'})
print(ficha)

#removo o item com chave, habilitação
ficha.pop('habilitação')
print(ficha)
