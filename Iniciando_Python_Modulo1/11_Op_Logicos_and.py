"""
Operador and em Python
and, or, not, in, not in

and: é necessario que as duas comparações sejam verdadeiras para retornar true
se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
São considerados falsy 0, 0.0, '', False.
Tambem existe o tipo None que é usado para representar um não valor

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

# Exemplo de senha
usuario = input('Login: ')
senha = input('Senha: ')

usu_bd = 'Victor'
senha_bd = 'ChicoBento34'

if usu_bd == usuario and senha_bd == senha:
    print('Você acessou o sistema')
else:
    print('Usuario ou senh incorretos.')




