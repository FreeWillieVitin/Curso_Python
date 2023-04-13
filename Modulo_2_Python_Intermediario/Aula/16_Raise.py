"""
raise - lançando exceções (error)
continuação da aula 16 - Introducao_try_Except do modulo 1
"""
def error(d):
    if d == 2:
        raise ValueError('Você está tentando dividir')


def divide(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} Deve ser um valor int ou float'
        )
    
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'{d} Deve ser um valor int ou float'
        )
    error(d)
    return n / d
    

print(divide(8, 1))