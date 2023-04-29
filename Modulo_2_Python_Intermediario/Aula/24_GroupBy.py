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
def ordena(aluno): # Função que irá receber uma lista como argumento
    return aluno['nota'] # Quando for passada a lista, a função vai retornar o item nota que estiver no dicionario dentro da lista

alunos_agrupados = sorted(alunos, key=ordena) # Variável que ordena a os itens especificados na função que estão dentro do dicionario que está dentro da lista passada de argumento
grupos1 = groupby(alunos_agrupados, key=ordena) # Após a organização usamos o groupby, para agrupar em uma tupla todos os alunos com a mesma nota
print(grupos1)
print()
for chave, grupo in grupos1: # Agora vamos iterar sobre o agrupamento, groupby é uma função iteravel então precisamos disso para que o resultado seja retornado
    print(chave) # Exibimos a variável chace que retorna a apenas a nota iterada
    for a in grupo: # Então iteramos sobre a segunda variável para receber o resto do dicionario
        print(a) # Abaixo da exibição da nota, teremos a lista de alunos que pertencem a respectiva nota, todos agrupados
"""
Abaixo temos um exemplo mais simples de como funciona o groupby
"""
print()
letras = ['a','a','a','a', 'b', 'c','a'] # Temos uma lista com quase todos os valores ordenados o que ja seria possivel de agrupar
grupos2 = groupby(sorted(letras)) # ordenamos com o sorted para posicionar o valor a com os outros

for chave, grupo in grupos2: # Então iteramos e temos todos os valores da lista agrupados
    print(chave)
    print(list(grupo))