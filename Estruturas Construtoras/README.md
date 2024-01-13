# Estruturas construtoras

## DEF

A estrutura `def` remete a palavra define, que em tradução direta significa definir. Serve para assim, criar funções próprias, de maneira a desenvolver códigos mais complexos de maneira mais simples. Tradicionalmente nomes de funções começam com letras minusculas.

Tem sua sintaxe tradicional da seguinte forma: 
```
def nome_da_função(argumento1, argumento2):
    [...]
    bloco de código a ser realizado caso a função seja chamada
    [...]
    return valor_retornado
```

### Variações da estrutura def

- Com argumento opcionais

    Para realizar a declaração de uma função com argumentos opcionais, precisamos primeiro declara-lá e inicializa-lá, passando um valor para que, caso na hora de chamar a função, não tenha sido posto um valor para esse argumento, exista um valor "padrão".

    Tem sua sintaxe da seguinte forma:
```
def nome_da_função(argumento1 = valor_padrão1, argumento2 = valor_padrão2):
    [...]
    bloco de código a ser realizado caso a função seja chamada
    [...]
    return valor_retornado
```

- Com inumeros argumentos

    Para realizar a declaração de uma função com inumeros argumentos, precisamos primeiro declara-lá, porém, marcando-a com o sinal '*', que passa para o computador a instrução de 'compactar' todos os argumentos que vierem em uma lista. Para acessar tais arguementos posteriormente, utilizamos da função for para descompactar, elemento por elemento, cada um dos argumentos passados.
    
```
def nome_da_função(*argumentos):
    [...]
    bloco de código a ser realizado caso a função seja chamada
    [...]
    return valor_retornado
```

## CLASS

A estrutura `class` remete a palavra classe. Classes e objetos são partes de uma área da programação chamada POO -programação orientada a objetos- sendo esse um assunto considerado complexo. Tradicionalmente, nomes de classes começam com letras maiusculas.

Tem sua sintaxe tradicional da seguinte forma: 
```
class NomeDaClasse:
    def __init__(self, arguementos):
        self.argumentos = arguementos

    def nome_do_metodo(self, argumento):
        [...]
        bloco de código a ser realizado com o objeto caso seja implicado tal método
        [...]
```

Classes por si, tendem a simplificar programas por conseguir 'generalizar' e agrupar um conjunto de informações, moldando assim um 'objeto'. Objeto esse totalmente funcional, com propriedadedes e usos, chamados métodos, que podem (ou não) alterar as proprias propriedades.


### Atenção
 * Para melhor entendimento e vizualização, todos os exemplos de funções estão apresentados de maneira completa, entretanto, nem toda função terá argumento, ou retorno, podendo assim haver alterações. Para saber como utilizar cada função (não escrita por você) recomendo ler as 'doc_strings': Um conjunto de informações descritas nas funções distribuidas por módulos a fim de explicar suas particularidades e instruir de que maneira utiliza-lá.

