"""
Metodos de strings:
isnumeric: Verifica se há números decimais, subscripts, superscripts,
ração vulgar, numeros romanos, numeradores de moeda e digitos da china, japão e outras línguas
isdigit: Verifica se há números decimais, subscripts e superscripts
isdecimal: Verifica se há números decimais
"""
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter')



# num3 = int(input('Digite um numero: '))
# num4 = int(input('Digite um numero: '))
#
# print(num3 + num4)

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False