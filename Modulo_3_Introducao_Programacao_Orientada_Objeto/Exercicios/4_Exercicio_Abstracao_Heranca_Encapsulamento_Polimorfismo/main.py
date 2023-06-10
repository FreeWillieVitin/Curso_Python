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
from Contas import ContaCorrente, ContaPoupanca
from Pessoas import Pessoa, Cliente
from Bancos import Banco

c1 = Cliente('Victor', 25)
continha = ContaCorrente(111, 5963963, 2000)
b1 = Banco()
c1.add_conta(continha)
b1._conta = c1._conta
b1.add_cliente(c1)
print(b1._conta)
print(b1._cliente)
print(b1._conta[0])

# for c in list():
#     for b in b1._conta:
#         if c in b:
#             valor = 500

#             if continha.sacar(valor):
#                 print(f"Saque de R${valor} realizado com sucesso.")
#             else:
#                 print("Saldo insuficiente.")
#         else:
#             print("Cliente ou conta não autenticados.")

# continha.sacar(2500)
# continha.deposito(3000)
# continha.sacar(5300)





