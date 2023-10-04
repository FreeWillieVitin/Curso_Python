from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from m_window import MainWindow
from display import Display, Info
from PySide6.QtGui import QIcon
from var import ICON_PATH
from style import setupTheme
import ctypes

if __name__ == '__main__':
    calcApp = QApplication()
    window = MainWindow()
    display = Display()
    info = Info()
    setupTheme('light')

    menu = window.menuBar()
    styleLayout = menu.addMenu('Estilo')
    escolheCor1 = styleLayout.addAction('Dark')
    escolheCor1.setCheckable(True)
    escolheCor1.triggered.connect(setupTheme('dark'))
    escolheCor2 = styleLayout.addAction('Light')
    escolheCor2.setCheckable(True)
    escolheCor2.triggered.connect(setupTheme('light'))

    # escolheCor2 = styleLayout.addMenu('Light')

    # self.acao2.toggled.connect(self.segundo_slot)  # type: ignore
    # self.acao2.hovered.connect(self.segundo_slot)

    # txt = QLabel('Texto')
    # txt.setStyleSheet('font-size: 20px;')

    # window.addWidgetToVLayout(txt)
    window.addWidgetToVLayout(info)
    window.addWidgetToVLayout(display)
    display.setPlaceholderText('Números Aqui')
    # window.addWidgetToVLayout(Display('Display 2'))
    # window.addWidgetToVLayout(Display('Display 3'))

    calcApp.setWindowIcon(QIcon(str(ICON_PATH)))

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    window.adjustFixedSize()
    window.show()
    calcApp.exec_()
