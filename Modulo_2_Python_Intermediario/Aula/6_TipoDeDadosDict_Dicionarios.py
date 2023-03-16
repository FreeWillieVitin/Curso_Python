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
pessoa = { # Está é a forma de criar um dicionario, o primeiro valor é chamado de chavee o seguinte é o valor, separado por :
    'nome': 'Victor Hugo',
    'sobrenome': 'Jurczyszyn',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}, # Podemos incluir outros dicionarios dentro de um dicionario
    ]
 }
pessoas = dict(nome='Luiz Otávio', sobrenome='Miranda') # Outra forma de estrutura de criação de dicionarios, informando a classe dict
print(pessoa['nome']) # print exibindo apenas uma chave do dicionario

for chave in pessoa: # Tambem podemos iterar sobre um dicionario
    print(chave)
    print(chave, pessoa[chave])

# # Manipulando chaves e valores em dicionários
p = {} # Aqui temos um dicionario sem valores algum

chave = 'nome' # Variável recebendo o valor nome

p[chave] = 'Victor Hugo' # Ao inserir a variavel mencionada dentro de colchetes referenciando o dicionario seguida por um valor, inserimos uma chave dentro do dicionartio vazio
p['Sobrenome'] = 'Jurczyszyn' # Faz exatamente a mesma coisa que acima, mostrando que não precisamos obritariamente inserir uma variavel dinamicamente

print(p[chave]) # Exibe apenas a chave e o valor de nome

del p['Sobrenome'] # Deleta a chave descrita do dicionario
print(p)
print(p['nome'])

print(p.get('sobrenome', 'Não tem Valor')) # O metodo get faz uma busca da chave desejada no dicionario, caso não encontre ele retorna um valor padrão de tipo None
if p.get('Sobrenome') is None: # Aqui fazemos a checagem se a chave é none, ou seja sem valor algum
    print('Não existe') # Se ela não for encontrada e for definida como None, então damos um retorno padrão
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
print(len(pessoa)) # Conta quantas chaves existem no dicionaro

print(list(pessoa.keys())) # retorna em um tipo lista todas as chaves do dicionario
print(tuple(pessoa.keys())) # retorna em um tipo tuple todas as chaves do dicionario
for chave in pessoa.keys(): # itera soomente sobre as chaves
    print(chave)

print(list(pessoa.values())) # retorna em um tipo lista todas os valores do dicionario
print(tuple(pessoa.values())) # retorna em um tipo tuple todas os valores do dicionario
for valor in pessoa.values(): # itera somente sobre os valores
    print(valor)

print(list(pessoa.items())) # retorna em um tipo lista os items do dicionario que são as chaves e os valores juntos
print(tuple(pessoa.items())) # retorna em um tipo tuple os items do dicionario que são as chaves e os valores juntos
for chave, valor in pessoa.items(): # itera sobre os itens, mosntrado de forma mais compreensivel os dados
    print(chave, valor)

print(pessoa.get('Carro', 'Não tem Valor'))

pessoa.setdefault('Planeta', 'Nenhum') # Para evitar erro, podemos tratar a falta de uma chave dando um valor padrão a ela
for chave, valor in pessoa.items():
    print(chave, valor)

nome = pessoa.pop('nome') # Apaga uma chave definida como parametro
print(nome)
print(pessoa)    

sobrenome = pessoa.popitem() # Apaga a ultima chave do dicionario
print(sobrenome)
print(pessoa) 

pessoa.update({  # Atualiza valores ou qualquer dado do dicionario
    'nome': 'Marieli',
    'idade': '24'
})

"""
Shallow Copy e Deep Copy
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
