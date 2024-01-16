
#### Para realizar a simples operação de mostrar alguma informação na tela ou capturar uma proveniente do teclado em python, utilizaremos as funções print e input, as usamos assim (respectivamente):

```
print('O que deseja apresentar')
variavel = input('Instruções para o usuario inserir a resposta')
```

## Print
Podemos usar a função `print` de diversas formas, sendo elas:
```
print('com aspas simples') #forma mais indicada seguindo o zen-python
print("com aspas duplas")
```
Dessa forma, mostramos a mensagem entre aspas no terminal. Quando queremos mencionar variaveis, temos algumas formas de concatenar junto a textos:

- com sinal + (pouco utilizado, uma vez que causa confusão ao python caso a variavel armazene dados do tipo numerico);
```
print('mensagem' + variavel + 'mensagem')
```

- utilizamos os argumentos da função print, concatenando através da ",";
```
print('mensagem', variavel, 'mensagem')
```
- podemos também utilizar a 'f-string' uma estrutura de formatação;
```
print(f'mensagem {variavel} mensagem')
```

- ou mesmo, o antigo método, .format(), que está obsoleto e foi substituido pelas f-strings;
```
print('mensagem {} mensagem'.format(variavel))
```

## Input
Para utilizarmos a função `input` é bem simples, apenas criamos uma variavel para armazenar o valor inserido pelo usuário. Da seguinte forma:
```
variavel = input('instrução para o usuário')
```
Essa instrução da-se para o usuário saber que informação inserir. 
\
\
A função input retorna por padrão o tipo string (str()) e quando desejamos um tipo específico de retorno, como um numero, temos que tipificar o retorno utilizando um iterador.

- para um numero inteiro
```
inteiro = int(input('instrução'))
```
- para um valor flutuante
```
real = float(input('instrução'))
```