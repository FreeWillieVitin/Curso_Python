"""
Exercício com classes
1 - Crie uma classe Carro (Nome)
2 - Crie uma classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça a ligação entre Carro tem um Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e um Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela
"""
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def exibir_carro():
        motor = Motor('Vrum')
        fabricante1 = Fabricante('Fiat')
        fabricante2 = Fabricante('Ford')
        p1, p2 = Carro('Argo'), Carro('Fiesta')
        motor.inserir_carros(p1, p2)
        fabricante1.inserir_carros(p1)
        fabricante2.inserir_carros(p2)
        print(f'O carro {p1.nome} foi fabricado por {fabricante1.nome} e usa o motor {motor.nome}')
        print(f'O carro {p2.nome} foi fabricado por {fabricante2.nome} e usa o motor {motor.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._carro = []

    def inserir_carros(self, *carros):
        for carro in carros:
            self._carro.append(carro)

    def listar_carros(self):
        print()
        for carro in self._carro:
            print(carro.nome)
        print()

class Fabricante:
    def __init__(self, nome):
        self.nome = nome 
        self._carro1 = []

    def inserir_carros(self, *carros1): 
        for carro1 in carros1:
            self._carro1.append(carro1)

    def listar_carros(self): 
        print()
        for carro1 in self._carro1:
            print(carro1.nome)
        print()

Carro.exibir_carro()
# -----------------------------------------------------------------------------------------------------------------------------------------
print()
"""
Correção do professor
"""
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
# ---------------------------------------------------------------------------------------------------------------------------------------------

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    def exibir_detalhes(self):
        print("Carro:", self.nome)
        print("Motor:", self.motor.nome)
        print("Fabricante:", self.fabricante.nome)
        print()


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# Criando instâncias das classes
motor1 = Motor("Motor 1")
motor2 = Motor("Motor 2")

fabricante1 = Fabricante("Fabricante 1")
fabricante2 = Fabricante("Fabricante 2")

carro1 = Carro("Carro 1", motor1, fabricante1)
carro2 = Carro("Carro 2", motor2, fabricante1)
carro3 = Carro("Carro 3", motor1, fabricante2)

# Exibindo os detalhes dos carros
carro1.exibir_detalhes()
carro2.exibir_detalhes()
carro3.exibir_detalhes()






