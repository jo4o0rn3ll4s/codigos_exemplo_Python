# Variaveis Compostas

## Turpla

A estrutura `tuple` é uma espécie de vetor que possui como característica marcante o ser imutável, ou seja, não é possível alterar seus valores em nenhum momento do programa.

Tem sua sintaxe de criação da seguinte forma:
```
val = ('val0','val1'...)
val = tuple(('val0','val1'...))
```
E possui os seguintes métodos para:

* retornar o número de vezes que o elemento aparece na tupla
`val.count(valor)`

* retornar o índice do elemento pesquisado
`val.index(valor)`

## Lista

A estrutura `list` é uma espécie de vetor, similar à tupla, porém, aceita as modificações dos valores presentes. Como inserir, pesquisar, ordenar e excluir.

Tem sua sintaxe de criação da seguinte forma:
```
val = ['val0','val1'...]
val = list(('val0','val1'...))
```

E conta com os seguintes métodos para:
* adicionar um valor ao final da lista ou em um índice específico

`val.append(valor)`

`val.insert(indice, valor)`

* ordenar a lista em ordem alfanumérica

`val.sort()`

* retirar um valor do índice específico ou pelo próprio valor

`val.pop(indice)`

`val.remove(valor)`


## Dicionario

A estrutura `dict` é uma estrutura de variável conhecida também por tabela hash. Ao invés de mencionarmos os valores através de um índice, mencionamos por um apelido.

Tem sua sintaxe de criação da seguinte forma: 
```
val = {'val0':'valor0','val1':'valor1'...}
val = dict(val0 = 'valor0',val1 = 'valor1'...)
```
E possui os seguintes métodos para:

* retornar os valores do dicionário
`val.values()`

* retornar as keys do dicionário
`val.keys()`

* retornar os itens do dicionário
`val.items()`

* retornar o valor pesquisado, caso não haja tal chave, o item é adicionado ao dicionário
`val.setdefault('key','valor')`

* adicionar um item ao dicionário
`val.update('item')`

* retirar um item por sua chave
`val.pop('key')`

* retirar o ultimo item adicionado ao dicionário
`val.popitem()`

Sem sombra de dúvidas, a estrutura mais complexa é o dicionário, porém, é de longe a estrutura mais versátil para utilizar uma vez que, ao trabalhar com estruturas `JSON`, tratamo-las como dicionários.
