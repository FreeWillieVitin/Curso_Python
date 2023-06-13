"""
# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass, asdict, astuple, field, fields # Importa o módulo dataclasses e a função dataclass, também temos as funções de conversão como asdict e astuple

@dataclass() # Para usar a função precisamos iniciar com o decorator @dataclass, se quiser usar o dataclass, mas ainda sim quiser criar o método init, é colocado como parâmetro init=false
class Pessoa: # Criação da classe exatamente como da forma tradicional
    nome: str # A diferença começa na criação dos atributos onde precisamos apenas passar o nome do atributo e o seu tipo separado por :
    idade: int # E pronto, a classe está criada, a função dataclass além do init, ela engloba reprs e o método eq, usado para comparar objetos 
    sobrenome: str

    @property # E por ser uma classe como qualquer outra apenas com uma estrutura um pouco diferente, podemos usar getters e setters
    def nome_completo(self): # Aqui temos um método getter que retorna o nome, sobrenome e idade passadas como atributo 
        return f'{self.nome} {self.sobrenome} {self.idade}'
    
    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    def __post_init__(self): # Post init é o método que vai ser executado após o init
        print('POST INIT')
        self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter 
    def nome_completo(self, valor): # E em seguida temos um setter que recebe um nome completo e divide ele como nome e sobrenome separados
        nome, sobrenome = valor.split() # A função split é a responsável pela separação do nome e definir em suas variáveis
        self.nome = nome
        self.sobrenome = sobrenome

if __name__ == '__main__':
    p1 = Pessoa('Victor', 25, 'Hugo')
    p1.nome_completo = 'Marieli Stankievski'
    print(p1)
    print(p1.nome_completo)
    print(asdict(p1).values()) # Converte em dicionario e pode ser usada todas as funcionalidades de um dicionario
    print(astuple(p1)[0]) # O mesmo ocorre para a tuplas
    # p2 = Pessoa('Victor', 25)
    # print(p1 == p2) # Uso do __eq__ comparando as duas pessoas acima, sem a necessidade de criar o método __eq__ na classe
    print()
# --------------------------------------------------------------------------------------------------------------------------------------------

"""
Valores padrão e filed em dataclasses
"""
@dataclass
class Pessoa2:
    nome: str = field(default='Falta nome', repr=False) # Usando a função field podemos configurar atributos, para se comportar de formas diferentes, como por exemplo receber um valor padrão ou não retirar aquele atributo do repr
    sobrenome: str = 'Hugo'
    idade: int = 25
    enderecos: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p2 = Pessoa2()
    print(p2)
    print(fields(p2))