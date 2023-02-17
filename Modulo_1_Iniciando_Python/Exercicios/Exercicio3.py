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

"""
Iterando strings com while
"""

nome = 'victor'  # Defina o nome na variavel
t_nome = len(nome) # Aplica a função de contagem de caracteres a variavel nome

val = 0 # Define a variavel de comparação como zero

while val < t_nome: # Enquanto a variavel de comparação for menor que a contagem dos caracteres
    print(val, nome[val]) # Retorne em tela o indice e qual letra pertence aquele indice
    val += 1 # Soma mais 1 a variável de comparação para continuar o laço de repetição

"""
Correção do professor
"""

nome = 'Maria Helena'  

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

