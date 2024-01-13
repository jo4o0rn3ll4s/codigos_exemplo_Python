# Estruturas de controle de fluxo por repetição

## For

A função ```for``` é uma função de repetição por um tempo determinado, realiza tal repetição por meio de uma variável de controle.


Tem sua sintaxe tradicional da seguinte forma: 
```
for variavel_de_controle in range(valor_inicial, valor_final , valor_de_incremento_ou_decremento):
    [...]
    bloco de código a realizar as X vezes especificas definida na condição lógica
    [...]
```

Além da sua sintaxe muito comum para trabalhar com variaveis compostas:
```
for variavel_de_controle in variavel_composta:
    o bloco de código que vai utilizar dos elementos na variavel composta
```

## while

A função ```while``` podemos compreender apenas traduzindo a palavra. A aplicamos quando desejamos fazer um laço de repetição, porém sem limitar previamente, mas sim deixando ela condicionada ao usuário, por exemplo.

Esta é sua sintaxe:

```
while condição_lógica:
    [...]
    bloco de código a realizar enquanto a condição for verdadeira o teste lógico retornar verdade;
    [...]
```

Uma forma muito utilizada do laço `while` é quando posto em `laço infinito`, pondo ,como condição lógica, apenas o valor booleano `True`. Para interromper o laço de repetição, é utilizado a estrutura de decisão `if`, para saber em que situação encerrar o laço, que por sua vez chama a estrutura `break`. Aqui emos um exemplo:
```
while True:

    [...]bloco de código a repetir x vezes[...]

    if condição_lógica:
        break
```