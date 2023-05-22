"""
@property - um getter em modo pythonico.
getter - um método para obter um atributo.
modo pythonico - modo do python de fazer as coisas.
@property é uma propriedade do objeto, ela é um método que se comporta como um atributo.
Geralmente é usada nas seguintes situações:
    como getter
    p/ evitar quebrar código cliente
    p/ habilitar setter
    p/ executar ações ao obter um atributo
Código cliente - é o código que usa seu código
"""
class Caneta: # Classe
    def __init__(self, cor): # Definida os atributos da calsse
        self.cor_tinta = cor

    def get_cor(self): # Função getter, funciona como um executor para evitar problemas se houver alterações em nomes ou qualquer mudança no codigo
        return self.cor_tinta # Pois dessa forma executamos apenas a função e seu retorno será do atributo definido no seu escopo, 
    
    @property # Da mesma forma que o getter, o decorator property é executado na forma de atributo pela instancia
    def cor(self):
        print('qualquer coisa')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        print('Vermelho')
        return 123456
    
caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)
print()
# --------------------------------------------------------------------------------------------------------------------------------------------

"""
@property + @setter - getter e setter no modo Pythonico
getter -> obter valor
setter -> passa o valor
"""
class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor
        self._cor_tampa = None

    @property # Decorator que indica um getter
    def cor(self): # Declaração do método
        print('ESTOU NO GETTER') # Apenas um informativo que mostra que esse método é um getter ou seja um receptor de dados
        return self._cor # Retorna o que for recebido

    @cor.setter # Decorator que indica um setter, deve ser passado o nome do método na frente seguido da palavra .setter
    def cor(self, valor): # Aqui é passado os argumentos que servirão para entregar os dados ao getter
        print('ESTOU NO SETTER') # Apenas um informativo que mostra que esse método é um setter ou seja um entregador de dados
        self._cor = valor # Não retorna nada, apenas armazena o valor no atributo

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul') # Define o objeto caneta para receber a classe
caneta.cor = 'Rosa' # Indica ao setter o valor do atributo cor
caneta.cor_tampa = 'Azul' # Indica ao setter o valor do atributo cor_tampa
print(caneta.cor) # Exibe o método getter retornando o valor informado no método setter
print(caneta.cor_tampa)