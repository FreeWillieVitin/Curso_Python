"""
groupby - agrupando valores(itertools)
"""
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])

for aluno in alunos_agrupados:
    print(aluno)

# grupos1 = groupby(alunos)

# for chave, grupo in grupos1:
#     print(chave)
#     print(list(grupo))

print()
letras = ['a','a','a','a', 'b', 'c','a']
grupos2 = groupby(sorted(letras))

for chave, grupo in grupos2:
    print(chave)
    print(list(grupo))