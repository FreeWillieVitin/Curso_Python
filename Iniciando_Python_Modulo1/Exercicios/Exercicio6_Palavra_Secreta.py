"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra = input('Digite uma palavra secreta: ')
tentativa = 0
resposta = ''

while True:
    if tentativa >= 5:
        print('Você perdeu!!')
        break

    letra = input('Digite uma letra: ')
    temp = ''

    if len(letra) > 1:
        tentativa += 1
        print('Você Digitou mais de uma letra')
        print(f'Você ja errou {tentativa} vezes')
        continue
    
    if letra in palavra:
        print(f'A letra {letra} bate com a palavra secreta')
    else:
        print(f'A letra {letra} não está na palavra secreta')

    if letra in palavra:
        resposta += letra
    else:
        tentativa += 1

    for l in palavra:
        if l in resposta:
            temp += l
        else:
            temp = temp + '*'

    if temp == palavra:
        print('Parabens você venceu')
        break

    print(temp)
    print(f'Você ja errou {tentativa} vezes')
    

        

