"""
 Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro
 dicionário.
 Usamos as chaves - {} - ou a classe dict para criar
 dicionários.
 Imutáveis: str, int, float, bool, tuple
 Mutável: dict, list
"""
pessoa = {
    'nome': 'Victor Hugo',
    'sobrenome': 'Jurczyszyn',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
 }
pessoas = dict(nome='Luiz Otávio', sobrenome='Miranda')
print(pessoa['nome'])

for chave in pessoa:
    print(chave)
    print(chave, pessoa[chave])

# # Manipulando chaves e valores em dicionários
p = {}

chave = 'nome'

p[chave] = 'Victor Hugo'
p['Sobrenome'] = 'Jurczyszyn'

print(p[chave])

del p['Sobrenome']
print(p)
print(p['nome'])

print(p.get('sobrenome', 'Não tem Valor'))
if p.get('Sobrenome') is None:
    print('Não existe')
else:
    print(p['Sobrenome'])

"""
    Métodos úteis dos dicionários em Python
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    items - iterável com chaves e valores
    setdefault - adiciona valor se a chave não existe
    copy - retorna uma cópia rasa (shallow copy)
    get - obtém uma chave
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último item adicionado
    update - Atualiza um dicionário com outro
"""
print(len(pessoa))

print(list(pessoa.keys()))
print(tuple(pessoa.keys()))
for chave in pessoa.keys():
    print(chave)

print(list(pessoa.values()))
print(tuple(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print(list(pessoa.items()))
print(tuple(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

print(pessoa.get('Carro', 'Não tem Valor'))

pessoa.setdefault('Planeta', 'Nenhum')
for chave, valor in pessoa.items():
    print(chave, valor)