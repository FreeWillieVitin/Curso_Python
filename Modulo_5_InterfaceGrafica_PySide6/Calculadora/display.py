from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit, QLabel
from var import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE, TEXT_MARGIN, MIN_WIDTH
from PySide6.QtCore import Qt, Signal
from util import isEmpty, inNumOrDot


class Display(QLineEdit):
    sigCalc = Signal()
    sigDel = Signal()
    sigClear = Signal()
    sigNum = Signal()
    inputPress = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MIN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(15, 7, 15, 7)  # que é a mesma coisa que [TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, ]

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        # isNumber = key in [KEYS.Key_0, KEYS.Key_1, KEYS.Key_2, KEYS.Key_3, KEYS.Key_4, KEYS.Key_5,
        #                    KEYS.Key_6, KEYS.Key_7, KEYS.Key_8, KEYS.Key_9]
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]

        if isEnter or text == '=':
            self.sigCalc.emit()
            return event.ignore()

        if isDelete or text.lower() == 'd':
            self.sigDel.emit()
            return event.ignore()

        if isEsc or text.lower() == 'c':
            self.sigClear.emit()
            return event.ignore()

        # if isNumber:
        #     self.sigNum.emit()
        #     return super().keyPressEvent(event)

        if isEmpty(text):
            return event.ignore()

        if inNumOrDot(text):
            print(
                'inputPressed pressionado, sinal emitido', type(self).__name__
            )
            self.inputPress.emit(text)
            return event.ignore()


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configInfo()

    def configInfo(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
