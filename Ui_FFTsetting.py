# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\FFTsetting.ui'
#
# Created: Mon May 15 00:15:30 2017
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

class Ui_Dialog_FFT(QtGui.QDialog):
    def setupUi(self, Dialog_FFT):
        Dialog_FFT.setObjectName(_fromUtf8("Dialog_FFT"))
        Dialog_FFT.resize(372, 255)
        Dialog_FFT.setSizeGripEnabled(True)
        self.label_3 = QtGui.QLabel(Dialog_FFT)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 41, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_FFT)
        self.buttonBox.setGeometry(QtCore.QRect(20, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_5 = QtGui.QLabel(Dialog_FFT)
        self.label_5.setGeometry(QtCore.QRect(50, 110, 41, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog_FFT)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog_FFT)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 41, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_repeatrate = QtGui.QComboBox(Dialog_FFT)
        self.comboBox_repeatrate.setGeometry(QtCore.QRect(120, 110, 69, 22))
        self.comboBox_repeatrate.setObjectName(_fromUtf8("comboBox_repeatrate"))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_repeatrate.addItem(_fromUtf8(""))
        self.comboBox_FFTnum = QtGui.QComboBox(Dialog_FFT)
        self.comboBox_FFTnum.setGeometry(QtCore.QRect(120, 30, 69, 22))
        self.comboBox_FFTnum.setObjectName(_fromUtf8("comboBox_FFTnum"))
        self.comboBox_FFTnum.addItem(_fromUtf8(""))
        self.comboBox_FFTnum.addItem(_fromUtf8(""))
        self.comboBox_FFTnum.addItem(_fromUtf8(""))
        self.comboBox_FFTnum.addItem(_fromUtf8(""))
        self.comboBox_capturefreq = QtGui.QComboBox(Dialog_FFT)
        self.comboBox_capturefreq.setGeometry(QtCore.QRect(120, 70, 69, 22))
        self.comboBox_capturefreq.setObjectName(_fromUtf8("comboBox_capturefreq"))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_capturefreq.addItem(_fromUtf8(""))
        self.comboBox_windowfunc = QtGui.QComboBox(Dialog_FFT)
        self.comboBox_windowfunc.setGeometry(QtCore.QRect(120, 150, 69, 22))
        self.comboBox_windowfunc.setObjectName(_fromUtf8("comboBox_windowfunc"))
        self.comboBox_windowfunc.addItem(_fromUtf8(""))
        self.comboBox_windowfunc.addItem(_fromUtf8(""))
        self.comboBox_windowfunc.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog_FFT)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_FFT.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_FFT.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_FFT)

    def retranslateUi(self, Dialog_FFT):
        Dialog_FFT.setWindowTitle(_translate("Dialog_FFT", "Dialog", None))
        self.label_3.setText(_translate("Dialog_FFT", "窗函数", None))
        self.label_5.setText(_translate("Dialog_FFT", "重叠率", None))
        self.label_6.setText(_translate("Dialog_FFT", "采样频率", None))
        self.label_7.setText(_translate("Dialog_FFT", "FFT点数", None))
        self.comboBox_repeatrate.setItemText(0, _translate("Dialog_FFT", "0", None))
        self.comboBox_repeatrate.setItemText(1, _translate("Dialog_FFT", "1/6", None))
        self.comboBox_repeatrate.setItemText(2, _translate("Dialog_FFT", "1/5", None))
        self.comboBox_repeatrate.setItemText(3, _translate("Dialog_FFT", "1/4", None))
        self.comboBox_repeatrate.setItemText(4, _translate("Dialog_FFT", "1/3", None))
        self.comboBox_repeatrate.setItemText(5, _translate("Dialog_FFT", "1/2", None))
        self.comboBox_repeatrate.setItemText(6, _translate("Dialog_FFT", "2/3", None))
        self.comboBox_repeatrate.setItemText(7, _translate("Dialog_FFT", "3/4", None))
        self.comboBox_repeatrate.setItemText(8, _translate("Dialog_FFT", "4/5", None))
        self.comboBox_repeatrate.setItemText(9, _translate("Dialog_FFT", "5/6", None))
        self.comboBox_FFTnum.setItemText(0, _translate("Dialog_FFT", "1024", None))
        self.comboBox_FFTnum.setItemText(1, _translate("Dialog_FFT", "2048", None))
        self.comboBox_FFTnum.setItemText(2, _translate("Dialog_FFT", "4096", None))
        self.comboBox_FFTnum.setItemText(3, _translate("Dialog_FFT", "8192", None))
        self.comboBox_capturefreq.setItemText(0, _translate("Dialog_FFT", "10", None))
        self.comboBox_capturefreq.setItemText(1, _translate("Dialog_FFT", "20", None))
        self.comboBox_capturefreq.setItemText(2, _translate("Dialog_FFT", "40", None))
        self.comboBox_capturefreq.setItemText(3, _translate("Dialog_FFT", "50", None))
        self.comboBox_capturefreq.setItemText(4, _translate("Dialog_FFT", "100", None))
        self.comboBox_capturefreq.setItemText(5, _translate("Dialog_FFT", "120", None))
        self.comboBox_capturefreq.setItemText(6, _translate("Dialog_FFT", "150", None))
        self.comboBox_capturefreq.setItemText(7, _translate("Dialog_FFT", "160", None))
        self.comboBox_capturefreq.setItemText(8, _translate("Dialog_FFT", "200", None))
        self.comboBox_windowfunc.setItemText(0, _translate("Dialog_FFT", "矩形窗", None))
        self.comboBox_windowfunc.setItemText(1, _translate("Dialog_FFT", "汉宁窗", None))
        self.comboBox_windowfunc.setItemText(2, _translate("Dialog_FFT", "海明窗", None))

