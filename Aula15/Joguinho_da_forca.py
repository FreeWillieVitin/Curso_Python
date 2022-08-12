# Exemplo de joguinho da forca, neste exemplo é usado uma lista para armazenar as letras existentes na palavra secreta
# Abaixo estão definidas as variáveis principais do jogo como a palavra secreta, a variável para armazenar a lista
# e a variável da quantidade de chances que o jogador tem.
segredo = input("Digite uma palavra: ")
digitos = []
chance = 3


while True:
    if chance == 0:  # Se o jogador errar 3 vezes e a variável chance chegar a 0 ele perde e encerra o jogo
        print(f"Você perdeu!!, A palavra era {segredo}")  # Mostra mensagem da derrota e qual era a palavra correta
        break

    letra = input('Digite uma letra: ')  # Define a variável que vai pedir a tentativa de letra ao jogador
    if len(letra) > 1:  # Se o jogador digitar 2 ou mais letra, é checado a quantidade de letras e invalidada a jogada
        chance = chance - 1  # Desconta uma chance do jogador
        print(f'Letras a mais, voce perdeu uma chance, agora você tem {chance} chances')  # mostra as chances restantes
        continue

    digitos.append(letra)  # Insere a letra digita na lista com a variável de nome digitos
    if letra in segredo:  # Inicia um laço que verifica se a letra digitada estiver na palavra segredo
        print(f'A letra {letra} bate com a secreta')  # Se sim, mostra essa mensagem ao jogador
    else:  # Se não
        print(f'A letra {letra} não foi encontrada')  # Mostra essa mensagem
        digitos.pop()  # E exclui o ultimo valor inserido na lista que no caso é a letra errada

    temp = ''  # Variável para armazenar a palavra segredo temporariamente
    for l in segredo:  # Define a variável l e inicia um laço na variável segredo
        if l in digitos:
            temp = temp + l  # Se o valor da variável l for igual a letra da variável digito então ele une os dois
        else:
            temp = temp + '*'  # Se a letra nao for igual então recebe o *

    if temp == segredo:  # Verifica se a variável temp armazena a mesma palavra que a secreta, após as tentativas
        print(f'QUe legal, você ganhou!!! A palavra era {temp}')  # Se o jogador acertou as letras, então parabéns
        break
    else:
        print(f'Até o momento a palavra está assim: {temp}')  # Se não forem iguais então o jogo continua e mostra o
                                                              # andamento do jogo

    if letra not in segredo:  # Se a letra escolhida não estiver na palavra segredo, então tirar uma chance do jogador
        chance = chance - 1
    print(f'Você ainda tem {chance} chances')
