# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pycharm\MplMainWindow.ui'
#
# Created: Wed Jun 28 15:21:51 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(679, 640)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mplCanvas = MplCanvasWrapper(self.centralWidget)
        self.mplCanvas.setGeometry(QtCore.QRect(10, 0, 661, 611))
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.cmdlnkbtn_datarfreq = QtGui.QCommandLinkButton(self.mplCanvas)
        self.cmdlnkbtn_datarfreq.setGeometry(QtCore.QRect(540, 50, 111, 41))
        self.cmdlnkbtn_datarfreq.setDescription(_fromUtf8(""))
        self.cmdlnkbtn_datarfreq.setObjectName(_fromUtf8("cmdlnkbtn_datarfreq"))
        self.cmdlnkbtn_realrhis = QtGui.QCommandLinkButton(self.mplCanvas)
        self.cmdlnkbtn_realrhis.setGeometry(QtCore.QRect(540, 560, 111, 41))
        self.cmdlnkbtn_realrhis.setMouseTracking(False)
        self.cmdlnkbtn_realrhis.setDescription(_fromUtf8(""))
        self.cmdlnkbtn_realrhis.setObjectName(_fromUtf8("cmdlnkbtn_realrhis"))
        self.dateEdit = QtGui.QDateEdit(self.mplCanvas)
        self.dateEdit.setGeometry(QtCore.QRect(90, 580, 110, 21))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.lbl_choosedate = QtGui.QLabel(self.mplCanvas)
        self.lbl_choosedate.setGeometry(QtCore.QRect(30, 580, 54, 21))
        self.lbl_choosedate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_choosedate.setObjectName(_fromUtf8("lbl_choosedate"))
        self.lbl_choosedate_2 = QtGui.QLabel(self.mplCanvas)
        self.lbl_choosedate_2.setGeometry(QtCore.QRect(220, 580, 54, 21))
        self.lbl_choosedate_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_choosedate_2.setObjectName(_fromUtf8("lbl_choosedate_2"))
        self.comboBox_chselect = QtGui.QComboBox(self.mplCanvas)
        self.comboBox_chselect.setGeometry(QtCore.QRect(280, 580, 69, 22))
        self.comboBox_chselect.setEditable(True)
        self.comboBox_chselect.setObjectName(_fromUtf8("comboBox_chselect"))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.comboBox_chselect.addItem(_fromUtf8(""))
        self.btn_showhis = QtGui.QPushButton(self.mplCanvas)
        self.btn_showhis.setGeometry(QtCore.QRect(380, 580, 75, 23))
        self.btn_showhis.setObjectName(_fromUtf8("btn_showhis"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 679, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menuBar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionFFT = QtGui.QAction(MainWindow)
        self.actionFFT.setObjectName(_fromUtf8("actionFFT"))
        self.actionPath = QtGui.QAction(MainWindow)
        self.actionPath.setObjectName(_fromUtf8("actionPath"))
        self.actionSerial = QtGui.QAction(MainWindow)
        self.actionSerial.setObjectName(_fromUtf8("actionSerial"))
        self.actionOpenSerial = QtGui.QAction(MainWindow)
        self.actionOpenSerial.setObjectName(_fromUtf8("actionOpenSerial"))
        self.actionCloseSerial = QtGui.QAction(MainWindow)
        self.actionCloseSerial.setEnabled(False)
        self.actionCloseSerial.setObjectName(_fromUtf8("actionCloseSerial"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setEnabled(False)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setEnabled(True)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionNet = QtGui.QAction(MainWindow)
        self.actionNet.setObjectName(_fromUtf8("actionNet"))
        self.menu.addAction(self.actionFFT)
        self.menu.addAction(self.actionPath)
        self.menu.addAction(self.actionSerial)
        self.menu.addAction(self.actionNet)
        self.menu_2.addAction(self.actionConnect)
        self.menu_2.addAction(self.actionCut)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "索力计数据采集分析系统", None))
        self.cmdlnkbtn_datarfreq.setText(_translate("MainWindow", "时/频切换", None))
        self.cmdlnkbtn_realrhis.setText(_translate("MainWindow", "实时显示", None))
        self.lbl_choosedate.setText(_translate("MainWindow", "选择日期", None))
        self.lbl_choosedate_2.setText(_translate("MainWindow", "选择通道", None))
        self.comboBox_chselect.setItemText(0, _translate("MainWindow", "通道 1", None))
        self.comboBox_chselect.setItemText(1, _translate("MainWindow", "通道 2", None))
        self.comboBox_chselect.setItemText(2, _translate("MainWindow", "通道 3", None))
        self.comboBox_chselect.setItemText(3, _translate("MainWindow", "通道 4", None))
        self.comboBox_chselect.setItemText(4, _translate("MainWindow", "通道 5", None))
        self.comboBox_chselect.setItemText(5, _translate("MainWindow", "通道 6", None))
        self.comboBox_chselect.setItemText(6, _translate("MainWindow", "通道 7", None))
        self.comboBox_chselect.setItemText(7, _translate("MainWindow", "通道 8", None))
        self.btn_showhis.setText(_translate("MainWindow", "OK", None))
        self.menu.setTitle(_translate("MainWindow", "设置", None))
        self.menu_2.setTitle(_translate("MainWindow", "控制", None))
        self.actionFFT.setText(_translate("MainWindow", "FFT设置", None))
        self.actionPath.setText(_translate("MainWindow", "路径设置", None))
        self.actionSerial.setText(_translate("MainWindow", "通道设置", None))
        self.actionOpenSerial.setText(_translate("MainWindow", "打开串口", None))
        self.actionCloseSerial.setText(_translate("MainWindow", "关闭串口", None))
        self.actionConnect.setText(_translate("MainWindow", "建立连接", None))
        self.actionCut.setText(_translate("MainWindow", "断开连接", None))
        self.actionNet.setText(_translate("MainWindow", "网络设置", None))

from mplcanvaswrapper import MplCanvasWrapper
