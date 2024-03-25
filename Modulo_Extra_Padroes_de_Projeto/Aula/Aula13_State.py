"""
O padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Pedido:
    # Context
    def __init__(self) -> None:
        self.status: StatusPedido = PagamentoPendente(self)

    def pendente(self) -> None:
        print('Tentando mover para pendente')
        self.status.pendente()
        print(f'Estado atual: {self.status}')
        print()

    def aprovado(self) -> None:
        print('Tentando mover para aprovado')
        self.status.aprovado()
        print(f'Estado atual: {self.status}')
        print()

    def rejeitado(self) -> None:
        print('Tentando mover para rejeitado')
        self.status.rejeitado()
        print(f'Estado atual: {self.status}')
        print()


class StatusPedido(ABC):
    def __init__(self, pedido) -> None:
        self.pedido = pedido

    @abstractmethod
    def pendente(self) -> None:
        pass

    @abstractmethod
    def aprovado(self) -> None:
        pass

    @abstractmethod
    def rejeitado(self) -> None:
        pass

    def __str__(self):
        return self.__class__.__name__


class PagamentoPendente(StatusPedido):

    def pendente(self) -> None:
        print('Pagamento já está em estado pendente, aguardar aprovação!')

    def aprovado(self) -> None:
        self.pedido.status = PagamentoAprovado(self.pedido)
        print('Pagamento aprovado!')

    def rejeitado(self) -> None:
        self.pedido.status = PagamentoRejeitado(self.pedido)
        print('Pagamento Rejeitado!')


class PagamentoAprovado(StatusPedido):

    def pendente(self) -> None:
        self.pedido.status = PagamentoPendente(self.pedido)
        print('Pagamento voltou ao estado pendente!')

    def aprovado(self) -> None:
        print('Pagamento já foi aprovado')

    def rejeitado(self) -> None:
        self.pedido.status = PagamentoRejeitado(self.pedido)
        print('Pagamento Rejeitado!')


class PagamentoRejeitado(StatusPedido):

    def pendente(self) -> None:
        print('Pagamento recusado')

    def aprovado(self) -> None:
        print('Pagamento recusado')

    def rejeitado(self) -> None:
        print('Pagamento recusado')


if __name__ == "__main__":
    pedido = Pedido()
    pedido.pendente()
    pedido.aprovado()
    pedido.pendente()
    pedido.rejeitado()
    pedido.pendente()
    pedido.aprovado()
