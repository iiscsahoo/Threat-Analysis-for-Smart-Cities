# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Windows.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
        MainWindow.resize(753, 544)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.sysLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sysLabel.sizePolicy().hasHeightForWidth())
        self.sysLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sysLabel.setFont(font)
        self.sysLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.sysLabel.setObjectName(_fromUtf8("sysLabel"))
        self.horizontalLayout_2.addWidget(self.sysLabel)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout_7.addWidget(self.textBrowser)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.figLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figLabel.sizePolicy().hasHeightForWidth())
        self.figLabel.setSizePolicy(sizePolicy)
        self.figLabel.setMinimumSize(QtCore.QSize(650, 350))
        self.figLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.figLabel.setText(_fromUtf8(""))
        self.figLabel.setObjectName(_fromUtf8("figLabel"))
        self.verticalLayout_3.addWidget(self.figLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        spacerItem3 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(150, 20))
        self.progressBar.setMaximum(150)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        spacerItem5 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem6 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(600, 15))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.radioButton_4.raise_()
        self.figLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 23))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "关键性基础设施漏洞实时追踪系统", None))
        self.sysLabel.setText(_translate("MainWindow", "关键性基础设施漏洞实时追踪系统", None))
        self.radioButton_3.setText(_translate("MainWindow", "柱状图", None))
        self.radioButton_4.setText(_translate("MainWindow", "饼状图", None))
        self.pushButton.setText(_translate("MainWindow", "更新数据库", None))
        self.pushButton_2.setText(_translate("MainWindow", "漏洞威胁统计", None))
        self.pushButton_3.setText(_translate("MainWindow", "威胁实时跟踪", None))
        self.label.setText(_translate("MainWindow", "ISCAS CopyRight 2018-2025", None))
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

