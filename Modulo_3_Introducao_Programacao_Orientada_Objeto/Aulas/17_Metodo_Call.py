"""
Método especial __call__
Callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma classe "callable"
"""


# Classe com o método call, com esse método podemos executar a classe sem precisar passar parenteses para ele,
# apenas chamando a função e passando os valores para o atributo
class CallMe:
    # Função init onde é criado o atributo fone
    def __init__(self, fone) -> None:
        self.fone = fone

    # Então criamos o método call e passamos para ele um argumento nome e abaixo a ação do método
    def __call__(self, nome):
        print(nome, 'está Chamando,', self.fone)


# Enfim passamos o valor do atributo fone para um objeto
call1 = CallMe('36422414')

# E passamos o valor do argumento nome do método call sem precisar executar o método diretamente, apenas passando os valores
# a ação é executada
call1('Judite')
