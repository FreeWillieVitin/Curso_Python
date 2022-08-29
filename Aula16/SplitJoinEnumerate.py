"""
Funções Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta e é tbm muito lindo.'
lista = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0

for i in lista:
    print(f'A palavra {i} aparece {lista.count(i)}x na frase.')

for x in lista:
    qtd_vezes = lista.count(x)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = x

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

print(lista2)
