from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from var import MEDIUM_FONT_SIZE
from util import inNumOrDot, validNumber
# from typing import TYPE_CHECKING
from display import Display, Info
import math  # https://docs.python.org/pt-br/3/library/math.html
from m_window import MainWindow


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
    def __init__(self, tela: Display, info: Info, window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['%', 'CE', 'C', '◀'],
            ['¹/x', '^', '²√x', '÷'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
        ]
        self.display = tela
        self.info = info
        self.window = window
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

        if text in '+-*÷^':
            self._connectClicked(button, self.connectBtn(
                self._operatorClick, button))

        # if text == '÷':
        #     text = '/'
        #     self._connectClicked(button, self.connectBtn(
        #         self._operatorClick, button))

        if text in '=':
            self._connectClicked(button, self._vle)

        if text in '◀':
            self._connectClicked(button, self.display.backspace)

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

        # if text == '÷':
        #     text = '/'

        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem digitar nenhum número não faz nada
        if not validNumber(displayText) and self._leftValue is None:
            self._showError('Você não digitou nada')
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
        result = 'Erro'

        try:
            if '÷' in self.value:
                result = eval(self.value.replace('÷', '/'))
            if '^' in self.value and isinstance(self._leftValue, float):
                result = math.pow(self._leftValue, self._rightValue)
            else:
                result = eval(self.value)
        except ZeroDivisionError:
            self._showError('Impossivel Dividir por 0')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada')

        self.display.clear()
        self.info.setText(f'{self.value} = {result}')
        self._leftValue = result
        self._rightValue = None

        if result == 'Erro':
            self._leftValue = None

    def _showError(self, error):
        msgBox = self.window.msgBox()
        msgBox.setText(error)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel)

        result = msgBox.exec()

        if result == msgBox.StandardButton.Ok:
            print('Usuário digitou OK')
        elif result == msgBox.StandardButton.Cancel:
            print('Usuário Cancelou')
        msgBox.exec()
