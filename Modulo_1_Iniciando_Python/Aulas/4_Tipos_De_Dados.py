"""
Tipos de dados
str - string - textos 'isso é um texto' "isso tbm é um texto 1234"
int - inteiro - 123456789 0 -10 -20 -50 -60 -15000
float - real/ponto flutuante - números com ponto 1.50 3.00
bool - booleano/lógico - true/false

Extra-------------
Atalho para comentar várias linhas ao mesmo tempo
ctrl + ;

Tudo em python é um objeto
"""

from math import isclose
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

"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
Existem casos que calculos com numeros flutuantes não retornam o valor de forma precisa, então nesses raros casos
temos algumas formas de corrigir estas imprecisões
"""

num1 = 0.1
num2 = 0.7
num3 = num1 + num2

# A soma deste valor retorna um número de valor impreciso = 0.7999999999999999, quando obviamente deveria retornar 0.80
print(num3)

# Ao tratar com a formatação f, o problema de imprecisão é corrigido e o resultado da operação torna-se = 0.80
print(f'{num3:.2f}')

# Outra forma de tratar esse erro é usando a função round, porém com essa função o numero será totalmente arredondado e nessa
# caso retorna = 0.8
print(round(num3, ndigits=1))

print(isclose(0.1 + 0.7, 1.5, abs_tol=0.8))
