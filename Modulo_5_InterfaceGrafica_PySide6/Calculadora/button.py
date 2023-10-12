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
            ['±', '0', '.', '='],
        ]
        self.display = tela
        self.info = info
        self._getValue = ''
        self._getValueInitial = 'Sua conta'
        self._leftValue = None
        self._rightValue = None
        self._opValue = None

        self.value = self._getValueInitial
        self._makeGrid()

    @property
    def value(self):
        return self._getValue

    @value.setter
    def value(self, valor):
        self._getValue = valor
        self.info.setText(valor)

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, btn_txt in enumerate(row):
                btn = Button(btn_txt)

                # if btn_txt not in '0123456789.±':
                if not inNumOrDot(btn_txt):
                    btn.setProperty('cssClass', 'specialButton')
                    self._configSpecialBtn(btn)

                self.addWidget(btn, i, j)
                btnSlot = self.connectBtn(self.clickBtn, btn)
                self._connectClicked(btn, btnSlot)

    def _connectClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialBtn(self, button):
        text = button.text()

        if text == 'C':
            # button.clicked.connect(self.display.clear)
            self._connectClicked(button, self._clear)
            # self._connectClicked(button, cleaning)

        if text in '+-/*':
            self._connectClicked(button, self.connectBtn(
                self._operatorClick, button))

        if text in '=':
            self._connectClicked(button, self._vle)

    def connectBtn(self, func, *args, **kwargs):
        @ Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def clickBtn(self, btn):
        button_text = btn.text()
        new_value = self.display.text() + button_text

        if not validNumber(new_value):
            return

        self.display.insert(button_text)

    def _clear(self):
        self._leftValue = None
        self._rightValue = None
        self._opValue = None
        self.value = self._getValueInitial
        self.display.clear()

    def _operatorClick(self, button):
        text = button.text()  # +-/*
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem digitar nenhum número não faz nada
        if not validNumber(displayText) and self._leftValue is None:
            return

        if self._leftValue is None:
            self._leftValue = float(displayText)

        self._opValue = text
        self.value = f'{self._leftValue} {self._opValue} ??'

    def _vle(self):
        displayText = self.display.text()

        if not validNumber(displayText):
            return

        # if self._rightValue is None:
        self._rightValue = float(displayText)
        self.value = f'{self._leftValue} {self._opValue} {self._rightValue}'
        result = 0.0

        try:
            result = eval(self.value)
        except ZeroDivisionError:
            print('Impossivel Dividir por 0')

        self.display.clear()
        self.info.setText(f'{self.value} = {result}')
        self._leftValue = result
        self._rightValue = None
