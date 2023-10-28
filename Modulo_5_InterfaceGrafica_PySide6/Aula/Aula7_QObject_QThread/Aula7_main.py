# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Aula7_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_MyObject(object):
    def setupUi(self, MyObject):
        if not MyObject.objectName():
            MyObject.setObjectName(u"MyObject")
        MyObject.resize(915, 657)
        self.horizontalLayout = QHBoxLayout(MyObject)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(MyObject)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(MyObject)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn1 = QPushButton(MyObject)
        self.btn1.setObjectName(u"btn1")
        font1 = QFont()
        font1.setPointSize(15)
        self.btn1.setFont(font1)

        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)

        self.btn2 = QPushButton(MyObject)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setFont(font1)

        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(MyObject)

        QMetaObject.connectSlotsByName(MyObject)
    # setupUi

    def retranslateUi(self, MyObject):
        MyObject.setWindowTitle(QCoreApplication.translate("MyObject", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MyObject", u"L2", None))
        self.label.setText(QCoreApplication.translate("MyObject", u"L1", None))
        self.btn1.setText(QCoreApplication.translate("MyObject", u"B1", None))
        self.btn2.setText(QCoreApplication.translate("MyObject", u"B2", None))
    # retranslateUi

