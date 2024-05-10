# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 679)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.connectionLabel = QLabel(self.centralwidget)
        self.connectionLabel.setObjectName(u"connectionLabel")

        self.verticalLayout.addWidget(self.connectionLabel)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.button_time_reset = QPushButton(self.tab)
        self.button_time_reset.setObjectName(u"button_time_reset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_time_reset.sizePolicy().hasHeightForWidth())
        self.button_time_reset.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_time_reset, 4, 0, 1, 1)

        self.button_save_s = QPushButton(self.tab)
        self.button_save_s.setObjectName(u"button_save_s")

        self.gridLayout.addWidget(self.button_save_s, 3, 0, 1, 1)

        self.table_1 = QTableView(self.tab)
        self.table_1.setObjectName(u"table_1")

        self.gridLayout.addWidget(self.table_1, 2, 1, 1, 1)

        self.table_0 = QTableView(self.tab)
        self.table_0.setObjectName(u"table_0")
        self.table_0.setAutoScroll(True)

        self.gridLayout.addWidget(self.table_0, 2, 0, 1, 1)

        self.button_save_d = QPushButton(self.tab)
        self.button_save_d.setObjectName(u"button_save_d")

        self.gridLayout.addWidget(self.button_save_d, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.layout_intervals = QHBoxLayout()
        self.layout_intervals.setObjectName(u"layout_intervals")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_v0 = QLabel(self.tab_2)
        self.label_v0.setObjectName(u"label_v0")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_v0.setFont(font)

        self.verticalLayout_2.addWidget(self.label_v0)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.value_0_counter = QLCDNumber(self.tab_2)
        self.value_0_counter.setObjectName(u"value_0_counter")
        self.value_0_counter.setDigitCount(3)
        self.value_0_counter.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_2.addWidget(self.value_0_counter)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.value_0_time_up = QLabel(self.tab_2)
        self.value_0_time_up.setObjectName(u"value_0_time_up")
        self.value_0_time_up.setFont(font)

        self.verticalLayout_2.addWidget(self.value_0_time_up)

        self.value_0_time_down = QLabel(self.tab_2)
        self.value_0_time_down.setObjectName(u"value_0_time_down")
        self.value_0_time_down.setFont(font)

        self.verticalLayout_2.addWidget(self.value_0_time_down)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.value_0_interval_up_front = QLabel(self.tab_2)
        self.value_0_interval_up_front.setObjectName(u"value_0_interval_up_front")
        self.value_0_interval_up_front.setFont(font)

        self.verticalLayout_2.addWidget(self.value_0_interval_up_front)

        self.value_0_interval_down_front = QLabel(self.tab_2)
        self.value_0_interval_down_front.setObjectName(u"value_0_interval_down_front")
        self.value_0_interval_down_front.setFont(font)

        self.verticalLayout_2.addWidget(self.value_0_interval_down_front)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_v1 = QLabel(self.tab_2)
        self.label_v1.setObjectName(u"label_v1")
        self.label_v1.setFont(font)

        self.verticalLayout_4.addWidget(self.label_v1)

        self.label1 = QLabel(self.tab_2)
        self.label1.setObjectName(u"label1")

        self.verticalLayout_4.addWidget(self.label1)

        self.value_1_counter = QLCDNumber(self.tab_2)
        self.value_1_counter.setObjectName(u"value_1_counter")
        self.value_1_counter.setDigitCount(3)
        self.value_1_counter.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_4.addWidget(self.value_1_counter)

        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_4.addWidget(self.label_21)

        self.value_1_time_up = QLabel(self.tab_2)
        self.value_1_time_up.setObjectName(u"value_1_time_up")
        self.value_1_time_up.setFont(font)

        self.verticalLayout_4.addWidget(self.value_1_time_up)

        self.value_1_time_down = QLabel(self.tab_2)
        self.value_1_time_down.setObjectName(u"value_1_time_down")
        self.value_1_time_down.setFont(font)

        self.verticalLayout_4.addWidget(self.value_1_time_down)

        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_4.addWidget(self.label_41)

        self.value_1_interval_up_front = QLabel(self.tab_2)
        self.value_1_interval_up_front.setObjectName(u"value_1_interval_up_front")
        self.value_1_interval_up_front.setFont(font)

        self.verticalLayout_4.addWidget(self.value_1_interval_up_front)

        self.value_1_interval_down_front = QLabel(self.tab_2)
        self.value_1_interval_down_front.setObjectName(u"value_1_interval_down_front")
        self.value_1_interval_down_front.setFont(font)

        self.verticalLayout_4.addWidget(self.value_1_interval_down_front)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.layout_intervals.addLayout(self.verticalLayout_3)

        self.table_cnts = QTableView(self.tab_2)
        self.table_cnts.setObjectName(u"table_cnts")
        self.table_cnts.setAutoScroll(True)

        self.layout_intervals.addWidget(self.table_cnts)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_add = QPushButton(self.tab_2)
        self.button_add.setObjectName(u"button_add")
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.button_add)

        self.button_save_t = QPushButton(self.tab_2)
        self.button_save_t.setObjectName(u"button_save_t")

        self.verticalLayout_7.addWidget(self.button_save_t)


        self.layout_intervals.addLayout(self.verticalLayout_7)


        self.gridLayout_4.addLayout(self.layout_intervals, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WiLAB ITMO", None))
        self.connectionLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0435 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u0440\u043e\u0442", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u0435 1 -> 2", None))
        self.button_time_reset.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u0443\u043b\u0438\u0442\u044c \u0447\u0430\u0441\u044b [Backspace]", None))
#if QT_CONFIG(shortcut)
        self.button_time_reset.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.button_save_s.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.button_save_d.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c", None))
        self.label_v0.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0440\u043e\u0442\u0430 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0435\u0442\u0447\u0438\u043a \u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (1 \u0438 0)", None))
        self.value_0_time_up.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_0_time_down.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443, \u043f\u043e \u0441\u043f\u0430\u0434\u0443, \u0441.", None))
        self.value_0_interval_up_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_0_interval_down_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_v1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0440\u043e\u0442\u0430 2", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0435\u0442\u0447\u0438\u043a \u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (1 \u0438 0)", None))
        self.value_1_time_up.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_1_time_down.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b (\u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443, \u043f\u043e \u0441\u043f\u0430\u0434\u0443)", None))
        self.value_1_interval_up_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_1_interval_down_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c [Enter]", None))
#if QT_CONFIG(shortcut)
        self.button_add.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.button_save_t.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
    # retranslateUi

