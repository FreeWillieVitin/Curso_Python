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

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)