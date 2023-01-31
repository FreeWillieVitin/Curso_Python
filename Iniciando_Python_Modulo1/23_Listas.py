"""
Listas em Python
É um tipo de dado da mesma forma que int, string, float e bool
que pode conter vários valores dentro de colchetes
Tipo list = Mutável
Suporta vários valores de qualquer tipo.
Indices e Fatiamento
Métodos utéis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um idice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create, Read, Update, Delete = (CRUD)
Criar, Ler, Alterar, Deletar = lista[i] 
"""
# Isto é uma Lista
# indice 0--1--2--3-------4-----------5-----6----------------
lista = [1, 2, 3, 4, 'Victor Hugo', True, 10.5]
listao = [1, 2, 3, 4, 'Victor Hugo', True, 10.5]
string = 'ABCDE'

# Acessar um elemento da lista com indice e alterar o valor de um indice
print(listao[4].upper(), type(lista[4]))
lista[5] = "teste"
print(lista)

# Usar um elemnto da lista como variável atraves do seu indice
var = lista[2]
print(var)

# Deleta um elemento com indice
del lista[2]
print(var)

# Definir um print com range
print(lista[1:4])

# Para acessar os valores de uma lista, usamos os indices
print(lista[5])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Concatenar lista
l3 = l1 + l2
# podemos concatenar listas atraves da função extend que é descrita dessa forma: variavel.extend(varivel a ser juntada)
# ou usar variavel.extend(um valor que queira concatenar ex: uma string qualquer)
l1.extend(l2)

# A função append insere um valor na ultima linha da lista
l2.append('Victor')

# O insert, insere na lista um valor na posição definada no parametro, sintaxe: variavel.insert(indice, valor inserido)
l2.insert(0, "tatata")

# O .pop exclui o ultimo item da lista, da mesma forma que o append insere na ultima linha
print(l2)
l2.insert(2, 'Gorgonzola')
print(l2)
l2.pop()

# Com o .pop também podemos usar o indice para excluir um valor desejado
print(l2)
l2.pop(4)
print(l2)

print(l1)
print(l3)
