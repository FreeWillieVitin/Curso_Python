from __future__ import annotations
from abc import ABC, abstractmethod


class Som:
    def __init__(self) -> None:
        self.modo: ModoLigado = ModoRadio(self)
        self.tocando = 0

    def muda_modo(self, modo: ModoLigado) -> None:
        print(f'Mudando para modo: {modo.__class__.__name__}')
        self.tocando = 0
        self.modo = modo

    def proxima(self) -> None:
        self.modo.proxima()
        print(self)

    def anterior(self) -> None:
        self.modo.anterior()
        print(self)

    def __str__(self) -> str:
        return str(self.tocando)


class ModoLigado(ABC):
    def __init__(self, som: Som) -> None:
        self.som = som

    @abstractmethod
    def proxima(self) -> None:
        pass

    @abstractmethod
    def anterior(self) -> None:
        pass


class ModoRadio(ModoLigado):
    def proxima(self) -> None:
        self.som.tocando += 1000

    def anterior(self) -> None:
        self.som.tocando -= 1000 if self.som.tocando > 0 else 0


class ModoMusica(ModoLigado):
    def proxima(self) -> None:
        self.som.tocando += 1

    def anterior(self) -> None:
        self.som.tocando -= 1 if self.som.tocando > 0 else 0


if __name__ == "__main__":
    som = Som()

    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.anterior()
    som.anterior()
    som.anterior()

    print()
    som.muda_modo(ModoMusica(som))

    print()
    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.proxima()
    som.anterior()
    som.anterior()
    som.anterior()
