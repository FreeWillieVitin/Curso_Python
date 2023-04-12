# List comprehension em python
# List Comprehension é uma forma rápida para criar listas a partir de iteráveis.
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista2 = [numero * 2 for numero in range(10)]
print(lista2)
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 30,},
    {'nome': 'p3', 'preco': 40,},
]
antigo_preco = [produto_antigo for produto_antigo in produtos]
print(*antigo_preco, sep='\n')

print()

novos_produtos = [{**produto, 'preco': produto['preco'] * 2} 
                  if produto['preco'] > 20 else {**produto} for produto in produtos]
print(*novos_produtos, sep='\n')
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Filtro
lista3 = [n for n in range(10) if n < 5]
p(lista3)

novos_produtos2 = [{**produto, 'preco': produto['preco'] * 2} 
                  if produto['preco'] > 20 else {**produto} for produto in produtos
                  if (produto['preco'] > 20)]
print(*novos_produtos2, sep='\n')
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehension com mais de um for

lista4 = []
for x in range(3):
    for y in range(3):
        lista4.append((x, y))

p(lista4)

lista5 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print()
p(lista5)
print()

# Strings
string = 'Victor Hugo'
num_letra = 1
nova_string = '.'.join([
    string[indice:indice + num_letra]
    for indice in range(0, len(string), num_letra)
])
print(nova_string)

nomes = ['victor', ' marieli', ' luiz', 'judite']
novos_nomes = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]
print(novos_nomes)