"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool

Metodos de strings:
isnumeric: Verifica se há números decimais, subscripts, superscripts,
ração vulgar, numeros romanos, numeradores de moeda e digitos da china, japão e outras línguas
isdigit: Verifica se há números decimais, subscripts e superscripts
isdecimal: Verifica se há números decimais
zfill: Acrescenta a quantidade de zero definida pelo usuario a esquerda de uma string
"""
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter')

string = '1000'
print(string.zfill(10))

# num3 = int(input('Digite um numero: '))
# num4 = int(input('Digite um numero: '))
#
# print(num3 + num4)
