from typing import Optional
import PySide6.QtCore
from Aula6_QT_Designer_UI import Ui_PrimeiraJanela
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_PrimeiraJanela):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
