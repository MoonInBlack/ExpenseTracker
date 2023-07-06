# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 506)
        Dialog.setStyleSheet(u"background-color: #4B0082;\n"
"font-family: Roboto LT;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_equipment = QLabel(self.frame)
        self.lb_equipment.setObjectName(u"lb_equipment")
        self.lb_equipment.setMaximumSize(QSize(16777215, 100))
        self.lb_equipment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lb_equipment.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_equipment)

        self.cb_responsible = QComboBox(self.frame)
        self.cb_responsible.addItem("")
        self.cb_responsible.addItem("")
        self.cb_responsible.setObjectName(u"cb_responsible")
        self.cb_responsible.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_responsible.setStyleSheet(u"QComboBox {\n"
"color: white;\n"
"font-size: 10pt;\n"
"font-weight: bold;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background: #9370DB;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"\n"
"color: white; \n"
"background-color: #4B0082;\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.cb_responsible)

        self.cb_nomenclature = QComboBox(self.frame)
        self.cb_nomenclature.addItem("")
        self.cb_nomenclature.addItem("")
        self.cb_nomenclature.setObjectName(u"cb_nomenclature")
        self.cb_nomenclature.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_nomenclature.setStyleSheet(u"QComboBox {\n"
"color: white;\n"
"font-size: 10pt;\n"
"font-weight: bold;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background: #9370DB;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"color: white; \n"
"background-color: #4B0082;\n"
"}")

        self.verticalLayout.addWidget(self.cb_nomenclature)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: #FFFF00;\n"
"padding-left: 10px;\n"
"")

        self.horizontalLayout.addWidget(self.label_6)

        self.shippt_date = QDateEdit(self.frame)
        self.shippt_date.setObjectName(u"shippt_date")
        self.shippt_date.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;")
        self.shippt_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.shippt_date.setDate(QDate(2023, 1, 1))

        self.horizontalLayout.addWidget(self.shippt_date)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_order_number = QLineEdit(self.frame)
        self.le_order_number.setObjectName(u"le_order_number")
        self.le_order_number.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.horizontalLayout_2.addWidget(self.le_order_number)

        self.date_order_number = QDateEdit(self.frame)
        self.date_order_number.setObjectName(u"date_order_number")
        self.date_order_number.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;")
        self.date_order_number.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_order_number.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_2.addWidget(self.date_order_number)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_number_equipment = QLineEdit(self.frame)
        self.le_number_equipment.setObjectName(u"le_number_equipment")
        self.le_number_equipment.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;\n"
"margin-bottom: 20px;\n"
"")

        self.horizontalLayout_3.addWidget(self.le_number_equipment)

        self.date_equipment = QDateEdit(self.frame)
        self.date_equipment.setObjectName(u"date_equipment")
        self.date_equipment.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;\n"
"margin-bottom: 20px;")
        self.date_equipment.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_equipment.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_3.addWidget(self.date_equipment)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cb_choose_quantity = QComboBox(self.frame)
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.addItem("")
        self.cb_choose_quantity.setObjectName(u"cb_choose_quantity")
        self.cb_choose_quantity.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_choose_quantity.setStyleSheet(u"QComboBox {\n"
"color: white;\n"
"font-size: 10pt;\n"
"font-weight: bold;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background: #9370DB;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"color: white; \n"
"background-color: #4B0082;\n"
"}")

        self.horizontalLayout_5.addWidget(self.cb_choose_quantity)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.le_area_sq_m = QLineEdit(self.frame)
        self.le_area_sq_m.setObjectName(u"le_area_sq_m")
        self.le_area_sq_m.setStyleSheet(u"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: white;\n"
"padding-left: 10px;")

        self.horizontalLayout_4.addWidget(self.le_area_sq_m)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"margin-top: 10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color:  rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:  rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/save_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Equipment", None))
        self.lb_equipment.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430\u0446\u0438\u044f \u0414\u041f", None))
        self.cb_responsible.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0430\u0441\u0438\u043b\u044c\u0447\u0435\u043d\u043a\u043e \u041e.\u0421", None))
        self.cb_responsible.setItemText(1, QCoreApplication.translate("Dialog", u"\u0428\u0438\u043f\u043e\u0432\u0441\u043a\u0438\u0439 \u0415.\u0410", None))

        self.cb_responsible.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e", None))
        self.cb_nomenclature.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u041f 1.2", None))
        self.cb_nomenclature.setItemText(1, QCoreApplication.translate("Dialog", u"\u0414\u041f 1.5", None))

        self.cb_nomenclature.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0443", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043e\u0442\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.le_order_number.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u2116 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.le_number_equipment.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u2116 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430\u0446\u0438\u0438", None))
        self.cb_choose_quantity.setItemText(0, QCoreApplication.translate("Dialog", u"1 ", None))
        self.cb_choose_quantity.setItemText(1, QCoreApplication.translate("Dialog", u"2 ", None))
        self.cb_choose_quantity.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))
        self.cb_choose_quantity.setItemText(3, QCoreApplication.translate("Dialog", u"4", None))
        self.cb_choose_quantity.setItemText(4, QCoreApplication.translate("Dialog", u"5", None))
        self.cb_choose_quantity.setItemText(5, QCoreApplication.translate("Dialog", u"6", None))
        self.cb_choose_quantity.setItemText(6, QCoreApplication.translate("Dialog", u"7", None))
        self.cb_choose_quantity.setItemText(7, QCoreApplication.translate("Dialog", u"8", None))
        self.cb_choose_quantity.setItemText(8, QCoreApplication.translate("Dialog", u"9", None))
        self.cb_choose_quantity.setItemText(9, QCoreApplication.translate("Dialog", u"10", None))
        self.cb_choose_quantity.setItemText(10, QCoreApplication.translate("Dialog", u"11", None))
        self.cb_choose_quantity.setItemText(11, QCoreApplication.translate("Dialog", u"12", None))
        self.cb_choose_quantity.setItemText(12, QCoreApplication.translate("Dialog", u"13", None))
        self.cb_choose_quantity.setItemText(13, QCoreApplication.translate("Dialog", u"14", None))
        self.cb_choose_quantity.setItemText(14, QCoreApplication.translate("Dialog", u"15", None))

        self.cb_choose_quantity.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.le_area_sq_m.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043c.\u043a\u0432", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

