"""
Uso da função len
"""

usuario = input('Digite seu nome: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Nome muito curto')
else:
    print('Seu nome é grande')

valor1 = input('Digite algo: ')
valor2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados é {len(valor1) + len(valor2)}')
