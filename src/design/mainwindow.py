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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 751, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.connectionLabel = QLabel(self.verticalLayoutWidget)
        self.connectionLabel.setObjectName(u"connectionLabel")

        self.verticalLayout.addWidget(self.connectionLabel)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 721, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.table_1 = QTableView(self.gridLayoutWidget)
        self.table_1.setObjectName(u"table_1")

        self.gridLayout.addWidget(self.table_1, 2, 1, 1, 1)

        self.button_time_reset = QPushButton(self.gridLayoutWidget)
        self.button_time_reset.setObjectName(u"button_time_reset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_time_reset.sizePolicy().hasHeightForWidth())
        self.button_time_reset.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_time_reset, 3, 0, 1, 1)

        self.table_0 = QTableView(self.gridLayoutWidget)
        self.table_0.setObjectName(u"table_0")
        self.table_0.setAutoScroll(True)

        self.gridLayout.addWidget(self.table_0, 2, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 711, 471))
        self.layout_intervals = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_intervals.setObjectName(u"layout_intervals")
        self.layout_intervals.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.value_0_counter = QLCDNumber(self.horizontalLayoutWidget)
        self.value_0_counter.setObjectName(u"value_0_counter")
        self.value_0_counter.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_2.addWidget(self.value_0_counter)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.value_0_time_up = QLCDNumber(self.horizontalLayoutWidget)
        self.value_0_time_up.setObjectName(u"value_0_time_up")

        self.verticalLayout_2.addWidget(self.value_0_time_up)

        self.value_0_time_down = QLCDNumber(self.horizontalLayoutWidget)
        self.value_0_time_down.setObjectName(u"value_0_time_down")

        self.verticalLayout_2.addWidget(self.value_0_time_down)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.value_0_interval_up_front = QLCDNumber(self.horizontalLayoutWidget)
        self.value_0_interval_up_front.setObjectName(u"value_0_interval_up_front")

        self.verticalLayout_2.addWidget(self.value_0_interval_up_front)

        self.value_0_interval_down_front = QLCDNumber(self.horizontalLayoutWidget)
        self.value_0_interval_down_front.setObjectName(u"value_0_interval_down_front")

        self.verticalLayout_2.addWidget(self.value_0_interval_down_front)


        self.layout_intervals.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WiLAB ITMO", None))
        self.connectionLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_time_reset.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u0443\u043b\u0438\u0442\u044c \u0447\u0430\u0441\u044b [Backspace]", None))
#if QT_CONFIG(shortcut)
        self.button_time_reset.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u0440\u043e\u0442 \u043d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f 1 -> 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
    # retranslateUi

