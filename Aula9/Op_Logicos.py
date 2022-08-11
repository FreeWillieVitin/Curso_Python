"""
Operadores Lógicos
and, or, not, in, not in
and: é necessario que as duas comparações sejam verdadeiras para retornar true
or: apenas que uma das expressões sejam verdadeiras
not: se nao existir nada dentro de uma variavel ou ela for igual a zero vai retornar true
in: usado para verificar se existe algo dentro de uma variavel
not in: é o contrario do in, ou seja, se nao existir algo dentro da variavel
"""
# Exemplo de AND
nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))

idade_menor = 18
idade_maior = 50

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar um empréstimo')
else:
    print(f'{nome} não pode pegar um empréstimo')

# Exemplo de not
a = 2
b = 3

if not b > a:  # Se b não for maior que a faça alguma coisa
    print('B é maior do que A')
else:
    print('A é maior do que B')

x = ''
y = 0

if not x:
    print('valor vazio')

# Exemplo de in
if 'v' in nome:
    print(f'Existe V no nome {nome}')
else:
    print(f'nao existe a letra v no nome {nome}')

# Exemplo de senha
usuario = input('Login: ')
senha = input('Senha: ')

usu_bd = 'Victor'
senha_bd = 'ChicoBento34'

if usu_bd == usuario and senha_bd == senha:
    print('Você acessou o sistema')
else:
    print('Usuario ou senh incorretos.')




