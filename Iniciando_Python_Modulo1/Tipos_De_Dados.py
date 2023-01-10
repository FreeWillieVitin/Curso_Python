"""
Tipos de dados
str - string - textos 'isso é um texto' "isso tbm é um texto 1234"
int - inteiro - 123456789 0 -10 -20 -50 -60 -15000
float - real/ponto flutuante - números com ponto 1.50 3.00
bool - booleano/lógico - true/false

Extra-------------
Atalho para comentar várias linhas ao mesmo tempo
ctrl + /
"""

print('Victor', type('Victor'))  # type mostra o tipo de dado da classe.
print(-10, type(-10))
print(20.50, type(20.50))
print(10 == 10, type(10 == 10))

"""
Converter tipos
"""
print('Victor', type('Victor'), bool('Victor'))
print('10', type('10'), type(int('10')))

print('Nome: Victor', type('Victor'))
print('Sua Idade: ', 24, type(24))
print('Sua Altura: ', 1.74, type(1.74))
print(24 > 18, type(24 > 18))
