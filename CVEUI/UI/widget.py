# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from src import LeakAutoDetection as LAD
from src import Initial as In

import datetime

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(869, 597)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 530, 161, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 861, 521))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.sysLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sysLabel.setFont(font)
        self.sysLabel.setObjectName(_fromUtf8("sysLabel"))
        self.horizontalLayout_2.addWidget(self.sysLabel)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 500))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.figLabel = QtGui.QLabel(self.widget)
        self.figLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.figLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.figLabel.setText(_fromUtf8(""))
        self.figLabel.setObjectName(_fromUtf8("figLabel"))
        self.horizontalLayout_3.addWidget(self.figLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setMaximumSize(QtCore.QSize(200, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_4 = QtGui.QMenu(self.menu_2)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        self.menu_5 = QtGui.QMenu(self.menu_2)
        self.menu_5.setObjectName(_fromUtf8("menu_5"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_6 = QtGui.QMenu(self.menu_3)
        self.menu_6.setObjectName(_fromUtf8("menu_6"))
        self.menu_8 = QtGui.QMenu(self.menu_3)
        self.menu_8.setObjectName(_fromUtf8("menu_8"))
        self.menu_7 = QtGui.QMenu(self.menu_3)
        self.menu_7.setObjectName(_fromUtf8("menu_7"))
        self.menu_9 = QtGui.QMenu(self.menubar)
        self.menu_9.setObjectName(_fromUtf8("menu_9"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_12 = QtGui.QAction(MainWindow)
        self.action_12.setObjectName(_fromUtf8("action_12"))
        self.action_13 = QtGui.QAction(MainWindow)
        self.action_13.setObjectName(_fromUtf8("action_13"))
        self.action_14 = QtGui.QAction(MainWindow)
        self.action_14.setObjectName(_fromUtf8("action_14"))
        self.action_15 = QtGui.QAction(MainWindow)
        self.action_15.setObjectName(_fromUtf8("action_15"))
        self.action_16 = QtGui.QAction(MainWindow)
        self.action_16.setObjectName(_fromUtf8("action_16"))
        self.action_17 = QtGui.QAction(MainWindow)
        self.action_17.setObjectName(_fromUtf8("action_17"))
        self.action_18 = QtGui.QAction(MainWindow)
        self.action_18.setObjectName(_fromUtf8("action_18"))
        self.action_19 = QtGui.QAction(MainWindow)
        self.action_19.setObjectName(_fromUtf8("action_19"))
        self.action_20 = QtGui.QAction(MainWindow)
        self.action_20.setObjectName(_fromUtf8("action_20"))
        self.action_21 = QtGui.QAction(MainWindow)
        self.action_21.setObjectName(_fromUtf8("action_21"))
        self.action_22 = QtGui.QAction(MainWindow)
        self.action_22.setObjectName(_fromUtf8("action_22"))
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action)
        self.menu_4.addAction(self.action_13)
        self.menu_4.addAction(self.action_14)
        self.menu_5.addAction(self.action_15)
        self.menu_5.addAction(self.action_16)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menu_2.addAction(self.menu_5.menuAction())
        self.menu_6.addAction(self.action_17)
        self.menu_6.addAction(self.action_18)
        self.menu_8.addAction(self.action_21)
        self.menu_8.addAction(self.action_22)
        self.menu_7.addAction(self.action_19)
        self.menu_7.addAction(self.action_20)
        self.menu_3.addAction(self.menu_6.menuAction())
        self.menu_3.addAction(self.menu_7.menuAction())
        self.menu_3.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())

        self.retranslateUi(MainWindow)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showThreats)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_bar)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_pie)
        QtCore.QObject.connect.connect(self.pushButton,  QtCore.SIGNAL(_fromUtf8("clicked()")), self.slotStart)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "关键性基础设施漏洞实时追踪系统", None))
        self.label.setText(_translate("MainWindow", "ISCAS CopyRight 2018-2025", None))
        self.sysLabel.setText(_translate("MainWindow", "关键性基础设施漏洞实时追踪系统", None))
        self.pushButton.setText(_translate("MainWindow", "更新数据库", None))
        self.pushButton_2.setText(_translate("MainWindow", "漏洞威胁统计", None))
        self.pushButton_3.setText(_translate("MainWindow", "威胁实时跟踪", None))
        self.menu.setTitle(_translate("MainWindow", "基础设施", None))
        self.menu_2.setTitle(_translate("MainWindow", "漏洞追踪", None))
        self.menu_4.setTitle(_translate("MainWindow", "威胁匹配", None))
        self.menu_5.setTitle(_translate("MainWindow", "实时跟踪", None))
        self.menu_3.setTitle(_translate("MainWindow", "统计显示", None))
        self.menu_6.setTitle(_translate("MainWindow", "柱状图", None))
        self.menu_8.setTitle(_translate("MainWindow", "威胁有向图", None))
        self.menu_7.setTitle(_translate("MainWindow", "饼状图", None))
        self.menu_9.setTitle(_translate("MainWindow", "说明文档", None))
        self.action_2.setText(_translate("MainWindow", "新建", None))
        self.action_3.setText(_translate("MainWindow", "删除", None))
        self.action_4.setText(_translate("MainWindow", "保存", None))
        self.action_5.setText(_translate("MainWindow", "另存为", None))
        self.action_6.setText(_translate("MainWindow", "数据库更新", None))
        self.action.setText(_translate("MainWindow", "退出", None))
        self.action_12.setText(_translate("MainWindow", "保存", None))
        self.action_13.setText(_translate("MainWindow", "保存", None))
        self.action_14.setText(_translate("MainWindow", "删除", None))
        self.action_15.setText(_translate("MainWindow", "保存", None))
        self.action_16.setText(_translate("MainWindow", "删除", None))
        self.action_17.setText(_translate("MainWindow", "保存", None))
        self.action_18.setText(_translate("MainWindow", "删除", None))
        self.action_19.setText(_translate("MainWindow", "保存", None))
        self.action_20.setText(_translate("MainWindow", "删除", None))
        self.action_21.setText(_translate("MainWindow", "保存", None))
        self.action_22.setText(_translate("MainWindow", "删除", None))

    def update(self):
        sender = self.pushButton.sender() #获取信号
        LAD.createVulDatabase()
        self.textBrowser.setText(datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S') + ': CVE Database was updated!\n')

    def show(self):
        sender = self.pushButton_2.sender() #获取信号
        In.drawResults()
        png = QtGui.QPixmap('bar.png').scaled(self.figLabel.width(), self.figLabel.height())
        self.figLabel.setPixmap(png)
        self.textBrowser.setText(
            datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')  + ': Statistic Results was showed!\n')

    def showThreats(self):
        sender = self.pushButton_3.sender() #获取信号
        g1 = In.matchThreats()
        png = QtGui.QPixmap('g1.svg').scaled(self.figLabel.width(), self.figLabel.height())
        self.figLabel.setPixmap(png)
        self.textBrowser.setText(
            datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')  + ': Real-time Threats Path Results was showed!\n')

    def show_bar(self):
        sender = self.radioButton.sender() #获取信号
        In.drawResults()
        png = QtGui.QPixmap('bar.png').scaled(self.figLabel.width(), self.figLabel.height())
        self.figLabel.setPixmap(png)

    def show_pie(self):
        sender = self.radioButton_2.sender()  # 获取信号
        In.drawResults()
        png = QtGui.QPixmap('pie.png').scaled(self.figLabel.width(), self.figLabel.height())
        self.figLabel.setPixmap(png)



    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step += 1
        self.progressBar.setValue(self.step)

    def slotStart(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText(_translate("MainWindow", "开始", None))
        else:
            self.timer.start(100, self)
            self.pushButton.setText(_translate("MainWindow", "停止", None))


