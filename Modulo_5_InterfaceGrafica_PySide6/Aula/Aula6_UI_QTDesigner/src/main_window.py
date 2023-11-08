from typing import Optional, cast
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import QObject, QEvent
from Aula6_QT_Designer_UI import Ui_PrimeiraJanela
from PySide6.QtWidgets import QMainWindow, QApplication
"""
Após criar a sua aplicação usando o QTDesigner, podemos gerar o arquivo de estrutura do sistema
para seguir com o desenvolvimento de suas funções, para isso foi criado uma nova classe que
herdará, a QMainWindow para ter acesso as funções da classe e herdaremos também a classe da aplicação
que vem do módulo python criado automaticamente pelo QTDesigner, dentro desse módulo existe uma classe
que é nomeada pelo desenvolvedor, durante o uso do QTDesigner, essa classe contém toda a estrutura
visual da aplicação, como os botões, campos de texto e etc, apartir disso podemos criar Slots para
esse objetos
"""


# QMainWindow: Classe do PySide6 para acessar funções de estruturação da janela principal do sistema
# Ui_PrimeiraJanela: Classe com nome que pode ser variável onde está toda a interface criada no QTDesigner
class MainWindow(QMainWindow, Ui_PrimeiraJanela):
    def __init__(self, parent=None) -> None:  # Método construtor init
        super().__init__(parent)  # Chama o método contrutor da classe herdada
        self.setupUi(self)  # Configura e inicializa os elementos graficos do arquivo de estrutura do QTDesigner

        self.btn.clicked.connect(self.changeMainLabel)  # Conecta o botão ao método que altera o texto da label

        self.LineName.installEventFilter(self)  # Monitorar o que é passado para o objeto LineName(Nome dado ao campo de texto)

    def changeMainLabel(self):
        text = self.LineName.text()  # Método que armazena na variável o que é digitado no campo de texto
        self.labelResult.setText(text)  # E transcreve ao ser pressionado o botão enviar para um label que esta no centro da tela

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:  # Esse método captura o evento do clique de uma tecla
        if event.type() == QEvent.Type.KeyPress:  # Usa a classe QEvent para captar o evento de digito se for igual ao parâmetro
            event = cast(QKeyEvent, event)
            # text = self.LineName.text()
            # self.labelResult.setText(text + event.text())
            # Exibe a tecla digita, se descomentar o código acima o que for digitado é mostrado no label em tempo real
            print(event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
