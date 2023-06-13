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
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco 
"""
from Contas import Conta
from Pessoas import Pessoa, Cliente

class Banco():
    def __init__(self) -> None:
        self._cliente = []
        self._conta = None

    def add_cliente(self, *clientes):
        for cliente in clientes:
            self._cliente.append(cliente)

    def checagem_conta(self, dados):
        self._conta = dados
        return self._conta 
    
    def checagem_cliente(self, cliente):
        self._cliente = cliente
        return self._cliente
# -------------------------------------------------------------------------------------------------------------------------------------------


# Solução do professor
# import contas
# import pessoas


# class Banco:
#     def __init__(
#         self,
#         agencias: list[int] | None = None,
#         clientes: list[pessoas.Pessoa] | None = None,
#         contas: list[contas.Conta] | None = None,
#     ):
#         self.agencias = agencias or []
#         self.clientes = clientes or []
#         self.contas = contas or []

#     def _checa_agencia(self, conta):
#         if conta.agencia in self.agencias:
#             print('_checa_agencia', True)
#             return True
#         print('_checa_agencia', False)
#         return False

#     def _checa_cliente(self, cliente):
#         if cliente in self.clientes:
#             print('_checa_cliente', True)
#             return True
#         print('_checa_cliente', False)
#         return False

#     def _checa_conta(self, conta):
#         if conta in self.contas:
#             print('_checa_conta', True)
#             return True
#         print('_checa_conta', False)
#         return False

#     def _checa_se_conta_e_do_cliente(self, cliente, conta):
#         if conta is cliente.conta:
#             print('_checa_se_conta_e_do_cliente', True)
#             return True
#         print('_checa_se_conta_e_do_cliente', False)
#         return False

#     def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
#         return self._checa_agencia(conta) and \
#             self._checa_cliente(cliente) and \
#             self._checa_conta(conta) and \
#             self._checa_se_conta_e_do_cliente(cliente, conta)

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
#         return f'{class_name}{attrs}'

# if __name__ == '__main__':
#     c1 = pessoas.Cliente('Luiz', 30)
#     cc1 = contas.ContaCorrente(111, 222, 0, 0)
#     c1.conta = cc1
#     c2 = pessoas.Cliente('Maria', 18)
#     cp1 = contas.ContaPoupanca(112, 223, 100)
#     c2.conta = cp1
#     banco = Banco()
#     banco.clientes.extend([c1, c2])
#     banco.contas.extend([cc1, cp1])
#     banco.agencias.extend([111, 222])

#     if banco.autenticar(c1, cc1):
#         cc1.depositar(10)
#         c1.conta.depositar(100)
#         print(c1.conta)