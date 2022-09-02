"""
Desempacotamento de listas em Python
Uso do * em uma variável com lista significa que ele vai trazer os resultados restados
"""
lista = ['Victor', 'Marieli', 'Barbrinha', 1, 2, 3, 4, 5]

n1, n2, *outra_lista, ultimo = lista

print(n2, outra_lista, ultimo)
