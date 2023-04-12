# Dictionary COmprehension e Set Comprehension
produto = {
    'nome': 'caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for chave , valor in produto.items():
    print(chave, valor)

print()

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(dc)
print()

s1 = {2 ** i for i in range(10)}
print(s1)