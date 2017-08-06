# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Ui_MplMainWindow import Ui_MainWindow
import os

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

filepath = "D:\data"
fftnum = 4096
fftfreq = 100.64
fftrepeat = '1/2'
fftwindow = u"矩形窗"

# 0:none_checked 1:half_checked 2:checked
glb_seriallist =\
[
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ['2-1', '2-2', '2-3', '2-4', '2-5', '3-1', '3-2', '3-3', '3-4', '3-5', '4-1', '4-2', '4-3', '5-1', '5-2', '5-3'],
]

serverIP = '127.0.0.1'
serverPort = 50040
hostIP = '127.0.0.1'
hostPort = 50000
channelchoosed = '通道 1'
datechoosed = ''


class Code_MainWindow(Ui_MainWindow):
    signal_getDateparam = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.cmdlnkbtn_datarfreq.clicked.connect(self.freqordata)
        self.cmdlnkbtn_realrhis.clicked.connect(self.realtimeorhistory)
        self.btn_showhis.clicked.connect(self.signal_emitter)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.signal_getDateparam.connect(self.getDate)

        global fftnum
        global fftfreq
        global fftwindow
        self.mplCanvas.canvas.fftnum = fftnum
        self.mplCanvas.canvas.fftfreq = float(fftfreq)
        self.mplCanvas.canvas.fftwindow = fftwindow

        global filepath
        path = filepath.split("\\")
        path = [x + os.path.sep for x in path]
        path = ''.join(path)
        self.mplCanvas.canvas.filepath = path

        global glb_seriallist
        i = 0
        for x in self.mplCanvas.canvas.datalist:
            if glb_seriallist[0][i] == 2:
                x['enabled'] = True
                x['device'] = glb_seriallist[1][i]
            else:
                x['enabled'] = False
                x['device'] = glb_seriallist[1][i]
            i = i + 1

        global fftrepeat
        listrepeatrate = fftrepeat.split('/')
        if len(listrepeatrate) is 1:
            repeatrate = 0
        else:
            repeatrate = float(listrepeatrate[0]) / float(listrepeatrate[1])
        self.mplCanvas.canvas.fftrepeat = repeatrate

        global datechoosed
        datechoosed = QtCore.QDate.currentDate()

        self.mplCanvas.initDataGenerator()
        self.Connect()

    def signal_emitter(self):
        self.signal_getDateparam.emit()
        
    def freqordata(self):
        self.mplCanvas.showDataorFreq() 
    
    def realtimeorhistory(self):
        if(self.cmdlnkbtn_realrhis.text().toUtf8() == "实时显示"):
            self.cmdlnkbtn_realrhis.setText(_translate("MainWindow", "查看历史", None))
            self.dateEdit.hide()
            self.lbl_choosedate.hide()
            self.lbl_choosedate_2.hide()
            self.comboBox_chselect.hide()
            self.btn_showhis.hide()
            self.mplCanvas.startPlot()  
        else:
            global datechoosed
            datechoosed = QtCore.QDate.currentDate()
            self.dateEdit.setDate(QtCore.QDate.currentDate())
            self.cmdlnkbtn_realrhis.setText(_translate("MainWindow", "实时显示", None))
            self.dateEdit.show()
            self.lbl_choosedate.show()
            self.lbl_choosedate_2.show()
            self.comboBox_chselect.show()
            self.btn_showhis.show()
            self.mplCanvas.pausePlot()
       
    def releasePlot(self):
        '''stop and release thread'''
        self.mplCanvas.releasePlot()

    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            self.releasePlot()  # release thread's resouce
            event.accept()

    def Connect(self):
        global serverIP
        global serverPort
        self.mplCanvas.client.connect(serverIP, serverPort)
        self.mplCanvas.client.needtosend = True
        self.actionConnect.setEnabled(False)
        self.actionCut.setEnabled(True)

    @QtCore.pyqtSlot()
    def getDate(self):
        global datechoosed
        global channelchoosed
        channelchoosed = self.comboBox_chselect.currentText()
        datechoosed = self.dateEdit.date().toString('yyyy-MM-dd')
        self.mplCanvas.canvas.displayhistory(datechoosed, channelchoosed)

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    app = QtGui.QApplication(sys.argv)
    ui_main = Code_MainWindow()
    ui_main.show()
sys.exit(app.exec_())
