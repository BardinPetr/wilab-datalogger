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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")

        self.horizontalLayout_2.addWidget(self.button_clear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.connectionLabel = QLabel(self.centralwidget)
        self.connectionLabel.setObjectName(u"connectionLabel")
        font = QFont()
        font.setPointSize(14)
        self.connectionLabel.setFont(font)
        self.connectionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.connectionLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_save_s = QPushButton(self.tab)
        self.button_save_s.setObjectName(u"button_save_s")

        self.horizontalLayout_4.addWidget(self.button_save_s)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.table_0 = QTableView(self.tab)
        self.table_0.setObjectName(u"table_0")
        self.table_0.setAutoScroll(True)

        self.gridLayout.addWidget(self.table_0, 2, 0, 1, 1)

        self.table_1 = QTableView(self.tab)
        self.table_1.setObjectName(u"table_1")

        self.gridLayout.addWidget(self.table_1, 2, 1, 1, 1)

        self.on_checkbox = QCheckBox(self.tab)
        self.on_checkbox.setObjectName(u"on_checkbox")

        self.gridLayout.addWidget(self.on_checkbox, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_save_d = QPushButton(self.tab)
        self.button_save_d.setObjectName(u"button_save_d")

        self.horizontalLayout_5.addWidget(self.button_save_d)


        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)

        self.button_time_reset = QPushButton(self.tab)
        self.button_time_reset.setObjectName(u"button_time_reset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_time_reset.sizePolicy().hasHeightForWidth())
        self.button_time_reset.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_time_reset, 6, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.layout_intervals = QHBoxLayout()
        self.layout_intervals.setObjectName(u"layout_intervals")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_v0 = QLabel(self.tab_2)
        self.label_v0.setObjectName(u"label_v0")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_v0.setFont(font1)

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
        self.value_0_time_up.setFont(font1)

        self.verticalLayout_2.addWidget(self.value_0_time_up)

        self.value_0_time_down = QLabel(self.tab_2)
        self.value_0_time_down.setObjectName(u"value_0_time_down")
        self.value_0_time_down.setFont(font1)

        self.verticalLayout_2.addWidget(self.value_0_time_down)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.value_0_interval_up_front = QLabel(self.tab_2)
        self.value_0_interval_up_front.setObjectName(u"value_0_interval_up_front")
        self.value_0_interval_up_front.setFont(font1)

        self.verticalLayout_2.addWidget(self.value_0_interval_up_front)

        self.value_0_interval_down_front = QLabel(self.tab_2)
        self.value_0_interval_down_front.setObjectName(u"value_0_interval_down_front")
        self.value_0_interval_down_front.setFont(font1)

        self.verticalLayout_2.addWidget(self.value_0_interval_down_front)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_v1 = QLabel(self.tab_2)
        self.label_v1.setObjectName(u"label_v1")
        self.label_v1.setFont(font1)

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
        self.value_1_time_up.setFont(font1)

        self.verticalLayout_4.addWidget(self.value_1_time_up)

        self.value_1_time_down = QLabel(self.tab_2)
        self.value_1_time_down.setObjectName(u"value_1_time_down")
        self.value_1_time_down.setFont(font1)

        self.verticalLayout_4.addWidget(self.value_1_time_down)

        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_4.addWidget(self.label_41)

        self.value_1_interval_up_front = QLabel(self.tab_2)
        self.value_1_interval_up_front.setObjectName(u"value_1_interval_up_front")
        self.value_1_interval_up_front.setFont(font1)

        self.verticalLayout_4.addWidget(self.value_1_interval_up_front)

        self.value_1_interval_down_front = QLabel(self.tab_2)
        self.value_1_interval_down_front.setObjectName(u"value_1_interval_down_front")
        self.value_1_interval_down_front.setFont(font1)

        self.verticalLayout_4.addWidget(self.value_1_interval_down_front)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.layout_intervals.addLayout(self.verticalLayout_3)

        self.table_cnts = QTableView(self.tab_2)
        self.table_cnts.setObjectName(u"table_cnts")
        self.table_cnts.setAutoScroll(True)

        self.layout_intervals.addWidget(self.table_cnts)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.autoStore = QCheckBox(self.tab_2)
        self.autoStore.setObjectName(u"autoStore")

        self.verticalLayout_7.addWidget(self.autoStore)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.timeFreq = QSpinBox(self.tab_2)
        self.timeFreq.setObjectName(u"timeFreq")
        self.timeFreq.setMinimum(1)
        self.timeFreq.setMaximum(5)

        self.verticalLayout_7.addWidget(self.timeFreq)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.button_add = QPushButton(self.tab_2)
        self.button_add.setObjectName(u"button_add")
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.button_add)

        self.button_save_t = QPushButton(self.tab_2)
        self.button_save_t.setObjectName(u"button_save_t")

        self.verticalLayout_7.addWidget(self.button_save_t)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.layout_intervals.addLayout(self.verticalLayout_7)


        self.verticalLayout_30.addLayout(self.layout_intervals)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_8)


        self.gridLayout_4.addLayout(self.verticalLayout_30, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table_exp = QTableView(self.tab_3)
        self.table_exp.setObjectName(u"table_exp")

        self.gridLayout_5.addWidget(self.table_exp, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exp_run = QCheckBox(self.tab_3)
        self.exp_run.setObjectName(u"exp_run")
        self.exp_run.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.exp_run)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exp_save = QPushButton(self.tab_3)
        self.exp_save.setObjectName(u"exp_save")

        self.horizontalLayout.addWidget(self.exp_save)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WiLAB ITMO", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.connectionLabel.setText("")
        self.button_save_s.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0435 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u0440\u043e\u0442", None))
        self.on_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u0435 1 -> 2", None))
        self.button_save_d.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.button_time_reset.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u0443\u043b\u0438\u0442\u044c \u0447\u0430\u0441\u044b [Backspace]", None))
#if QT_CONFIG(shortcut)
        self.button_time_reset.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u043c\u043e\u0436\u043d\u043e \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0430 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0447\u0435\u0440\u0435\u0437 \u0432\u043e\u0440\u043e\u0442\u0430. \u0421\u043b\u0435\u0432\u0430 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0434\u0432\u0435 \u043d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u044b\u0445 \u043a\u043e\u043b\u043e\u043d\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u044b\u0445 \u0432\u043e\u0440\u043e\u0442 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e. \u0421\u043f\u0440\u0430\u0432\u0430 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u043e\u0442\u043c\u0435\u0447\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0441\u043b\u0435\u0434"
                        "\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0432\u044b\u0445, \u0437\u0430\u0442\u0435\u043c \u0432\u0442\u043e\u0440\u044b\u0445 \u0432\u043e\u0440\u043e\u0442. \u0412\u0440\u0435\u043c\u044f \u0432 \u043c\u0438\u043b\u043b\u0438\u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445, \u0438\u0437\u043c\u0435\u0440\u044f\u0435\u0442\u0441\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b, \u043b\u0438\u0431\u043e \u0436\u0435 \u0435\u0433\u043e \u043c\u043e\u0436\u043d\u043e \u043e\u0431\u043d\u0443\u043b\u044f\u0442\u044c \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0438 \"\u041e\u0431\u043d\u0443\u043b\u0438\u0442\u044c\" \u0438\u043b\u0438 \u0436\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0435\u0439 backspace \u043d\u0430 \u043a\u043b\u0430\u0432\u0438"
                        "\u0430\u0442\u0443\u0440\u0435. \u0414\u043b\u044f \u0437\u0430\u043f\u0443\u0441\u043a\u0430, \u043f\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0444\u043b\u0430\u0436\u043e\u043a \"\u0420\u0430\u0431\u043e\u0442\u0430\". ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c", None))
        self.label_v0.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0440\u043e\u0442\u0430 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0435\u0442\u0447\u0438\u043a \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (1 \u0438 0)", None))
        self.value_0_time_up.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_0_time_down.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443, \u043f\u043e \u0441\u043f\u0430\u0434\u0443, \u0441.", None))
        self.value_0_interval_up_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_0_interval_down_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_v1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0440\u043e\u0442\u0430 2", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0435\u0442\u0447\u0438\u043a \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u043e\u0432", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (1 \u0438 0)", None))
        self.value_1_time_up.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_1_time_down.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b (\u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443, \u043f\u043e \u0441\u043f\u0430\u0434\u0443)", None))
        self.value_1_interval_up_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.value_1_interval_down_front.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.autoStore.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u0437\u0430\u043f\u0438\u0441\u0438 \u0413\u0446", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c [Enter]", None))
