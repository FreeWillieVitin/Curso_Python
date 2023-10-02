from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from m_window import MainWindow
from display import Display
from PySide6.QtGui import QIcon
from var import ICON_PATH
import ctypes

if __name__ == '__main__':
    calcApp = QApplication()
    window = MainWindow()
    display = Display()
    # txt = QLabel('Texto')

    # txt.setStyleSheet('font-size: 20px;')

    # window.addWidgetToVLayout(txt)
    window.addWidgetToVLayout(display)
    window.adjustFixedSize()
    calcApp.setWindowIcon(QIcon(str(ICON_PATH)))

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    window.show()
    calcApp.exec_()
