"""
Listas em Python - É um tipo de dado que pode conter vários valores dentro de colchetes
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# Isto é uma Lista
lista = [1, 2, 3, 4, 'Victor Hugo', True, 10.5]

# Alterar um indice
lista[5] = "teste"

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

print(l1)
print(l2)
print(l3)
