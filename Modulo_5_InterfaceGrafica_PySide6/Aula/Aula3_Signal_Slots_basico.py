"""
O básico sobre Signal e Slots (eventos e documentação)
"""

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


def segundo_slot(status_bar):
    status_bar.showMessage('O slot foi executado')


# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
acao = primeiro_menu.addAction('Primeira Ação')
acao.triggered.connect(lambda: exemplo_acao(status_bar))

acao2 = primeiro_menu.addAction('Segunda Ação')
acao2.setCheckable(True)
# acao2.triggered.connect(lambda: exemplo_acao(status_bar))
acao2.toggled.connect(lambda: exemplo_acao(status_bar))

window.show()
app1.exec()
