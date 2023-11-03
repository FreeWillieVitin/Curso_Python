# frase = 'o rato roeu a roupa do rei de roma'
# tamanho = len(frase)
# contador = 0
# nova_string = ''
# #digit = input('Digite uma letra: ')
# while contador < tamanho:
#     letra = frase[contador]
#     #if letra == digit:
#      #   nova_string += digit.upper()
#     #else:
#      #   nova_string += letra
#     # print(frase.upper()[contador], contador)
#     nova_string += frase[contador]
#     print(nova_string)
#     contador += 1
# print(nova_string)

# Exercicio - Quantas vezes a letra aparece na frase

frase = 'Eu tenho um carro, mas ele explodiu e tudo foi para os ares, nao sobrando nada' \
    'nem mesmo um fio de cabelo da careca do meu pai'
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
