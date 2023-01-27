"""
Condicionais IF, ELIF e ELSE
if = se
elif (else if) = senão se
else = senão
Hierarquia = Identação(Espaços entre as linhas para identificar de quem cada codigo pertence)
"""
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não quer nada da vida')


if False:
    print('Verdadeiro.')
elif True:
    print('Agora é verdadeiro.')
elif True:
    print('Outro bloco')
else:
    print('Expressão não é verdadeira.')
