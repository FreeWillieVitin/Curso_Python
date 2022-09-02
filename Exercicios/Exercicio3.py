"""
Exercício de laços
"""
x = -1
y = 11
while x < 8:
    while y > 2:
        y = y - 1
        x = x + 1
        print(x, y)

"""
Correção
"""
for i, r in enumerate(range(10, 1, -1)):
    print(i, r)
