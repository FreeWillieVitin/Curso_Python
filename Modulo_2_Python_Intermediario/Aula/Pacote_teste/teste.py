__all__ = [
    'multi',
    'vezes',
]

from Pacote_teste.teste2 import fala

def multi(*args):
    result = 1
    for calc in args:
        print('Total', result, '*', calc) 
        result = result * calc
        print('Total', result)
    return result

vezes = multi(2,3,4,5)
print(vezes)
fala()


nova = 'Ok'
