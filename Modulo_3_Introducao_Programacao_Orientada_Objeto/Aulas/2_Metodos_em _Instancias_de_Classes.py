"""
Métodos em instâncias de classes Python
Hard codded - É Algo que  foi escrito diretamente no código
"""
class Carro: # Criamos uma classe e dentro dela teremos nossa função inicializadora e um método, esse método podemos executar no momento de execução do objeto
    def __init__(self, nome): # Função inicializadora definindo sempre o argumento self, e criamos um argumento secundário para receber o nome como parâmetro
        self.nome = nome

    def acelerar(self): # Dentro da classe criamos um método básico que executa uma ação a partir do nome passado como argumento
        print(f'{self.nome} está acelerando...') # Dessa forma o método exibe o valor de atributo passado com sua ação

fusca = Carro('Fusca') # Objeto com seu atributo
print(fusca.nome)
fusca.acelerar() # Objeto executando o método criado na classe

celta = Carro(nome='Celta')
print(celta.nome)
Carro.acelerar(celta)

"""
Entendendo self em classes Python
Classe - Molde(geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instância.
O argumento self tem esse nome apenas por convenção, pois poderia ser qualquer outro nome, mas basicamente o self é o primeiro argumento para referenciar uma instância
"""