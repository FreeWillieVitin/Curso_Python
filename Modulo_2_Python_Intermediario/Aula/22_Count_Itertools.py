"""
count é um iterador sem fim (itertools)
"""
from itertools import count

c1 = count(start=10, step=8) # A classe count é muito similar ao range, a diferença é que o range necessita de um paramêtro de fim, já o count é um contador sem fim e que vem de um modulo separado, ou seja deve ser importado.
r1 = range(10, 100, 8) # O range precisa de parâmetro para indicar o seu fim, no caso o seu fim é 100

print('Count')
for i in c1:
    if i >= 100: # Iteração com o count, foi necessário uma condição para que a iteração chegue ao fim em um determinado número, caso contrário ele fica em um looping infinito
        break

    print(i)
print()
print('Range')
for x in r1:
    print(x) # O range ja teve seu fim definido na variável