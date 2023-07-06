# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 548)
        MainWindow.setStyleSheet(u"background-color: #4B0082;\n"
"font-family: Roboto LT;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lb_loader = QLabel(self.balance_frame)
        self.lb_loader.setObjectName(u"lb_loader")
        self.lb_loader.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_loader)

        self.lb_total = QLabel(self.balance_frame)
        self.lb_total.setObjectName(u"lb_total")
        self.lb_total.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_total)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.balance_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(24, 16777215))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_3.setPixmap(QPixmap(u":/icon/icon/local_shipping_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.balance_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_total_min = QLabel(self.balance_frame)
        self.lb_total_min.setObjectName(u"lb_total_min")
        self.lb_total_min.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_total_min)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.balance_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(24, 16777215))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_6.setPixmap(QPixmap(u":/icon/icon/local_shipping_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.balance_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_total_max = QLabel(self.balance_frame)
        self.lb_total_max.setObjectName(u"lb_total_max")
        self.lb_total_max.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_total_max)


        self.horizontalLayout_5.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_9 = QLabel(self.categories_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-bottom: 42px;\n"
"")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.categories_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(24, 16777215))
        self.label_13.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"")
        self.label_13.setPixmap(QPixmap(u":/icon/icon/person_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_11 = QLabel(self.categories_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lb_personally_v = QLabel(self.categories_frame)
        self.lb_personally_v.setObjectName(u"lb_personally_v")
        self.lb_personally_v.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_3.addWidget(self.lb_personally_v)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.categories_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(24, 16777215))
        self.label_10.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_10.setPixmap(QPixmap(u":/icon/icon/person_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_14 = QLabel(self.categories_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.lb_personally_sh = QLabel(self.categories_frame)
        self.lb_personally_sh.setObjectName(u"lb_personally_sh")
        self.lb_personally_sh.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.lb_personally_sh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_pl_load = QPushButton(self.centralwidget)
        self.bt_pl_load.setObjectName(u"bt_pl_load")
        self.bt_pl_load.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:  rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:  rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pl_load.setIcon(icon)
        self.bt_pl_load.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.bt_pl_load)

        self.btn_pl_edit = QPushButton(self.centralwidget)
        self.btn_pl_edit.setObjectName(u"btn_pl_edit")
        self.btn_pl_edit.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:  rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:  rgba(255,255,255,70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pl_edit.setIcon(icon1)
        self.btn_pl_edit.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_pl_edit)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:  rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:  rgba(255,255,255,70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255, 30);\n"
"border: 1px solid rgba(255,255,255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"background-color: rgba(53,53,53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255, 50)\n"
"}\n"
"QTableView:item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255, 50);\n"
"}\n"
"\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plate loader", None))
        self.lb_loader.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0433\u0440\u0443\u0436\u0435\u043d\u043e", None))
        self.lb_total.setText(QCoreApplication.translate("MainWindow", u"250 \u0448\u0442", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041f 1.2", None))
        self.lb_total_min.setText(QCoreApplication.translate("MainWindow", u"250 \u0448\u0442", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041f 1.5", None))
        self.lb_total_max.setText(QCoreApplication.translate("MainWindow", u"250 \u0448\u0442", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_13.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0441\u0438\u043b\u044c\u0447\u0435\u043d\u043a\u043e", None))
        self.lb_personally_v.setText(QCoreApplication.translate("MainWindow", u"150 \u0448\u0442", None))
        self.label_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u043f\u043e\u0432\u0441\u043a\u0438\u0439", None))
        self.lb_personally_sh.setText(QCoreApplication.translate("MainWindow", u"150 \u0448\u0442", None))
        self.bt_pl_load.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_pl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

