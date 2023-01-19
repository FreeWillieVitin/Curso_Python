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

# f-strings
print(nome, 'você tem', idade, 'e seu imc é', imc)  # Sem a formatação
print(f'{nome} voce tem {idade} e seu IMC é {imc:.2f}')  # Com a formatação

"""
Formatar valores string com modificadores.

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:valor(x ou X) - Número Hexadecimal
:.(NÚMERO DE CASAS DECIMAIS)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

:= - Força o número a aparecer antes dos zeros
Sinal - :+ ou :- Mostra o sinal na frente do numero conforme o seu sinal (positivo ou negativo)
Ex.: 0>-100,.1f

> - Esquerda
< - Direita
^ - Centro

Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}') # Retorna o valor da variavel
print(f'{variavel: >10}') # Retorna a variavel com 10 strings vazias a esquerda
print(f'{variavel: <10}.') # Retorna a variavel com 10 strings vazias a direita
print(f'{variavel: ^10}.') # Retona a variavel entre strings vazias
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}') # Retorna a forma hexadecimal com 8 caracteres maiusculos
print(f'{variavel!r}')

num1 = 10
num2 = 3
div = num1 / num2
print('{:.2f}'.format(div))
print(f'{div:.2f}')

nome = 'Victor Hugo'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 1150
print(f'{num_3:0^10}')

#  Uso de indices
nome = 'victor'
nome = nome.ljust(20,'#')  # Retorna 20 caracteres justificados a esquerda da palavra
sobrenome = 'Hugo'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)  # adiciona caracteres as strings
print(nome_formatado)
print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo Maiusculo
print(nome.title())  # As primeiras letras maiusculas

# função format
"""
Usando a função .format podemos formatar as strings de 3 formas
através da ordem das variaveis em posição com as chaves, usando indices
que numeram as chaves e nomeando as variaveis forma chamada de parametros nomeados
"""
a = 'A'
b = 'B'
c = 1.1
string = 'a={}, b={}, c={}' # Nesta forma retorna os valores conforme o posicionamento da variavel em relação a chave
formato = string.format(a, b, c) # Ao trabalhar com esse tipo de formatação não podemos repetir valores a não ser que seja repetida a variavel
indice = 'a={0}, b={1}, c={2}' # Nesta forma trabalhamos com numeração dos campos, cada variavel representa um indice iniciado em 0
formato_2 = indice.format(a, b, c) # Então podemos apenas numerar as chaves, conforme a ordem das variaveis podendo repetir os indices
param = 'a={val1}, b={val2}, c={val3}' # E por ultimo temos os parametros nomeados que nada mais é do que nomear as variaveis
formato_3= param.format(val1=a, val2=b, val3=c) # Assim inserimos nas chaves os nomes dados para identificar cada variavel

print(formato)
print(formato_2)
print(formato_3)

print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc))

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Victor'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexidecimal de %d é %x' % (15,15))


