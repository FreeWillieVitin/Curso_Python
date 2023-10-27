# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Aula6_QT_Designer_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_PrimeiraJanela(object):
    def setupUi(self, PrimeiraJanela):
        if not PrimeiraJanela.objectName():
            PrimeiraJanela.setObjectName(u"PrimeiraJanela")
        PrimeiraJanela.resize(795, 660)
        self.centralwidget = QWidget(PrimeiraJanela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName(u"labelResult")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1)

        self.GridName = QGridLayout()
        self.GridName.setObjectName(u"GridName")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.GridName.addWidget(self.label, 0, 0, 1, 1)

        self.LineName = QLineEdit(self.centralwidget)
        self.LineName.setObjectName(u"LineName")

        self.GridName.addWidget(self.LineName, 0, 1, 1, 1)

        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.btn.setFont(font2)

        self.GridName.addWidget(self.btn, 0, 2, 1, 1)

        self.gridLayout.addLayout(self.GridName, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        PrimeiraJanela.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PrimeiraJanela)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 22))
        PrimeiraJanela.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PrimeiraJanela)
        self.statusbar.setObjectName(u"statusbar")
        PrimeiraJanela.setStatusBar(self.statusbar)

        self.retranslateUi(PrimeiraJanela)

        QMetaObject.connectSlotsByName(PrimeiraJanela)
    # setupUi

    def retranslateUi(self, PrimeiraJanela):
        PrimeiraJanela.setWindowTitle(QCoreApplication.translate("PrimeiraJanela", u"Primeira Janela", None))
        self.labelResult.setText(QCoreApplication.translate("PrimeiraJanela", u"Hello World!!!", None))
        self.label.setText(QCoreApplication.translate("PrimeiraJanela", u"Seu Nome:", None))
        self.LineName.setPlaceholderText(QCoreApplication.translate("PrimeiraJanela", u"Digite Seu Nome Aqui", None))
        self.btn.setText(QCoreApplication.translate("PrimeiraJanela", u"Enviar", None))
    # retranslateUi