#if QT_CONFIG(shortcut)
        self.button_add.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.button_save_t.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u043c\u043e\u0436\u043d\u043e \u0432\u0440\u0443\u0447\u043d\u0443\u044e \u0438\u043b\u0438 \u0436\u0435 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u042b\u0445 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430\u0445 \u0441\u0438\u0433\u043d\u0430\u043b\u0430. \"\u0414\u043b\u0438\u0442\u0438\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430\" - \u0432\u0440\u0435\u043c\u044f \u043e\u0442 \u0444\u0440\u043e\u043d\u0442\u0430 \u0434\u043e \u0441\u043f\u0430\u0434\u0430 (\u043f\u0435\u0440\u0432\u043e\u0435 \u043f\u043e\u043b\u0435), \u043e\u0442 \u0441\u043f\u0430\u0434\u0430 \u0434\u043e \u0444\u0440\u043e\u043d\u0442\u0430 (\u0432\u0442\u043e\u0440\u043e"
                        "\u0435). \"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\" - \u0432\u0440\u0435\u043c\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u0444\u0440\u043e\u043d\u0442\u0430\u043c\u0438 (\u043f\u043e \u0444\u0440\u043e\u043d\u0442\u0443), \u0432\u0440\u0435\u043c\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u0441\u043f\u0430\u0434\u0430\u043c\u0438 (\u043f\u043e \u0441\u043f\u0430\u0434\u0443).  \u0412\u0440\u0435\u043c\u044f \u0432 \u043c\u0438\u043b\u043b\u0438\u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445. \u0412 \u0440\u0443\u0447\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u043c\u043e\u0436\u043d\u043e \u043a\u043d\u043e\u043f\u043e\u0439 \"\u0417\u0430\u043f"
                        "\u0438\u0441\u0430\u0442\u044c\" \u0438\u043b\u0438 \u043d\u0430\u0436\u0430\u0432 Enter. \u0414\u043b\u044f \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043b\u043e\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0447\u0430\u0441\u0442\u043e\u0442\u0443 (1-5 \u0413\u0446) \u0438 \u0432\u044b\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0444\u043b\u0430\u0436\u043e\u043a \"\u0410\u0432\u0442\u043e\u0437\u0430\u043f\u0438\u0441\u044c\"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.exp_run.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c [Enter]", None))
