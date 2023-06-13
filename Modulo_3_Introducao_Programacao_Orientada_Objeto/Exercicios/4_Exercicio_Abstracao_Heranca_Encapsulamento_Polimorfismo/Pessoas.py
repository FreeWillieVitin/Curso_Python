"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco 
"""
from Contas import ContaPoupanca, ContaCorrente, Conta

class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = []

    def __repr__(self) -> str:
        # class_name = type(self).__name__
        attrs = f'Cliente: {self.nome!r}, Idade: {self.idade!r}'
        return f'{attrs}'

    def add_conta(self, *contas):
        for conta in contas:
            self._conta.append(conta)
# -------------------------------------------------------------------------------------------------------------------------------------------

# Solução do professor
# import contas


# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome: str):
#         self._nome = nome

#     @property
#     def idade(self):
#         return self._idade

#     @idade.setter
#     def idade(self, idade: int):
#         self._idade = idade

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.nome!r}, {self.idade!r})'
#         return f'{class_name}{attrs}'


# class Cliente(Pessoa):
#     def __init__(self, nome: str, idade: int) -> None:
#         super().__init__(nome, idade)
#         self.conta: contas.Conta | None = None


# if __name__ == '__main__':
#     c1 = Cliente('Luiz', 30)
#     c1.conta = contas.ContaCorrente(111, 222, 0, 0)
#     print(c1)
#     print(c1.conta)
#     c2 = Cliente('Maria', 18)
#     c2.conta = contas.ContaPoupanca(112, 223, 100)
#     print(c2)
#     print(c2.conta)