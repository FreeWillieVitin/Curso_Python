"""
* Enumerate - Enumerar elementos da lista #list
"""
lista =[
        # 0       # 1       # 2
    ['victor', 'marieli', 'luiz'],  # 0
    ['judite', 'dayane', 'lolo'],   # 1     # Uma lista dentro de uma lista
    ['carla', 'antonio', 'maria']   # 2
]
conta = list(enumerate(lista))  # Variável que salva a lista para enumeração, para isso é necessário usar o construtor
# list que transforma a variável em uma lista
print(conta)
print(lista[2][1])  # print com index da lista, indica que retornará a terceira linha da lista e a segunda coluna
print(conta[1][1][2])  # Como temos uma lista dentro de outra é preciso identificar ela quando for selecionar para que
# o sistema saiba qual você esta buscando por isso os parâmetros são desta forma [coluna],[qual lista], [valor da lista]

for v1 in enumerate(lista):
    valor, lili = v1
    nome1, nome2, nome3 = lili
    print(v1)
    print(nome1, nome2,nome3)


