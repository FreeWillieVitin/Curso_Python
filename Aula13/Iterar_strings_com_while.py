frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_string = ''
#digit = input('Digite uma letra: ')
while contador < tamanho:
    letra = frase[contador]
    #if letra == digit:
     #   nova_string += digit.upper()
    #else:
     #   nova_string += letra
    # print(frase.upper()[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
print(nova_string)
