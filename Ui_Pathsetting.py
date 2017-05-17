# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric workspace\Pathsetting.ui'
#
# Created: Wed Mar 08 11:30:40 2017
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

class Ui_Dialog_Path(QtGui.QDialog):
    def setupUi(self, Dialog_Path):
        Dialog_Path.setObjectName(_fromUtf8("Dialog_Path"))
        Dialog_Path.resize(400, 158)
        Dialog_Path.setSizeGripEnabled(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Path)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog_Path)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_opfp = QtGui.QPushButton(Dialog_Path)
        self.btn_opfp.setGeometry(QtCore.QRect(330, 30, 31, 23))
        self.btn_opfp.setObjectName(_fromUtf8("btn_opfp"))
        self.lineEdit_path = QtGui.QLineEdit(Dialog_Path)
        self.lineEdit_path.setGeometry(QtCore.QRect(100, 30, 221, 20))
        self.lineEdit_path.setObjectName(_fromUtf8("lineEdit_path"))

        self.retranslateUi(Dialog_Path)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Path.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Path.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Path)

    def retranslateUi(self, Dialog_Path):
        Dialog_Path.setWindowTitle(_translate("Dialog_Path", "Dialog", None))
        self.label.setText(_translate("Dialog_Path", "缓存文件夹", None))
        self.btn_opfp.setText(_translate("Dialog_Path", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Path = QtGui.QDialog()
    ui = Ui_Dialog_Path()
    ui.setupUi(Dialog_Path)
    Dialog_Path.show()
    sys.exit(app.exec_())

