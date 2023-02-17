"""
Operador ternario em Python
Forma de reduzir codigos
<valor> if <condicao> else <outro valor>
"""
# Aqui temos uma condicional padrão, se for verdadeiro exibe a primeira condição, senão a segunda (nada de novo).
logged = True

if logged:
    msg = 'Usuário logado'
else:
    msg = 'Usuário não logado'

print(msg)

# Aqui temos um operador ternário, que faz exatamente a mesma coisa que acima, porém poupando linhas de código
# e deixando tudo mais organizado
user = True
msg = 'Usuário logado' if user else 'Usuário não logado'
print(msg)

"""
Um exemplo mais completo, usando condição padrão e operador ternário
"""
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
