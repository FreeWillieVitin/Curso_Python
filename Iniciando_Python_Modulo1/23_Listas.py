"""
Listas em Python
É um tipo de dado da mesma forma que int, string, float e bool
que pode conter vários valores dentro de colchetes
Tipo list = Mutável
Suporta vários valores de qualquer tipo.
Indices e Fatiamento
Métodos utéis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um idice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create, Read, Update, Delete = (CRUD)
Criar, Ler, Alterar, Deletar = lista[i] 
"""
# Isto é uma Lista
# indice 0--1--2--3-------4-----------5-----6----------------
lista = [1, 2, 3, 4, 'Victor Hugo', True, 10.5]
listao = [1, 2, 3, 4, 'Victor Hugo', True, 10.5]
string = 'ABCDE'

# Acessar um elemento da lista com indice e alterar o valor de um indice
print(listao[4].upper(), type(lista[4]))
lista[5] = "teste"
print(lista)

# Usar um elemnto da lista como variável atraves do seu indice
var = lista[2]
print(var)

# Deleta um elemento com indice
del lista[2]
print(var)

# Definir um print com range
print(lista[1:4])

# Para acessar os valores de uma lista, usamos os indices
print(lista[5])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Concatenar lista
l3 = l1 + l2

# podemos concatenar listas atraves da função extend que é descrita dessa forma: variavel.extend(varivel a ser juntada)
# ou usar variavel.extend(um valor que queira concatenar ex: uma string qualquer), diferente do sinal de +, o extend aplica a ação diretamente na variavel
# não sendo necessaria a craição e outra variavel para a concatenação, pois o metodo extend é do tipo None e não retornaria nada
l1.extend(l2)

# A função append insere um valor na ultima linha da lista
l2.append('Victor')

# O insert, insere na lista um valor na posição definada no parametro, sintaxe: variavel.insert(indice, valor inserido)
l2.insert(0, "tatata")

# O .pop exclui o ultimo item da lista, da mesma forma que o append insere na ultima linha
print(l2)
l2.insert(2, 'Gorgonzola')
print(l2)
l2.pop()

# Com o .pop também podemos usar o indice para excluir um valor desejado
print(l2)
l2.pop(4)
print(l2)

print(l1)
print(l3)

"""
Cuidados com dados mutáveis
= - (imutáveis)
Os objetos do tipo int, float, string, bool sao imutaveis. Isto
significa que objetos deste tipo nao podem ter seus valores alterados.
Cada objeto criado esta em uma posicao de memoria e possui um
identificador unico que pode ser obtido com a funcao id()

= (imutáveis)
"""
# Exemplo de dado imutável
# A variavel a está associada com o objeto int de valor 94, que possui o identificador 2399522393232
a = 94
id(a) # 2399522393232

# Como um int e imutavel quando fazemos o incremento da variavel a, o que ocorre na verdade e a criacao de um novo objeto do tipo int que sera associado com a.

a += 1
a
id(a) # 1446056889520, percebemos que mesmo a variavel sendo a mesma, por ter um valor diferente o seu id é alterado, não podendo ser atribuido o mesmo id que o anterior

# Objetos do tipo list sao mutaveis (veremos outros tipos mutaveis posteriormente no curso). Isto significa que objetos deste tipo podem ter seus valores alterados.

b = []
id(b) # 2270716744448

b.append(1)
b
id(b) # 2270716744448

b += [2]
b
id(b) # 2270716744448

b = [1,2]
id(b) # 2270717295488

# No exemplo acima note que a variavel b fica associada com a mesma lista de identificador 2270716744448, exceto na ultima atribuicao.
# Na ultima atribuicao é criada uma nova lista e esta é associada com b.

"""
for in com listas - Da mesma forma que podemos iterar uma strig
podemos iterar uma lista tambem usando o for in
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4 = ['victor', 1, 1.1, True]
soma = 0
lista = ['Victor', 'Marieli', 'Jorge']

for nome in lista:
    print(nome, type(nome))

for i in l2:
    soma = soma + i
    print(f'{soma} + {i} = {soma}')
print(soma)

for a in l4:
    print(f'O tipo do {a} é {type(a)}')

"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

exercicio = ['Maria', 'Helena', 'Luiz'] # Lista com os nomes

for num in range(0,3): # Armazena em uma variavel um range
    print(num, exercicio[num]) # Usa o range passado na variavel num como indice para os itens da lista
