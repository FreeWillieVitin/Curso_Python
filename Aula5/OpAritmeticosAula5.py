"""
+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
// = Divisão inteira, ou seja o resultado da divisão é arredondado
** = Exponenciação, um número elevado a outro
% = modulo ou o resto da divisão de um número
() = Altera as precedence da conta
"""

print("Adição", 10 + 10)  # Adição
print("Subtração", 10 - 5)  # Subtração
print("Multiplicação", 10 * 10)  # Multiplicação
print("Divisão", 6 / 3)  # Divisão
print(10 * '10')  # Se multiplicar um número inteiro com uma string ele retorna aquele texto sendo multiplicado
print('5' + '5')  # Se somar duas strings elas sao concatenadas

print(6.7 // 3.8)  # Faz a divisão e retorna a parte inteira do resultado
print(2 ** 10)  # Faz a potenciação
print(10 % 3)  # Faz a divisão e retorna o resto do resultado
print((5+2)*10)  # Altera a ordem dos calculos
