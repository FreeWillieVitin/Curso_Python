"""
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6
"""
# import sys

# from PySide6.QtWidgets import QApplication, QPushButton

# app = QApplication()

# botao = QPushButton('Marieli Amor da Minha Vida')  # Exibe um botão na tela com um texto dentro
# botao.setStyleSheet('font-size: 40px; color: Pink; background-color: blue')  # Estiliza o botão usando comandos CSS
# botao.show()  # Adiciona o widget na hierarquia e exibe a janela

# botao2 = QPushButton('Botão2')
# botao2.show()

# app.exec()  # Executa a aplicação
# --------------------------------------------------------------------------------------------------------------------------------

"""
# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

Os processos da aplicação - QMainWindow e centralWidget
-> QApplication (app)
    -> QMainWnow (window->setCentralWdget)
        -> CentralWidget (central_widget)
            -> Layout
                -> Widget 3 (Botão 3)
                -> Widget 4 (Botão 4)
                -> Widget 5 (Botão 5)
    -> show
-> exec
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow

app1 = QApplication()  # Indica um inicializador de aplicação para a variável
window = QMainWindow()
central_widget = QWidget()   # O QWidget seria como um formulário onde é posicionado os itens e exibido ao usuário
window.setCentralWidget(central_widget)
window.setWindowTitle('Meu primeiro programa')

botao3 = QPushButton('Marieli Amor da Minha Vida')
botao3.setStyleSheet('font-size: 40px; color: Pink; background-color: blue')

botao4 = QPushButton('Botão')
botao4.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')

botao5 = QPushButton('Botão2')
botao5.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')


layout = QGridLayout()  # QGridLayout é um layout que seria como uma tabela, existem vários outros tipos e layout
central_widget.setLayout(layout)  # Define qual o tipo de layout da determinada sessão da aplicação

layout.addWidget(botao3, 1, 2, 1, 1)  # A função addWidget adiciona item em um layout, essa função também recebe valores
layout.addWidget(botao4, 1, 1, 1, 1)  # de posicionamento, após indicar o que será adicionado, o proximo parâmetro indica em qual
layout.addWidget(botao5, 3, 1, 1, 2)  # linha o item se posicionará, a seguir a coluna

# Barra de Status
status_bar = window.statusBar()
status_bar.showMessage('Barra de Status')


def exemplo_acao(status_bar):
    status_bar.showMessage('O slot foi executado')


# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
acao = primeiro_menu.addAction('Primeira Ação')
acao.triggered.connect(lambda: exemplo_acao(status_bar))

window.show()
app1.exec()
