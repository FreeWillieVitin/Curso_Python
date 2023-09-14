"""
Deque - Trabalhando com LIFO e FIFO
deque - Double-ended queue Deque é preferível à lista nos casos em que precisamos de operações de acréscimo e pop mais rápidas de
ambas as extremidades do contêiner, já que deque fornece uma complexidade de tempo O (1) para operações de acréscimo e pop em
comparação com a lista que fornece complexidade de tempo O (n) .

Lifo  e fifo
pilha e fila

LIFO (Last In First Out)
Pilha (stack)
Significa que o último item a entrar será o primeiro a sair (list)
Artigo:
https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
Vídeo:
https://youtu.be/svWVHEihyNI
Para tirar itens do final: O(1) Tempo constante
Para tirar itens do início: O(n) Tempo Linear
"""

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Legal (LIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)
#  0  1  2  3  4  5  6  7  8  9  10  11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ultimo_registro = lista.pop()
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Ultimo a sair:', ultimo_registro)
print('Lista:', lista)
print()
# --------------------------------------------------------------------------------------------------------------------------------

lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 🚫 Ruim (FIFO com lista)
# [0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2.insert(0, 10)
# [0   1  2  3  4  5  6  7  8  9  10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2.insert(0, 11)
# [0   1  2  3  4  5  6  7  8  9  10  11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista2.pop(0)  # Removeu o primeiro registro
# [0   1  2  3  4  5  6  7  8  9  10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro:', primeiro_removido)
print('Lista:', lista2)
print()
# --------------------------------------------------------------------------------------------------------------------------------

"""
FIFO (First In First Out)
Filas (queue)
Significa que o primeiro item a entrar será o primeiro a sair (deque)
Artigo:
https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
Vídeo:
https://youtu.be/RHb-8hXs3HE
Para tirar itens do final: O(1) Tempo constante
Para tirar itens do início: O(1) Tempo constante
Documentação do modulo collections => https://docs.python.org/3/library/collections.html
"""

# ✅ Legal (FIFO com deque)

fila_correta: deque[int] = deque()
fila_correta.append(3)  # Adiciona no final
fila_correta.append(4)  # Adiciona no final
fila_correta.append(5)  # Adiciona no final
fila_correta.appendleft(0)  # Adiciona no começo
fila_correta.appendleft(1)  # Adiciona no começo
fila_correta.appendleft(2)  # Adiciona no começo
print(fila_correta)  # deque([2, 1, 0, 3, 4, 5])
fila_correta.pop()  # Exclui o 5
fila_correta.popleft()  # Exclui o 2
print(fila_correta)  # deque([1, 0, 3, 4])
