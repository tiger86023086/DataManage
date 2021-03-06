# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Project\ProCCMTest\DataManage\code\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataAnalysis(object):
    def setupUi(self, DataAnalysis):
        DataAnalysis.setObjectName("DataAnalysis")
        DataAnalysis.setWindowModality(QtCore.Qt.WindowModal)
        DataAnalysis.resize(1148, 784)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xiaoniao/myico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataAnalysis.setWindowIcon(icon)
        DataAnalysis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(DataAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setStyleSheet("font: 9pt \"Arial\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("font: 14pt \"Agency FB\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.DataSource = QtWidgets.QTabWidget(self.groupBox_2)
        self.DataSource.setObjectName("DataSource")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButtonDataCon = QtWidgets.QToolButton(self.tab_2)
        self.pushButtonDataCon.setGeometry(QtCore.QRect(430, 130, 101, 41))
        self.pushButtonDataCon.setObjectName("pushButtonDataCon")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(3, 30, 100, 34))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(3, 71, 100, 34))
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName("label_8")
        self.lineEditTgtFile = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditTgtFile.setGeometry(QtCore.QRect(110, 71, 884, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTgtFile.sizePolicy().hasHeightForWidth())
        self.lineEditTgtFile.setSizePolicy(sizePolicy)
        self.lineEditTgtFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditTgtFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditTgtFile.setText("")
        self.lineEditTgtFile.setObjectName("lineEditTgtFile")
        self.lineEditDateFile = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditDateFile.setGeometry(QtCore.QRect(110, 30, 884, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDateFile.sizePolicy().hasHeightForWidth())
        self.lineEditDateFile.setSizePolicy(sizePolicy)
        self.lineEditDateFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditDateFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDateFile.setText("")
        self.lineEditDateFile.setObjectName("lineEditDateFile")
        self.pushButtonDateFile = QtWidgets.QToolButton(self.tab_2)
        self.pushButtonDateFile.setGeometry(QtCore.QRect(1000, 29, 69, 34))
        self.pushButtonDateFile.setObjectName("pushButtonDateFile")
        self.pushButtonTgtFile = QtWidgets.QToolButton(self.tab_2)
        self.pushButtonTgtFile.setGeometry(QtCore.QRect(1000, 70, 69, 34))
        self.pushButtonTgtFile.setObjectName("pushButtonTgtFile")
        self.DataSource.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 1071, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonDataSo = QtWidgets.QToolButton(self.layoutWidget)
        self.pushButtonDataSo.setObjectName("pushButtonDataSo")
        self.gridLayout_3.addWidget(self.pushButtonDataSo, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditDataSource = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDataSource.sizePolicy().hasHeightForWidth())
        self.lineEditDataSource.setSizePolicy(sizePolicy)
        self.lineEditDataSource.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditDataSource.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDataSource.setText("")
        self.lineEditDataSource.setObjectName("lineEditDataSource")
        self.gridLayout_3.addWidget(self.lineEditDataSource, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)
        self.pushButtonDBPath = QtWidgets.QToolButton(self.layoutWidget)
        self.pushButtonDBPath.setObjectName("pushButtonDBPath")
        self.gridLayout_3.addWidget(self.pushButtonDBPath, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditDBPath = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDBPath.sizePolicy().hasHeightForWidth())
        self.lineEditDBPath.setSizePolicy(sizePolicy)
        self.lineEditDBPath.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditDBPath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDBPath.setText("")
        self.lineEditDBPath.setObjectName("lineEditDBPath")
        self.gridLayout_3.addWidget(self.lineEditDBPath, 4, 2, 1, 1)
        self.pushButtonMapFile = QtWidgets.QToolButton(self.layoutWidget)
        self.pushButtonMapFile.setObjectName("pushButtonMapFile")
        self.gridLayout_3.addWidget(self.pushButtonMapFile, 1, 3, 1, 1)
        self.lineEditMapFile = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMapFile.sizePolicy().hasHeightForWidth())
        self.lineEditMapFile.setSizePolicy(sizePolicy)
        self.lineEditMapFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditMapFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditMapFile.setText("")
        self.lineEditMapFile.setObjectName("lineEditMapFile")
        self.gridLayout_3.addWidget(self.lineEditMapFile, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonStartD = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStartD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStartD.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonStartD.setObjectName("pushButtonStartD")
        self.horizontalLayout.addWidget(self.pushButtonStartD)
        self.pushButtonStopD = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStopD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStopD.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonStopD.setObjectName("pushButtonStopD")
        self.horizontalLayout.addWidget(self.pushButtonStopD)
        self.pushButtonClearD = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonClearD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonClearD.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonClearD.setObjectName("pushButtonClearD")
        self.horizontalLayout.addWidget(self.pushButtonClearD)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowserD = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowserD.setObjectName("textBrowserD")
        self.verticalLayout.addWidget(self.textBrowserD)
        self.DataSource.addTab(self.tab, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.tab_7)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_7)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditDBFile = QtWidgets.QLineEdit(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDBFile.sizePolicy().hasHeightForWidth())
        self.lineEditDBFile.setSizePolicy(sizePolicy)
        self.lineEditDBFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditDBFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDBFile.setText("")
        self.lineEditDBFile.setObjectName("lineEditDBFile")
        self.gridLayout_4.addWidget(self.lineEditDBFile, 0, 1, 1, 1)
        self.pushButtonDBFile = QtWidgets.QToolButton(self.tab_7)
        self.pushButtonDBFile.setObjectName("pushButtonDBFile")
        self.gridLayout_4.addWidget(self.pushButtonDBFile, 0, 2, 1, 1)
        self.lineEditTitleFile = QtWidgets.QLineEdit(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTitleFile.sizePolicy().hasHeightForWidth())
        self.lineEditTitleFile.setSizePolicy(sizePolicy)
        self.lineEditTitleFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditTitleFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditTitleFile.setText("")
        self.lineEditTitleFile.setObjectName("lineEditTitleFile")
        self.gridLayout_4.addWidget(self.lineEditTitleFile, 1, 1, 1, 1)
        self.pushButtonTitleFile = QtWidgets.QToolButton(self.tab_7)
        self.pushButtonTitleFile.setObjectName("pushButtonTitleFile")
        self.gridLayout_4.addWidget(self.pushButtonTitleFile, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonStartP = QtWidgets.QPushButton(self.tab_7)
        self.pushButtonStartP.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStartP.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonStartP.setObjectName("pushButtonStartP")
        self.horizontalLayout_2.addWidget(self.pushButtonStartP)
        self.pushButtonStopP = QtWidgets.QPushButton(self.tab_7)
        self.pushButtonStopP.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStopP.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonStopP.setObjectName("pushButtonStopP")
        self.horizontalLayout_2.addWidget(self.pushButtonStopP)
        self.pushButtonClearP = QtWidgets.QPushButton(self.tab_7)
        self.pushButtonClearP.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonClearP.setStyleSheet("font: 20pt \"Agency FB\";")
        self.pushButtonClearP.setObjectName("pushButtonClearP")
        self.horizontalLayout_2.addWidget(self.pushButtonClearP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textBrowserP = QtWidgets.QTextBrowser(self.tab_7)
        self.textBrowserP.setObjectName("textBrowserP")
        self.verticalLayout_2.addWidget(self.textBrowserP)
        self.DataSource.addTab(self.tab_7, "")
        self.gridLayout.addWidget(self.DataSource, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        DataAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        DataAnalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataAnalysis)
        self.statusbar.setObjectName("statusbar")
        DataAnalysis.setStatusBar(self.statusbar)
        self.toolBarMenus = QtWidgets.QToolBar(DataAnalysis)
        self.toolBarMenus.setObjectName("toolBarMenus")
        DataAnalysis.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarMenus)
        self.actionActionA = QtWidgets.QAction(DataAnalysis)
        self.actionActionA.setObjectName("actionActionA")
        self.actionActionSubA = QtWidgets.QAction(DataAnalysis)
        self.actionActionSubA.setObjectName("actionActionSubA")
        self.actionActionSubB = QtWidgets.QAction(DataAnalysis)
        self.actionActionSubB.setObjectName("actionActionSubB")
        self.actionActionDelayedA = QtWidgets.QAction(DataAnalysis)
        self.actionActionDelayedA.setObjectName("actionActionDelayedA")
        self.actionActionDelayedSubA = QtWidgets.QAction(DataAnalysis)
        self.actionActionDelayedSubA.setObjectName("actionActionDelayedSubA")
        self.actionActionCheckableA = QtWidgets.QAction(DataAnalysis)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setEnabled(True)
        self.actionActionCheckableA.setObjectName("actionActionCheckableA")
        self.actionActionCheckableSubAChecked = QtWidgets.QAction(DataAnalysis)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName("actionActionCheckableSubAChecked")
        self.actionActionCheckableSubAUnchecked = QtWidgets.QAction(DataAnalysis)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName("actionActionCheckableSubAUnchecked")
        self.actionNewB = QtWidgets.QAction(DataAnalysis)
        self.actionNewB.setObjectName("actionNewB")
        self.actionNewC = QtWidgets.QAction(DataAnalysis)
        self.actionNewC.setObjectName("actionNewC")
        self.actionNewD = QtWidgets.QAction(DataAnalysis)
        self.actionNewD.setObjectName("actionNewD")
        self.actionNewE = QtWidgets.QAction(DataAnalysis)
        self.actionNewE.setObjectName("actionNewE")
        self.actionActionIconADis = QtWidgets.QAction(DataAnalysis)
        self.actionActionIconADis.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/window_undock_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionIconADis.setIcon(icon1)
        self.actionActionIconADis.setObjectName("actionActionIconADis")
        self.actionDarkStyle = QtWidgets.QAction(DataAnalysis)
        self.actionDarkStyle.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/window_close_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDarkStyle.setIcon(icon2)
        self.actionDarkStyle.setObjectName("actionDarkStyle")
        self.actionLightStyle = QtWidgets.QAction(DataAnalysis)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/window_grip_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLightStyle.setIcon(icon3)
        self.actionLightStyle.setObjectName("actionLightStyle")
        self.actionActionDis = QtWidgets.QAction(DataAnalysis)
        self.actionActionDis.setEnabled(False)
        self.actionActionDis.setObjectName("actionActionDis")
        self.actionActionCheckableCheckedDis = QtWidgets.QAction(DataAnalysis)
        self.actionActionCheckableCheckedDis.setCheckable(True)
        self.actionActionCheckableCheckedDis.setChecked(True)
        self.actionActionCheckableCheckedDis.setEnabled(False)
        self.actionActionCheckableCheckedDis.setObjectName("actionActionCheckableCheckedDis")
        self.actionActionCheckableUncheckedDis = QtWidgets.QAction(DataAnalysis)
        self.actionActionCheckableUncheckedDis.setCheckable(True)
        self.actionActionCheckableUncheckedDis.setEnabled(False)
        self.actionActionCheckableUncheckedDis.setObjectName("actionActionCheckableUncheckedDis")
        self.actionActionTranspIcon = QtWidgets.QAction(DataAnalysis)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionTranspIcon.setIcon(icon4)
        self.actionActionTranspIcon.setObjectName("actionActionTranspIcon")
        self.menuMenu.addAction(self.actionDarkStyle)
        self.menuMenu.addAction(self.actionLightStyle)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(DataAnalysis)
        self.DataSource.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataAnalysis)

    def retranslateUi(self, DataAnalysis):
        _translate = QtCore.QCoreApplication.translate
        DataAnalysis.setWindowTitle(_translate("DataAnalysis", "DataAnalysis"))
        self.groupBox.setTitle(_translate("DataAnalysis", "Info"))
        self.label.setText(_translate("DataAnalysis", "<html><head/><body><p><span style=\" font-size:8pt; color:#7d7d7d;\">Pulish by Will at 202105,Coprright 2021</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("DataAnalysis", "Main "))
        self.pushButtonDataCon.setText(_translate("DataAnalysis", "DateConvert"))
        self.label_7.setText(_translate("DataAnalysis", "Date name"))
        self.label_8.setText(_translate("DataAnalysis", "Target path"))
        self.lineEditTgtFile.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditTgtFile.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditTgtFile.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.lineEditDateFile.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditDateFile.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditDateFile.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.pushButtonDateFile.setText(_translate("DataAnalysis", "SetPath"))
        self.pushButtonTgtFile.setText(_translate("DataAnalysis", "SetPath"))
        self.DataSource.setTabText(self.DataSource.indexOf(self.tab_2), _translate("DataAnalysis", "dateConvert"))
        self.pushButtonDataSo.setText(_translate("DataAnalysis", "SetPath"))
        self.label_4.setText(_translate("DataAnalysis", "Map File"))
        self.lineEditDataSource.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditDataSource.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditDataSource.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.label_2.setText(_translate("DataAnalysis", "DB Path"))
        self.pushButtonDBPath.setText(_translate("DataAnalysis", "SetPath"))
        self.label_3.setText(_translate("DataAnalysis", "DataSource"))
        self.lineEditDBPath.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditDBPath.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditDBPath.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.pushButtonMapFile.setText(_translate("DataAnalysis", "SetPath"))
        self.lineEditMapFile.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditMapFile.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditMapFile.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.pushButtonStartD.setText(_translate("DataAnalysis", "Start"))
        self.pushButtonStopD.setText(_translate("DataAnalysis", "Stop"))
        self.pushButtonClearD.setText(_translate("DataAnalysis", "Clear"))
        self.DataSource.setTabText(self.DataSource.indexOf(self.tab), _translate("DataAnalysis", "Database Generate"))
        self.label_6.setText(_translate("DataAnalysis", "Title File"))
        self.label_5.setText(_translate("DataAnalysis", "DB File"))
        self.lineEditDBFile.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditDBFile.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditDBFile.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.pushButtonDBFile.setText(_translate("DataAnalysis", "SetPath"))
        self.lineEditTitleFile.setToolTip(_translate("DataAnalysis", "This is a tool tip"))
        self.lineEditTitleFile.setStatusTip(_translate("DataAnalysis", "This is a status tip"))
        self.lineEditTitleFile.setWhatsThis(_translate("DataAnalysis", "This is \"what is this\""))
        self.pushButtonTitleFile.setText(_translate("DataAnalysis", "SetPath"))
        self.pushButtonStartP.setText(_translate("DataAnalysis", "Start"))
        self.pushButtonStopP.setText(_translate("DataAnalysis", "Stop"))
        self.pushButtonClearP.setText(_translate("DataAnalysis", "Clear"))
        self.DataSource.setTabText(self.DataSource.indexOf(self.tab_7), _translate("DataAnalysis", "Plot Generate"))
        self.menuMenu.setTitle(_translate("DataAnalysis", "Menu"))
        self.menuAbout.setTitle(_translate("DataAnalysis", "About DataAnalysis"))
        self.menuHelp.setTitle(_translate("DataAnalysis", "Help"))
        self.toolBarMenus.setWindowTitle(_translate("DataAnalysis", "Toolbar with menu"))
        self.toolBarMenus.setToolTip(_translate("DataAnalysis", "Toolbar with menu"))
        self.actionActionA.setText(_translate("DataAnalysis", "Action A"))
        self.actionActionSubA.setText(_translate("DataAnalysis", "Action A Sub"))
        self.actionActionSubA.setToolTip(_translate("DataAnalysis", "Action A Sub"))
        self.actionActionSubB.setText(_translate("DataAnalysis", "Action B Sub"))
        self.actionActionDelayedA.setText(_translate("DataAnalysis", "Action Delayed A"))
        self.actionActionDelayedA.setToolTip(_translate("DataAnalysis", "Action Delayed A"))
        self.actionActionDelayedSubA.setText(_translate("DataAnalysis", "Action Delayed Sub A"))
        self.actionActionDelayedSubA.setToolTip(_translate("DataAnalysis", "Action Delayed Sub A"))
        self.actionActionCheckableA.setText(_translate("DataAnalysis", "Action Checkable A"))
        self.actionActionCheckableA.setToolTip(_translate("DataAnalysis", "Action Checkable A"))
        self.actionActionCheckableSubAChecked.setText(_translate("DataAnalysis", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAChecked.setToolTip(_translate("DataAnalysis", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAUnchecked.setText(_translate("DataAnalysis", "Action Checkable Sub A Unchecked"))
        self.actionActionCheckableSubAUnchecked.setToolTip(_translate("DataAnalysis", "Action Checkable Sub A Unchecked"))
        self.actionNewB.setText(_translate("DataAnalysis", "New B"))
        self.actionNewC.setText(_translate("DataAnalysis", "New C"))
        self.actionNewD.setText(_translate("DataAnalysis", "New D"))
        self.actionNewE.setText(_translate("DataAnalysis", "New E"))
        self.actionActionIconADis.setText(_translate("DataAnalysis", "Action Icon A"))
        self.actionDarkStyle.setText(_translate("DataAnalysis", "DarkStyle"))
        self.actionDarkStyle.setToolTip(_translate("DataAnalysis", "Action Icon B"))
        self.actionLightStyle.setText(_translate("DataAnalysis", "LightStyle"))
        self.actionActionDis.setText(_translate("DataAnalysis", "Action Disabled"))
        self.actionActionDis.setToolTip(_translate("DataAnalysis", "Action Disabled"))
        self.actionActionCheckableCheckedDis.setText(_translate("DataAnalysis", "Action Checkable Checked Disabled"))
        self.actionActionCheckableCheckedDis.setToolTip(_translate("DataAnalysis", "Action Checkable Checked Disabled"))
        self.actionActionCheckableUncheckedDis.setText(_translate("DataAnalysis", "Action Checkable Unchecked Disabled"))
        self.actionActionCheckableUncheckedDis.setToolTip(_translate("DataAnalysis", "Action Checkable Unchecked Disabled"))
        self.actionActionTranspIcon.setText(_translate("DataAnalysis", "Action Transp. Icon"))
import style_rc
import xiaoniao_rc
