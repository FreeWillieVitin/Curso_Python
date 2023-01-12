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



