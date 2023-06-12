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