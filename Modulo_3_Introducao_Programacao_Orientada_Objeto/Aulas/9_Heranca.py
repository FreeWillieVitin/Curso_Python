"""
Herança simples - Relações entre classes
Associação - usa, Agregação - tem
Composição - É dono de, Herança - É um

Herança vs Composição

Classe principal (Pessoa)
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""
class Pessoa(object): # Na criação da classe, automaticamente a super classe já vem herdada de uma classe padrão python que é a superclasse object
    cpf = '11131867980' # Atributo da classe Pessoa

    def __init__(self, nome, sobrenome): # Construtor da classe com os atributos nome e sobrenome
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self): # Método para retornar o nome, sobrenome e de qual sub classe esses nomes pertencem
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    cpf = 'cpf aluno' # Atributo da classe Aluno, segundo a ordem de resolução dos métodos, o cpf da classe aluno mesmo herdando da classe pessoa
# Será exibido o valor que foi passado dentor da subclasse no caso será exibido o cpf aluno e nao o valor numérico acima

c1 = Cliente('Victor', 'Hugo') # Definindo os valores do objeto c1 da classe Cliente
c1.falar_nome_classe() # Execução do método da superclasse Pessoa, essa execução retornará o valor herdado da classe pai Pessoa, mesmo sendo de um objeto da classe filho CLiente
a1 = Aluno('Marieli', 'Stankievski')
a1.falar_nome_classe()
print(a1.cpf) # Segundo a ordem de resolução, mesmo o objeto a1 sendo de uma classe filha que herda informações da classe pessoa, o valor do cpf retornado será o que foi passado dentro da classe filha e não o valor passado na classe pai
print()
# help(Foo)
# ---------------------------------------------------------------------------------------------------------------------------------------------

"""
Sobreposição de membros e class super
"""
class MinhaString(str): # Aqui temos uma classe que herda de uma superclasse chamada str, essa classe str tem um metódo chamado upper
    def upper(self): # Se tentarmos criar um método dentro da classe filha com o mesmo nome de uma classe existente na classe pai haverá um erro
        print('Chamou Upper') # Mas se quisermos fazer alguma coisa enquando o sistema executa aquele método da classe pai, podemos usar a class super
        retorno = super().upper() # A class super quando não tem parametro indicado, mostra ao sistema que será retornado o método passado após o ponto
        print('Depois Upper') # Da classe anterior, que no caso é a classe pai, mas caso a classe anterior seja filha de uma outra classe e assim por diante
        return retorno # Podemos também passar um parâmetro para o super indicando qual classe pai será a responsavel pelo método a ser usada como no exemplo abaixo:
		
    
string = MinhaString('Victor')
print(string.upper())
print()

class A: # Aqui temos uma classe que herdará o seu método para a classe seguinte e assim por diante
    atributo_a = 'valor_a'

    def metodo(self):
        print('A')
        
class B(A): # A classe B recebe o método da classe A
    atributo_b = 'valor_b'

    def metodo(self):
        print('B')
        
class C(B): # E a classe C recebe o método da B que por coincidência recebe o método da classe A
    atributo_c = 'valor_c'

    def metodo(self): # Entãoo dessa forma usando o super() podemos acessar os métodos das classes anteriores seguinto a ordem de resolução dos métodos
        super().metodo() # B
        super(C, self).metodo() # B
        super(B, self).metodo() # A
        # super(A, self).metodo() # object
        print('C')

print(C.mro())  
print(B.mro())  
print(A.mro())  
c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

