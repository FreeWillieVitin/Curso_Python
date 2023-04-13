# isistance - Para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}
]
"""
A Função isinstance() é usada como uma forma de checar se um item tem o tipo correto para executar uma ação, como podemos ter listas com tipos de dados diferentes mesmo não sendo recomendado
então quando precisamos executar algum método que é específico de um tipo que está presente em uma lista com vários outros tipos, usamos o isistance(uma váriavel com o iteravel da lista, tipo do dado)
"""
for item in lista:
    if isinstance(item, set): # Aqui por exemplo pegamos o tipo de dado set que está presente na lista com o valor 0,1 e queremos adicionar mais um valor nesse set, para isso iremos a lista
        print() # E usando o isistance() indicamos ao interpretador que queremos apenas os itens que forem do tipo set, dessa forma o python automaticamente reconhece que para o tipo set
        print('SET') # Temos o método .add() permitindo assim usa-lo e alterar apenas aquele tipo da lista
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print()
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print()
        print('NUM')
        print(item, item * 2)
    else:
        print()
        print('OUTRO')
        print(item)