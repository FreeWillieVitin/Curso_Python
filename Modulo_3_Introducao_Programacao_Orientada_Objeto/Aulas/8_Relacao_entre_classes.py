"""
Relações entre classes: associação, agregação e composição
Associação é um tipo de relação onde os objetos
estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos
como agregação e composição (que veremos depois).
Geralmente, temos uma associação quando um objeto tem
um atributo que referencia outro objeto.
A associação não especifica como um objeto controla
o ciclo de vida de outro objeto.
"""
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
print()
# ------------------------------------------------------------------------------------------------------------------------------------------

"""
Agregação é uma forma mais especializada de associação
entre dois ou mais objetos. Cada objeto terá
seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um
objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode
se tratar de uma relação onde um objeto precisa de
outro para fazer determinada tarefa.
(existem controvérsias sobre as definições de agregação).
"""
class Carrinho: # Criação da classe carrinho
    def __init__(self): # Iniciando um atributo que será uma lista de produtos 
        self._produtos = []

    def inserir_produtos(self, *produtos): # Método para inserir os produtos e os preços na lista que foi a definida no atributo _produtos
        for produto in produtos:
            self._produtos.append(produto)

    def total(self): # Método que retornará a soma do valor dos produtos
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self): # Método que mostrará os produtos e seus respectivos preços
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto: # Classe que recebe os atributos nome e preço dos produtos e será "relacionado" com a classe carrinho, seguindo a ideia
    def __init__(self, nome, preco) -> None: # que os dois existem mas não funcionam separados
        self.nome = nome 
        self.preco = preco 

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('telefone', 40.00)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
print()
# ------------------------------------------------------------------------------------------------------------------------------------------

"""
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas
as referências dos objetos filhos também são
apagadas.
"""
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1


print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')