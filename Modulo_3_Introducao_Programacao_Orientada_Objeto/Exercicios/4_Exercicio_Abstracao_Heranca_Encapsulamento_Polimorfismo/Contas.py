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
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, numconta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numconta = numconta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:...

    def deposito(self, valor: float) -> None:
        self.saldo += valor

class ContaPoupanca(Conta):    
    def sacar(self, valor):
        valor_saque = self.saldo - valor

        if valor_saque >= 0:
            self.saldo -= valor
            print('Saque efetuado')
            return self.saldo
        else:
            print('Valor abaixo do solicitado')

    def __repr__(self) -> str:
        attrs = f'Agência: {self.agencia!r}, Conta: {self.numconta!r}, Saldo: {self.saldo!r}'
        return f'{attrs}'

class ContaCorrente(Conta):
    limite = 500

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Valor do Saque excede o saldo e o limite permitido')
        else:
            self.saldo -= valor
            print(f'Você sacou {valor} da sua conta')

    def __repr__(self) -> str:
        attrs = f'Agência: {self.agencia!r}, Conta: {self.numconta!r}, Saldo: {self.saldo!r}'
        return f'{attrs}'
# -------------------------------------------------------------------------------------------------------------------------------------------


# Solução do professor
# import abc


# class Conta(abc.ABC):
#     def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
#         self.agencia = agencia
#         self.conta = conta
#         self.saldo = saldo

#     @abc.abstractmethod
#     def sacar(self, valor: float) -> float: ...

#     def depositar(self, valor: float) -> float:
#         self.saldo += valor
#         self.detalhes(f'(DEPÓSITO {valor})')
#         return self.saldo

#     def detalhes(self, msg: str = '') -> None:
#         print(f'O seu saldo é {self.saldo:.2f} {msg}')
#         print('--')

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
#         return f'{class_name}{attrs}'


# class ContaPoupanca(Conta):
#     def sacar(self, valor):
#         valor_pos_saque = self.saldo - valor

#         if valor_pos_saque >= 0:
#             self.saldo -= valor
#             self.detalhes(f'(SAQUE {valor})')
#             return self.saldo

#         print('Não foi possível sacar o valor desejado')
#         self.detalhes(f'(SAQUE NEGADO {valor})')
#         return self.saldo


# class ContaCorrente(Conta):
#     def __init__(
#         self, agencia: int, conta: int,
#         saldo: float = 0, limite: float = 0
#     ):
#         super().__init__(agencia, conta, saldo)
#         self.limite = limite

#     def sacar(self, valor: float) -> float:
#         valor_pos_saque = self.saldo - valor
#         limite_maximo = -self.limite

#         if valor_pos_saque >= limite_maximo:
#             self.saldo -= valor
#             self.detalhes(f'(SAQUE {valor})')
#             return self.saldo

#         print('Não foi possível sacar o valor desejado')
#         print(f'Seu limite é {-self.limite:.2f}')
#         self.detalhes(f'(SAQUE NEGADO {valor})')
#         return self.saldo

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
#             f'{self.limite!r})'
#         return f'{class_name}{attrs}'


# if __name__ == '__main__':
#     cp1 = ContaPoupanca(111, 222)
#     cp1.sacar(1)
#     cp1.depositar(1)
#     cp1.sacar(1)
#     cp1.sacar(1)
#     print('##')
#     cc1 = ContaCorrente(111, 222, 0, 100)
#     cc1.sacar(1)
#     cc1.depositar(1)
#     cc1.sacar(1)
#     cc1.sacar(1)
#     cc1.sacar(98)
#     cc1.sacar(1)
#     print('##')