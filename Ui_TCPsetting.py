# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric workspace\TCPsetting.ui'
#
# Created: Sun Mar 26 23:27:26 2017
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

class Ui_Dialog_Net(QtGui.QDialog):
    def setupUi(self, Dialog_Net):
        Dialog_Net.setObjectName(_fromUtf8("Dialog_Net"))
        Dialog_Net.resize(400, 262)
        Dialog_Net.setSizeGripEnabled(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Net)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit_serverIP = QtGui.QLineEdit(Dialog_Net)
        self.lineEdit_serverIP.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.lineEdit_serverIP.setObjectName(_fromUtf8("lineEdit_serverIP"))
        self.lineEdit_serverPort = QtGui.QLineEdit(Dialog_Net)
        self.lineEdit_serverPort.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit_serverPort.setObjectName(_fromUtf8("lineEdit_serverPort"))
        self.lineEdit_hostIP = QtGui.QLineEdit(Dialog_Net)
        self.lineEdit_hostIP.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.lineEdit_hostIP.setObjectName(_fromUtf8("lineEdit_hostIP"))
        self.lineEdit_hostPort = QtGui.QLineEdit(Dialog_Net)
        self.lineEdit_hostPort.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.lineEdit_hostPort.setObjectName(_fromUtf8("lineEdit_hostPort"))
        self.label = QtGui.QLabel(Dialog_Net)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_Net)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog_Net)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog_Net)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog_Net)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Net.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Net.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Net)

    def retranslateUi(self, Dialog_Net):
        Dialog_Net.setWindowTitle(_translate("Dialog_Net", "网络设置", None))
        self.label.setText(_translate("Dialog_Net", "服务器IP", None))
        self.label_2.setText(_translate("Dialog_Net", "服务器端口", None))
        self.label_3.setText(_translate("Dialog_Net", "本机IP", None))
        self.label_4.setText(_translate("Dialog_Net", "本机端口", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Net = QtGui.QDialog()
    ui = Ui_Dialog_Net()
    ui.setupUi(Dialog_Net)
    Dialog_Net.show()
    sys.exit(app.exec_())

