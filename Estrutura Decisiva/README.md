# Estruturas de controle de fluxo por decisão

## IF...ELIF...ELSE

A função ```IF``` é uma função de decisão que faz com que um conjunto de instruções sejam ou não realizados. Traduzindo ao pé da letra, entendemos como a função 'se'

Tem sua sintaxe tradicional da seguinte forma: 
```
if condição_lógica:
    [...]
    bloco de código a realizar caso a condição lógica retorne True
    [...]
```

Além da sua sintaxe de um teste 'se', podemos construir estruturas complexas acrescentando respostas `elif` (senão se) [que podem ser inumeros] e `else` (senão).

Tem sua sintaxe da seguinte forma:
```
if condição_lógica:
    [...]
    bloco de código a realizar caso a condição lógica retorne True
    [...]
elif condição_lógica:
    [...]
    bloco de código a realizar caso a condição lógica do if retorne False e do elif retorne True
    [...]
else:
    [...]
    bloco de código a realizar caso todas as condições lógicas anteriores retorne false
    [...]
```

### Versão "linear" do if

Podemos também criar condições para determinadas ações de forma linear. Como mostra o exemplo a seguir:
```
variavel = valor_a if condição_lógica else valor_b
```
Tal estrutura é muito pratica e minimiza a quantidade de linhas em programas mais complexos.