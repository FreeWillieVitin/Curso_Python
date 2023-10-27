from typing import Optional, cast
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import QObject, QEvent
from Aula6_QT_Designer_UI import Ui_PrimeiraJanela
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_PrimeiraJanela):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.btn.clicked.connect(self.changeMainLabel)

        self.LineName.installEventFilter(self)

    def changeMainLabel(self):
        text = self.LineName.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            # text = self.LineName.text()
            # self.labelResult.setText(text + event.text())
            print(event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
