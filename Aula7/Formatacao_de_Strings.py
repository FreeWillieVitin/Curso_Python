"""
Formatação de strings
uso do f para formatar textos
:.2f - Essa função é usada pra encurtar casa decimais, o 2 descrito na função pode ser trocado por qualquer numero
que deseja ser usado, ele significa a quantidade de casas decimais que vai conter no valor
.format() define uma ordem para usar as variaveis em uma string
"""
nome = 'Victor'
idade = 24
altura = 1.74
e_maior = idade > 18
peso = 82
imc = (peso / (altura ** 2))
print(nome, 'você tem', idade, 'e seu imc é', imc)  # Sem a formatação
print(f'{nome} voce tem {idade} e seu IMC é {imc:.2f}')  # Com a formatação
print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc))



