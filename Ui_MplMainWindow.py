# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\MplMainWindow.ui'
#
# Created: Thu May 11 23:14:18 2017
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
        MainWindow.resize(679, 675)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mplCanvas = MplCanvasWrapper(self.centralWidget)
        self.mplCanvas.setGeometry(QtCore.QRect(0, 0, 661, 611))
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
        self.checkBox4 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox4.setGeometry(QtCore.QRect(270, 620, 71, 16))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox8 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox8.setGeometry(QtCore.QRect(550, 620, 71, 16))
        self.checkBox8.setObjectName(_fromUtf8("checkBox8"))
        self.checkBox1 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox1.setGeometry(QtCore.QRect(60, 620, 71, 16))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox3 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox3.setGeometry(QtCore.QRect(200, 620, 71, 16))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox2 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox2.setGeometry(QtCore.QRect(130, 620, 71, 16))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox5 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox5.setGeometry(QtCore.QRect(340, 620, 71, 16))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox6.setGeometry(QtCore.QRect(410, 620, 71, 16))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.checkBox7 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox7.setGeometry(QtCore.QRect(480, 620, 71, 16))
        self.checkBox7.setObjectName(_fromUtf8("checkBox7"))
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
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setEnabled(False)
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
        self.checkBox4.setText(_translate("MainWindow", "通道4", None))
        self.checkBox8.setText(_translate("MainWindow", "通道8", None))
        self.checkBox1.setText(_translate("MainWindow", "通道1", None))
        self.checkBox3.setText(_translate("MainWindow", "通道3", None))
        self.checkBox2.setText(_translate("MainWindow", "通道2", None))
        self.checkBox5.setText(_translate("MainWindow", "通道5", None))
        self.checkBox6.setText(_translate("MainWindow", "通道6", None))
        self.checkBox7.setText(_translate("MainWindow", "通道7", None))
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
