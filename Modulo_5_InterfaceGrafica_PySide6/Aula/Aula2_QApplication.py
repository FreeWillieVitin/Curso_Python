"""
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6
"""
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow

# app = QApplication()

# # Exibe um botão na tela com um texto dentro
# botao = QPushButton('Marieli Amor da Minha Vida')
# # Estiliza o botão usando comandos CSS
# botao.setStyleSheet('font-size: 40px; color: Pink; background-color: blue')
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

app1 = QApplication()  # Indica um inicializador de aplicação para a variável
window = QMainWindow()  # Cria a tela principal e armazena na variável
# O QWidget seria como um formulário onde é posicionado os itens e exibido ao usuário
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Meu primeiro programa')  # Define o Título para a janela

botao3 = QPushButton('Marieli Amor da Minha Vida')  # Classe onde fica a estrutura de um botão
# No método setStyleSheet é personalizado o botão utilizando comandos CSS
botao3.setStyleSheet('font-size: 40px; color: Pink; background-color: blue')

botao4 = QPushButton('Botão')
botao4.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')

botao5 = QPushButton('Botão2')
botao5.setStyleSheet('font-size: 20px; color: Pink; background-color: blue')


# QGridLayout é um layout que seria como uma tabela, existem vários outros tipos e layout
layout = QGridLayout()
# Define qual o tipo de layout da determinada sessão da aplicação
central_widget.setLayout(layout)

# A função addWidget adiciona item em um layout, essa função também recebe valores
layout.addWidget(botao3, 1, 2, 1, 1)
# de posicionamento, após indicar o que será adicionado, o proximo parâmetro indica em qual
layout.addWidget(botao4, 1, 1, 1, 1)
# linha o item se posicionará, a seguir a coluna
layout.addWidget(botao5, 3, 1, 1, 2)

# Barra de Status
status_bar = window.statusBar()
status_bar.showMessage('Barra de Status')  # Exibe um texto fixo na barra de status


# O que temos abaixo é um slot, slot são métodos ou funções que são que é chamado em resposta a um Signal, basicamente são ações
# que o sistema irá executar, no caso abaixo, quando o botão for clicado, a ação de mudar a mensagem da barra de status executará
def exemplo_acao(status_bar):
    status_bar.showMessage('O slot foi executado')


# MenuBar
# Adiciona uma barra de menu na QMainWindow
menu = window.menuBar()
# E dentro do menuBar usamos a função add menu para adicionar abas nele
primeiro_menu = menu.addMenu('Primeiro Menu')
# A função addAction cria um tipo de botão/aba do menu está lá como uma abinha, porém pode executar alguma ação.
acao = primeiro_menu.addAction('Primeira Ação')
# Nesse caso ela irá disparar a ação que foi criada para o slot logo mais acima
acao.triggered.connect(lambda: exemplo_acao(status_bar))

window.show()
app1.exec()
