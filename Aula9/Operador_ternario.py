"""
Operador ternario em Python
Forma de reduzir codigos
"""

logged = True

if logged:
    msg = 'Usuário logado'
else:
    msg = 'Usuário não logado'

print(msg)

user = True
msg = 'Usuário logado' if user else 'Usuário não logado'
print(msg)

idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Valor não aceito')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    proibido = 'Pode acessar' if e_maior else 'Você é de menor'
    print(proibido)

if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar')
