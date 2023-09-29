from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from m_window import MainWindow


if __name__ == '__main__':
    calcApp = QApplication()
    window = MainWindow()

    txt = QLabel('Texto')

    txt.setStyleSheet('font-size: 20px;')

    window.v_lt.addWidget(txt)
    window.adjustFixedSize()

    window.show()
    calcApp.exec()
