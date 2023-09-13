from collections.abc import Callable, Iterable, Mapping
from time import sleep
from threading import Thread
from threading import Lock
from typing import Any

print('Hello')

for i in range(10):
    print(i)
    sleep(.5)

print('World!')
print('')
#  ------------------------------------------------------------------------------------------------------------------------------


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 8)
t2.start()

t3 = MeuThread('Thread 3', 3)
t3.start()

for i in range(10):
    print(i)
    sleep(1)
print('')
# --------------------------------------------------------------------------------------------------------------------------------


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


th1 = Thread(target=vai_demorar, args=('Olá Mundo', 5))
th1.start()

th2 = Thread(target=vai_demorar, args=('Olá Mundo 2', 6))
th2.start()

th3 = Thread(target=vai_demorar, args=('Olá Mundo 3', 2))
th3.start()

th4 = Thread(target=vai_demorar, args=('Olá Mundo 3', 10))
th4.start()

# for i in range(10):
#     print(i)
#     sleep(1)

while th4.is_alive():
    print('Esperando a thread.')
    sleep(2)

print('')
# --------------------------------------------------------------------------------------------------------------------------------


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos.'
              f'Ainda temos {self.estoque}')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
