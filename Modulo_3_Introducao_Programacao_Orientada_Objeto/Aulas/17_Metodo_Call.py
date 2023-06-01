"""
Método especial __call__
Callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma 
classe "callable"
"""
class CallMe:
    def __init__(self, fone) -> None:
        self.fone = fone

    def __call__(self, nome):
        print(nome,'está Chamando,', self.fone)

call1 = CallMe('36422414')
call1('Judite')