"""
raise - lançando exceções (error)
continuação da aula 16 - Introducao_try_Except do modulo 1
"""

def error(d): # Temos também a keyword raise, ela é utilizada para criar o nosso próprio erro, como no exemplo abaixo, para isso usamos o raise e damos uma classe de erro para ele
    if d == 2: # Criamos essa função para impedir que o usuário use o valor 2 como valor de divisão, 2 normalmente é um valor divisório, mas ao darmos essa condição ao sistema
        raise ValueError('Você está tentando dividir') # E definir isso como um erro qualquer outro numero divisivel pode ser usado excluíndo o 2


def divide(n, d): # Aqui temos um outro erro criado para evitar que o sistema aceite valor que não é inteiro ou flutuante
    if not isinstance(n, (float, int)): # Atráves da função isinstance() definimos os tipos aceitos
        raise TypeError( # E caso o tipo não seja o desejado então enviamos o erro ao usuário
            f'{n} Deve ser um valor int ou float'
        )
    
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'{d} Deve ser um valor int ou float'
        )
    error(d)
    return n / d
    

print(divide(8, 1))