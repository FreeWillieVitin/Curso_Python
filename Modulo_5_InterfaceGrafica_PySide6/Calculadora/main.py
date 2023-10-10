from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidgetAction
from m_window import MainWindow
from display import Display, Info
from PySide6.QtGui import QIcon
from button import Button, ButtonGrid
from var import ICON_PATH
from style import setupTheme
import ctypes

if __name__ == '__main__':
    calcApp = QApplication()
    window = MainWindow()
    display = Display()
    btnGrid = ButtonGrid()
    info = Info()
    setupTheme('dark')

# Display da calculadora
    menu = window.menuBar()
    styleLayout = menu.addMenu('Estilo')
    escolheCor1 = styleLayout.addAction('Dark')
    escolheCor1.triggered.connect(lambda: setupTheme('dark'))
    escolheCor2 = styleLayout.addAction('Light')
    escolheCor2.triggered.connect(lambda: setupTheme('light'))

    # txt = QLabel('Texto')
    # txt.setStyleSheet('font-size: 20px;')

    # window.addWidgetToVLayout(txt)
    window.addWidgetToVLayout(info)
    window.addWidgetToVLayout(display)
    window.vLayout.addLayout(btnGrid)
    display.setPlaceholderText('Números Aqui')
    # window.addWidgetToVLayout(Display('Display 2'))
    # window.addWidgetToVLayout(Display('Display 3'))

    # btnGrid.addWidget(Button('%'), 0, 0)
    # btnGrid.addWidget(Button('CE'), 0, 1)
    # btnGrid.addWidget(Button('C'), 0, 2)
    # btnGrid.addWidget(Button('<'), 0, 3)

    # btnGrid.addWidget(Button('¹/x'), 1, 0)
    # btnGrid.addWidget(Button('x²'), 1, 1)
    # btnGrid.addWidget(Button('²√x'), 1, 2)
    # btnGrid.addWidget(Button('÷'), 1, 3)

    # btnGrid.addWidget(Button('7'), 2, 0)
    # btnGrid.addWidget(Button('8'), 2, 1)
    # btnGrid.addWidget(Button('9'), 2, 2)
    # btnGrid.addWidget(Button('X'), 2, 3)

    # btnGrid.addWidget(Button('4'), 3, 0)
    # btnGrid.addWidget(Button('5'), 3, 1)
    # btnGrid.addWidget(Button('6'), 3, 2)
    # btnGrid.addWidget(Button('-'), 3, 3)

    # btnGrid.addWidget(Button('1'), 4, 0)
    # btnGrid.addWidget(Button('2'), 4, 1)
    # btnGrid.addWidget(Button('3'), 4, 2)
    # btnGrid.addWidget(Button('+'), 4, 3)

    # btnGrid.addWidget(Button('±'), 5, 0)
    # btnGrid.addWidget(Button('0'), 5, 1)
    # btnGrid.addWidget(Button(','), 5, 2)
    # btnGrid.addWidget(Button('='), 5, 3)

    calcApp.setWindowIcon(QIcon(str(ICON_PATH)))

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    window.adjustFixedSize()
    window.show()
    calcApp.exec_()
