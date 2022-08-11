"""
Operadores Relacionais
== : se usar um sinal de igual quer que um valor é igual ao outro e se usar 2 quer saber se ele é igual
> : Maior que, verifica se um valor é maior que o outro
>= : Maior ou igual a, verifica se o primeiro valor é maior ou igual ao segundo
< : Menor que
<= : Menor ou igual a
!= : Diferente
"""
num1 = 2  # INT
num2 = '2'  # String
num3 = 2  # INT
num4 = 4  # INT
expressao = num1 == num3
expressao1 = num1 > num3
expressao2 = num1 >= num4
expressao3 = num1 < num4
expressao4 = num1 <= num3
expressao5 = num1 != num4
print(2 == 2)
print(2 == 1)
print(2 >= 1)
print(2)
print(num1 == num2)

print(expressao)
print(expressao1)
print(expressao2)
print(expressao3)
print(expressao4)
print(expressao5)

nome = input('QUal o seu Nome: ')
idade = int(input('Qual é a sua idade: '))

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} é maior de idade')
else:
    print(f'{nome} é menor de idade')
