from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from var import MEDIUM_FONT_SIZE
from util import inNumOrDot, validNumber
# from typing import TYPE_CHECKING
from display import Display, Info


class Button(QPushButton):
    def __init__(self, text: str, *args, **kwargs) -> None:
        super().__init__(text, *args, **kwargs)
        self.configStyle()
        self.nome = text

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True)
        # font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(30, 30)
        # self.setProperty('cssClass', 'specialButton')


class ButtonGrid(QGridLayout):
    def __init__(self, tela: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['%', 'CE', 'C', '◀'],
            ['¹/x', 'x²', '²√x', '÷'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±',  '0', '.', '='],
        ]
        self.display = tela
        self.info = info
        self._getValue = ''
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, btn_txt in enumerate(row):
                btn = Button(btn_txt)

                # if btn_txt not in '0123456789.±':
                if not inNumOrDot(btn_txt):
                    btn.setProperty('cssClass', 'specialButton')

                self.addWidget(btn, i, j)
                btnSlot = self.connectBtn(self.clickBtn, btn)
                btn.clicked.connect(btnSlot)

    def _connectClicked(self, button, slot):
        

    @property
    def conta(self):
        return self.conta

    @conta.setter
    def conta(self, valor):
        self._getValue = valor
        self.info.setText(valor)
      
    def connectBtn(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def clickBtn(self, btn):
        button_text = btn.text()
        new_value = self.display.text() + button_text

        if not validNumber(new_value):
            return

        self.display.insert(button_text)
