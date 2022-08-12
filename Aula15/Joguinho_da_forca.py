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
