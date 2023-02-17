"""
Trocar valores de variáveis, sem precisar ficar criando variáveis
"""
x = 10
y = 'Victor'

# z = x
# x = y
# y = z
# ou

x, y = y, x

print(f'x={x} e y={y}')