#if QT_CONFIG(shortcut)
        self.exp_run.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.exp_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u044c \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0437\u0430\u043c\u0435\u0440\u044b \u043c\u043e\u043c\u0435\u043d\u0442\u043e\u0432 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u0435\u043b \u043f\u0440\u043e\u0445\u043e\u0434 \u0447\u0435\u0440\u0435\u0437 \u0432\u043e\u0440\u043e\u0442\u0430, \u043d\u043e \u0438 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0445\u043e\u0434\u0430 \u0441\u0432\u0435\u0442\u043e\u043d\u0435\u043f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0439 \u0434\u0432\u0438\u0436\u0443\u0449\u0435\u0439\u0441\u044f \u0447\u0430\u0441\u0442\u0438 \u0447\u0435\u0440\u0435\u0437 \u0432\u043e\u043f\u0440\u043e\u0442\u0430, \u0447\u0442\u043e \u043f\u043e\u0437\u0432"
                        "\u043e\u043b\u044f\u0435\u0442, \u0437\u043d\u0430\u044f \u0433\u0435\u043e\u043c\u0435\u0440\u0438\u044e \u043e\u0431\u044a\u0435\u043a\u0442\u0430, \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0435\u0433\u043e \u043c\u0433\u043d\u043e\u0432\u0435\u043d\u043d\u0443\u044e \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c. \u041f\u0440\u0435\u0434\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u043c, \u0447\u0442\u043e \u043a\u0430\u0436\u0434\u044b\u0435 \u0438\u0437 \u0434\u0432\u0443\u0445 \u0432\u043e\u0440\u043e\u0442 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u043e\u0434\u043d\u043e\u0433\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430 \u043c\u043e\u0433\u0443\u0442 \u0441\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043e\u0442 0 \u0434\u043e 2\u0445 \u0440\u0430\u0437 \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e. \u0422\u043e \u0435\u0441\u0442\u044c, \u043f\u0435\u0440\u0432"
                        "\u044b\u0435 4 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u043e\u0442\u0432\u0435\u0447\u0430\u044e\u0442 \u0437\u0430 \u043f\u0435\u0440\u0432\u044b\u0439 \u043f\u0440\u043e\u0445\u043e\u0434 \u043a\u0430\u0436\u0434\u044b\u0445 \u0432\u043e\u0440\u043e\u0442 (\u041b \u0438 \u041f - \u043b\u0435\u0432\u044b\u0435 \u0438 \u043f\u0440\u0430\u0432\u044b\u0435), \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 4 - \u0430\u043d\u0430\u043b\u043e\u0433\u0438\u0447\u043d\u043e \u0434\u043b\u044f \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0440\u043e\u0445\u043e\u0434\u0430. \u041f\u0440\u0438 \u044d\u0442\u043e\u043c \u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0431\u044b\u043b\u0438 \u0432\u0441\u0435 4 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f. \u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0435"
                        "\u0440\u0435\u0434 \u043a\u0430\u0436\u0434\u044b\u043c \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0435\u043c \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u0444\u043b\u0430\u0436\u043e\u043a \"\u0417\u0430\u043f\u0438\u0441\u044c\", \u043b\u0438\u0431\u043e \u043d\u0430\u0436\u0438\u043c\u0430\u0442\u044c Enter \u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0435. \u041f\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u043d\u0443\u0436\u043d\u043e \u0441\u043d\u044f\u0442\u044c \u0444\u043b\u0430\u0436\u043e\u043a, \u043b\u0438\u0431\u043e \u043d\u0430\u0436\u0430\u0442\u044c \u0442\u0443 \u0436\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443, \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043d\u043e\u0432\u0430\u044f"
                        " \u0441\u0442\u0440\u043e\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445. ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0436\u043a\u0438", None))
    # retranslateUi

