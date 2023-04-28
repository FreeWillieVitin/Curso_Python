"""
groupby - agrupando valores(itertools)

Para um agrupamento acontecer eles devem estar ordenados. Ex: a,a,a,b,a (Por estar fora da ordem o ultimo a não seria agrupado com o restante)
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
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos1 = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos1:
    print(chave)
    for a in grupo:
        print(a)

print()
letras = ['a','a','a','a', 'b', 'c','a']
grupos2 = groupby(sorted(letras))

for chave, grupo in grupos2:
    print(chave)
    print(list(grupo))