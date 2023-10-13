"""
+ = Adição ou concatenação se for strings
- = Subtração
* = Multiplicação ou repetição de strings
/ = Divisão sempre retorna um valor float
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
print(10 % 2 == 0)  # Um dos usos do módulo é para checar se um numero é par ou impar

"""
Precendencia dos operadores
1. (n + n) e sempre de dentro para fora
2. **
3. * / // %
4. + -
"""

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

# Exercicio de IMC
nome = 'Victor Hugo'
idade = 24
altura = 1.74
peso = 84
imc = peso / (altura * altura)

print('Seu nome é', nome, 'tem', altura, 'metros, pesa', peso, 'quilos, e seu imc é', imc)

