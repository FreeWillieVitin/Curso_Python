"""
Listas em Python - É um tipo de dado que pode conter vários valores dentro de colchetes
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Podemos criar listas atraves da função range, mas para isso precisa ser adicionado a função de construção list()
l3 = list(range(1, 10, 2))
soma = 0

l4 = ['victor', 1, 1.1, True]

# O uso do del é importante para excluir indices da lista, sintaxe: del(variavel da lista[indice inicial:indice final])
del(l1[3:5])
print(l1)

# Função max e min, pode-se entender como um retorno do maior(max) numero da lista e o menor(min) numero da lista
print(max(l2))
print(min(l2))

for i in l3:
    soma = soma + i
    print(f'{soma} + {i} = {soma}')
print(soma)

for a in l4:
    print(f'O tipo do {a} é {type(a)}')

# Exemplo de joguinho da forca, neste exemplo é usado uma lista para armazenar as letras existentes na palavra secreta
# Abaixo estão definidas as variaveis principais do jogo como a palavra secreta, a varivel para armazenar a lista
# e a variavel da quantidade de chances que o jogador tem.
segredo = input("Digite uma palavra: ")
digitos = []
chance = 3


while True:
    if chance == 0:
        print("Você perdeu!!")
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Letras a mais')
        continue

    digitos.append(letra)
    if letra in segredo:
        print(f'A letra {letra} bate com a secreta')
    else:
        print(f'A letra {letra} não foi encontrada')
        digitos.pop()
    temp = ''
    for l in segredo:
        if l in digitos:
            temp += l
        else:
            temp += '*'

    if temp == segredo:
        print(f'QUe legal, você ganhou!!! A palavra era {temp}')
        break
    else:
        print(f'Até o momento a palavra está assim: {temp}')

    if letra not in segredo:
        chance = chance - 1

    print(f'Você ainda tem {chance} chances')









