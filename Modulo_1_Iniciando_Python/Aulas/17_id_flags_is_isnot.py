"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, quantidade)
id = Identidade
"""
"""
Os algoritmos abaixo mostram uma checagem se uma linha de codigo foi acessada ou não atraves de um tipo de checkpoint
onde o valor de uma variavel que no momento esta como tipo none (sem valor), ao encontrar uma condição que atribui
valor a ela é checada em seguida informando se aquela variável recebeu ou não um valor
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
