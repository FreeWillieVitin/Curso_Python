"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final)
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


# Receiver
class Luz:
    def __init__(self, name: str, sala_nome: str) -> None:
        self.name = name
        self.sala_nome = sala_nome
        self.cor = 'Cor Padrão'

    def ligado(self):
        print(f'{self.name} do {self.sala_nome} está ligada')

    def desligado(self):
        print(f'{self.name} do {self.sala_nome} está desligada')

    def muda_cor(self, cor: str):
        self.cor = cor
        print(f'{self.name} do {self.sala_nome} está na cor {self.cor}')


# Interface de comando
class Comando(ABC):
    @abstractmethod
    def executa(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# Comando Concreto
class AcendeLuz(Comando):
    def __init__(self, luz: Luz) -> None:
        self.luz = luz

    def executa(self) -> None:
        self.luz.ligado()

    def undo(self) -> None:
        self.luz.desligado()


class MudaCor(Comando):
    def __init__(self, luz: Luz, cor: str) -> None:
        self.luz = luz
        self.cor = cor
        self._cor_atual = self.luz.cor

    def executa(self) -> None:
        self._cor_atual = self.luz.cor
        self.luz.muda_cor(self.cor)

    def undo(self) -> None:
        self.luz.muda_cor(self._cor_atual)


# Invoker
class ControleRemoto:
    def __init__(self) -> None:
        self._botao: Dict[str, Comando] = {}
        self._desfazer: List[Tuple[str, str]]

    def add_botao_comando(self, valor: str, comando: Comando) -> None:
        self._botao[valor] = comando

    def botao_executa(self, nome: str) -> None:
        if nome in self._botao:
            self._botao[nome].executa()
            self._desfazer.append((nome, 'executa'))

    def botao_desfaz(self, nome: str) -> None:
        if nome in self._botao:
            self._botao[nome].undo()
            self._desfazer.append((nome, 'undo'))

    def global_undo(self):
        if not self._desfazer:
            return None

        nome_botao, acao = self._desfazer[-1]

        if acao == 'execute':
            self._botao[nome_botao].undo()
        else:
            self._botao[nome_botao].executa()

        self._desfazer.pop()


if __name__ == "__main__":
    quarto = Luz('Luz quarto', 'Quarto')
    banheiro = Luz('Luz banheiro', 'Banheiro')

    liga_luz1 = AcendeLuz(quarto)
    liga_luz2 = AcendeLuz(banheiro)

    cor = MudaCor(quarto, 'Verde')
    cor2 = MudaCor(banheiro, 'Rosa')

    controle = ControleRemoto()
    controle.add_botao_comando('Primeiro Botão', liga_luz1)
    controle.add_botao_comando('Segundo Botão', cor)
    controle.add_botao_comando('Terceiro Botão', cor2)

    controle.botao_executa('Primeiro Botão')
    controle.botao_desfaz('Primeiro Botão')

    controle.botao_executa('Segundo Botão')
    controle.botao_desfaz('Segundo Botão')
    controle.botao_executa('Terceiro Botão')
    controle.botao_desfaz('Terceiro Botão')

    print()
    controle.global_undo()
