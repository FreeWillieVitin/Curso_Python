"""
While / Else
Contadores - conta de forma linear
Acumuladores - a cada volta do laço ele vai acumulando a variável
else - else só vai ser executado quando for interpretado que é falso, caso contrario o laço continuará
"""
# Abaixo um exemplo de laço contador, para usar o while é necessário que haja uma variável que possa ser contada
contador = 0

while contador <= 100:
    print(contador)
    contador += 1

# Exemplo de um laço acumulador, basicamente soma uma variável com a outra e vai realizando laço até seu fim
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else:
    print('Acabou!')
# Else dnv
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Acabou!')
print('Acabou sem chegar no else!')

""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
