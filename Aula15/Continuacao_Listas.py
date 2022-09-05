"""
Listas em Python - É um tipo de dado que pode conter vários valores dentro de colchetes
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Podemos criar listas atraves da função range, mas para isso precisa ser adicionado a função de construção list()
l3 = list(range(1, 10, 2))
soma = 0

l4 = ['victor', 1, 1.1, True]

# O uso do del é importante para excluir indices da lista, sintaxe: del(variavel da lista[indice inicial:indice final])
del(l1[3:5])
print(l1)

# Função max e min, pode-se entender como um retorno do maior(max) numero da lista e o menor(min) numero da lista
print(max(l2))
print(min(l2))

for i in l2:
    soma = soma + i
    print(f'{soma} + {i} = {soma}')
print(soma)

for a in l4:
    print(f'O tipo do {a} é {type(a)}')









