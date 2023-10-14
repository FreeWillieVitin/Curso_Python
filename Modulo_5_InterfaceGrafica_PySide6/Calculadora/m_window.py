from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon
from var import ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central = QWidget()
        self.vLayout = QVBoxLayout()
        self.icon = QIcon(str(ICON_PATH))

        self.setCentralWidget(self.central)
        self.central.setLayout(self.vLayout)
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(325, 425)

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def msgBox(self):
        return QMessageBox(self)
