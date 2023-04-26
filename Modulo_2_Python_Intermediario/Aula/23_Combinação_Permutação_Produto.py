"""
    Combinations, Permutations e Product - Itertools
    Combinação - Ordem não importa - iterável + tamanho do grupo
    Permutação - Ordem importa
    Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n') # Função para facilitar a formatação da exibição
    print()

pessoas = [
    'Victor', 'Marieli', 'Luiz', 'Judite', 
]

camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodão', 'Poliéster']
]

print_iter(combinations(pessoas, 2)) # A classe combinations é usada para combinar os valores sem repetir, ou seja é iterado sobre os valores da lista e combina eles, porém não repete as combinações
print_iter(permutations(pessoas, 2)) # Já a classe permutations também combina os valores, porém ela repete combinações apenas invertendo a ordem, se antes retornou (1,2) o próximo será (2,1)
print_iter(product(*camisetas)) # Product gerá combinação mais complexas entre outra listas ou listas dentro da mesma lista, gerando todas as combinações possíveis