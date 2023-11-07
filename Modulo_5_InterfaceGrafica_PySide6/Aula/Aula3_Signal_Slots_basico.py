"""
O básico sobre Signal e Slots (eventos e documentação)
"""
from typing import Optional
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow
from PySide6.QtCore import Slot

# app1 = QApplication()  # Indica um inicializador de aplicação para a variável
# window = QMainWindow()
# # O QWidget seria como um formulário onde é posicionado os itens e exibido ao usuário
# central_widget = QWidget()
# window.setCentralWidget(central_widget)
# window.setWindowTitle('Meu primeiro programa')

# botao3 = QPushButton('Marieli Amor da Minha Vida')
# botao3.setStyleSheet('font-size: 40px; color: Pink; background-color: blue')

# botao4 = QPushButton('Botão')
# botao4.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')

# botao5 = QPushButton('Botão2')
# botao5.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')


# # QGridLayout é um layout que seria como uma tabela, existem vários outros tipos e layout
# layout = QGridLayout()
# # Define qual o tipo de layout da determinada sessão da aplicação
# central_widget.setLayout(layout)

# # A função addWidget adiciona item em um layout, essa função também recebe valores
# layout.addWidget(botao3, 1, 2, 1, 1)
# # de posicionamento, após indicar o que será adicionado, o proximo parâmetro indica em qual
# layout.addWidget(botao4, 1, 1, 1, 1)
# # linha o item se posicionará, a seguir a coluna
# layout.addWidget(botao5, 3, 1, 1, 2)

# # Barra de Status
# status_bar = window.statusBar()
# status_bar.showMessage('Barra de Status')


# @Slot  # type: ignore
# def exemplo_acao(status_bar):
#     def inner():
#         status_bar.showMessage('O slot foi executado')
#     return inner


# @Slot  # type: ignore
# def segundo_slot(checked):
#     print('Slot Está marcado', checked)


# @Slot  # type: ignore
# def terceiro_slot(action):
#     def inner():
#         segundo_slot(action.isChecked())
#     return inner


# # MenuBar
# menu = window.menuBar()
# primeiro_menu = menu.addMenu('Primeiro Menu')
# acao = primeiro_menu.addAction('Primeira Ação')
# acao.triggered.connect(exemplo_acao(status_bar))  # type: ignore

# acao2 = primeiro_menu.addAction('Segunda Ação')
# acao2.setCheckable(True)
# # acao2.triggered.connect(lambda: exemplo_acao(status_bar))
# acao2.toggled.connect(segundo_slot)
# acao2.hovered.connect(terceiro_slot(acao2))  # type: ignore

# botao3.clicked.connect(terceiro_slot(acao2))  # type: ignore

# window.show()
# app1.exec()
# --------------------------------------------------------------------------------------------------------------------------------

"""
Trabalhando com classes e heranças
"""

app2 = QApplication()


# Podemos herdar outras classes e termos a nossa própria classe para poder ter mais controle e mais organização da aplicação
class MyWindow(QMainWindow):  # Classe própria MyWindow que herda os atributos da classe do PySide6 QMainWIndow
    def __init__(self, parent=None):  # Definindo o método construtor init
        super().__init__(parent)  # Chama o método contrutor da classe herdada(QMainWIndow)

        self.central_widget = QWidget()  # Criamos nossa Widget que é onde haverá os requisitos de interação do usúario

        self.setCentralWidget(self.central_widget)  # Definimos qual o widget que será usado na tela principal
        self.setWindowTitle('Meu primeiro programa')   # Define um título para a janela

        self.botao3 = self.make_btn('Marieli Amor da Minha Vida')  # Usa a função criada abaixo para criar um botão
        self.botao3.clicked.connect(self.segundo_slot)  # type: ignore  # Conecta o botão ao slot

        self.botao4 = self.make_btn('Botão')

        self.botao5 = self.make_btn('Botão2')

        self.Mylayout = QGridLayout()  # Define o tipo do layout, nesse caso usamos o layout tipo grid
        self.central_widget.setLayout(self.Mylayout)  # Indica para o widget qual o layout que se posicionaram

        self.Mylayout.addWidget(self.botao3, 1, 2, 1, 1)  # Adiciona algo ao layout, o primeiro parâmetor é o que será adicionado
        self.Mylayout.addWidget(self.botao4, 1, 1, 1, 1)  # No caso é passada a variável do botão e a seguir é o posicionamento
        self.Mylayout.addWidget(self.botao5, 3, 1, 1, 2)  # Linha, Coluna, quantidade de linhas ocupadas e quantidade de colunas

        # Barra de Status - Abaixo cria e configura a barra de status
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Barra de Status')

        # MenuBar - Cria e configura a barra de menu
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro Menu')  # Cria a aba
        self.acao = self.primeiro_menu.addAction('Primeira Ação')  # Cria a primeira opção de ação da aba criada acima
        self.acao.triggered.connect(self.exemplo_acao)  # type: ignore  #  Conecta ela ao slot

        self.acao2 = self.primeiro_menu.addAction('Segunda Ação')  # Cria a segunda opção de ação da aba
        self.acao2.setCheckable(True)  # Define ela como um botão de checagem, ou seja, ao ser clicado mostrada um sinal de oky
        self.acao2.toggled.connect(self.segundo_slot)  # type: ignore  # Conecta ao slot
        self.acao2.hovered.connect(self.segundo_slot)  # type: ignore Executa o slot apenas passando o mouse sem clicar

    @Slot()  # Indica que isso é um slot
    def exemplo_acao(self):  # Slot que mostra mensagem na barra de status
        self.status_bar.showMessage('O slot foi executado')

    @Slot()
    def segundo_slot(self):  # Slot que informa se a segunda opção do menu está checado ou não
        print('Slot Está marcado', self.acao2.isChecked())

    def make_btn(self, text):  # Isso é a função que cria o botão
        btn = QPushButton(text)  # Define a variável como tipo botão que recebe um texto como parâmetro
        btn.setStyleSheet(  # Personaliza o botão com comando CSS
            'font-size: 40px; color: Pink; background-color: blue')
        return btn


window = MyWindow()
window.show()
app2.exec()
