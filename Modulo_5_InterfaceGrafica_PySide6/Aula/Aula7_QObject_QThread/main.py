from typing import Optional
from PySide6.QtCore import QObject, Signal, Slot, QThread
import time
from PySide6.QtWidgets import QApplication, QWidget
from Aula7_main import Ui_MyObject


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        num = '0'
        self.started.emit(num)
        for i in range(1, 6):
            num = str(i)
            self.progressed.emit(num)
            time.sleep(1)
        self.finished.emit(num)


class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run2(self):
        num = '0'
        self.started.emit(num)
        for i in range(50, 100, 5):
            num = str(i)
            self.progressed.emit(num)
            time.sleep(0.3)
        self.finished.emit(num)


class MyWidget(QWidget, Ui_MyObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btn1.clicked.connect(self.hardWork1)
        self.btn2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()
        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker
        thread = self._thread

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente ou seja conecta ao run.
        thread.started.connect(worker.run)
        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # Garante que a Thread será removido da memória
        thread.finished.connect(thread.deleteLater)
        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        # Inicie a thread
        thread.start()

    def worker1Started(self, value):
        self.btn1.setDisabled(True)
        self.label.setText(value)
        print('Worker 2 Iniciado')

    def worker1Progressed(self, value):
        self.label.setText(value)
        print('2 em Progresso')

    def worker1Finished(self, value):
        self.btn1.setDisabled(False)
        self.label.setText(value)
        print('Worker 2 Finalizado')

    def hardWork2(self):
        self._worker2 = Worker2()
        self._thread2 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        # Nome do método "run" modificado para "run2" (p/ exemplo)
        thread.started.connect(worker.run2)
        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        # Inicie a thread
        thread.start()

    def worker2Started(self, value):
        self.btn2.setDisabled(True)
        self.label_2.setText(value)
        print('Worker Iniciado')

    def worker2Progressed(self, value):
        self.label_2.setText(value)
        print('em Progresso')

    def worker2Finished(self, value):
        self.label_2.setText(value)
        self.btn2.setDisabled(False)
        print('Worker Finalizado')


if __name__ == "__main__":
    app = QApplication()
    window = MyWidget()
    window.show()
    app.exec()
