"""
Introdução às Generator Functions em Python
Generator = (n for n in range(1000))
Continuação da Aula 22 do Modulo 1 Estrutura_For Seção iterator
"""
def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Terminar')
    return 'ACABOU'

gen = generator(n=0)
print(next(gen))
print(next(gen))

print()

for n in gen:
    print(n)

def generator2(n=0, maximun=10):
    while True:
        yield n
        n +=1

        if n > maximun:
            return

gen2 = generator2(maximun=100)
for n in gen2:
    print(n)

print()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yield From
def generator3():
    yield 1
    yield 2
    yield 3
    print('Acabou o gen3')
    print()

def generator4(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6

g = generator4(generator3)
for i in g:
    print(i)