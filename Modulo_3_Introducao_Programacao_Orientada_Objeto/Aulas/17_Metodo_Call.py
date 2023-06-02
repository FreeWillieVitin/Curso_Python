"""
Método especial __call__
Callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma 
classe "callable"
"""
class CallMe: # Função com o método call, com esse método podemos executar o método sem precisar passar parenteses para ele, apenas chamando a função e passando os valores para o atributo
    def __init__(self, fone) -> None: # Método init onde é criado o atributo fone
        self.fone = fone

    def __call__(self, nome): # Então criamos o método call e passamos para ele um argumento nome e abaixo a ação do método
        print(nome,'está Chamando,', self.fone)

call1 = CallMe('36422414') # Enfim passamos o valor do atributo fone para um objeto
call1('Judite') # E passamos o valor do argumento nome do método call sem precisar executar o método diretamente, apenas passando os valores a ação é executada