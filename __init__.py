# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Ui_MplMainWindow import Ui_MainWindow
from Ui_FFTsetting import Ui_Dialog_FFT
from Ui_Pathsetting import Ui_Dialog_Path
from Ui_Serialsetting import Ui_Dialog_Serial
from Ui_TCPsetting import Ui_Dialog_Net
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

filepath = "C:\Users\zwq\Desktop\pydat"
fftnum = 8192
fftfreq = 200
fftrepeat = '0'
fftwindow = u"矩形窗"

# 0:none_checked 1:half_checked 2:checked
glb_seriallist =\
[
    [2, 0, 0, 0, 0, 0, 0, 0],
    ['1-1', '1-2', '2-1', '2-2', '3-1', '3-2', '4-1', '4-2'],
]

serverIP = '127.0.0.1'
serverPort = 8080
hostIP = '127.0.0.1'
hostPort = 50000
channelchoosed = '通道 1'
datechoosed = ''

class Code_NetWindow(Ui_Dialog_Net):
    signal_getNetparam = QtCore.pyqtSignal(dict)

    def __init__(self, parent = None):
        super(Code_NetWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_serverIP.setText(serverIP)
        self.lineEdit_serverPort.setText(str(serverPort))
        self.lineEdit_hostIP.setText(hostIP)
        self.lineEdit_hostPort.setText(str(hostPort))
        self.buttonBox.accepted.connect(self.signal_emitter)

    def signal_emitter(self):
        Netdict = {}
        Netdict['serverIP'] = self.lineEdit_serverIP.text()
        Netdict['serverPort'] = int(self.lineEdit_serverPort.text())
        Netdict['hostIP'] = self.lineEdit_hostIP.text()
        Netdict['hostPort'] = int(self.lineEdit_hostPort.text())
        self.signal_getNetparam.emit(Netdict)

class Code_SerialWindow(Ui_Dialog_Serial):
    signal_getSerialparam = QtCore.pyqtSignal(list)

    def __init__(self, parent = None):
        global glb_seriallist
        super(Code_SerialWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox_com1.setCheckState(glb_seriallist[0][0])
        self.checkBox_com2.setCheckState(glb_seriallist[0][1])
        self.checkBox_com3.setCheckState(glb_seriallist[0][2])
        self.checkBox_com4.setCheckState(glb_seriallist[0][3])
        self.checkBox_com5.setCheckState(glb_seriallist[0][4])
        self.checkBox_com6.setCheckState(glb_seriallist[0][5])
        self.checkBox_com7.setCheckState(glb_seriallist[0][6])
        self.checkBox_com8.setCheckState(glb_seriallist[0][7])

        self.lineEdit_chno1.setText(glb_seriallist[1][0])
        self.lineEdit_chno2.setText(glb_seriallist[1][1])
        self.lineEdit_chno3.setText(glb_seriallist[1][2])
        self.lineEdit_chno4.setText(glb_seriallist[1][3])
        self.lineEdit_chno5.setText(glb_seriallist[1][4])
        self.lineEdit_chno6.setText(glb_seriallist[1][5])
        self.lineEdit_chno7.setText(glb_seriallist[1][6])
        self.lineEdit_chno8.setText(glb_seriallist[1][7])
        
        self.buttonBox.accepted.connect(self.signal_emitter)

    def signal_emitter(self):
        Seriallist = []
        Seriallist.append([
                            self.checkBox_com1.checkState(), self.checkBox_com2.checkState(),
                            self.checkBox_com3.checkState(), self.checkBox_com4.checkState(),
                            self.checkBox_com5.checkState(), self.checkBox_com6.checkState(),
                            self.checkBox_com7.checkState(), self.checkBox_com8.checkState(),
                          ])
        Seriallist.append([
                            self.lineEdit_chno1.text(), self.lineEdit_chno2.text(),
                            self.lineEdit_chno3.text(), self.lineEdit_chno4.text(),
                            self.lineEdit_chno5.text(), self.lineEdit_chno6.text(),
                            self.lineEdit_chno7.text(), self.lineEdit_chno8.text(),
                          ])
        self.signal_getSerialparam.emit(Seriallist)


class Code_FFTWindow(Ui_Dialog_FFT):
    signal_getFFTparam = QtCore.pyqtSignal(dict)

    def __init__(self, parent = None):
        super(Code_FFTWindow, self).__init__(parent)
        self.setupUi(self)
        self.comboBox_FFTnum.setEditable(True)
        self.comboBox_FFTnum.setEditText(str(fftnum))
        self.comboBox_capturefreq.setEditable(True)
        self.comboBox_capturefreq.setEditText(str(fftfreq))
        self.comboBox_windowfunc.setEditable(True)
        self.comboBox_windowfunc.setEditText(fftwindow)
        self.comboBox_repeatrate.setEditable(True)
        self.comboBox_repeatrate.setEditText(fftrepeat)
        self.buttonBox.accepted.connect(self.signal_emitter)

    def signal_emitter(self):
        FFTdict = {}
        FFTdict['num'] = int(self.comboBox_FFTnum.currentText())
        FFTdict['freq'] = int(self.comboBox_capturefreq.currentText())
        FFTdict['window'] = self.comboBox_windowfunc.currentText()
        FFTdict['repeat'] = self.comboBox_repeatrate.currentText()
        self.signal_getFFTparam.emit(FFTdict)


class Code_PathWindow(Ui_Dialog_Path):
    signal_getPathparam = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(Code_PathWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_path.setText(filepath)
        self.buttonBox.accepted.connect(self.signal_emitter)
        self.btn_opfp.clicked.connect(self.dlggetStrPath)
    
    def signal_emitter(self):
        self.signal_getPathparam.emit(self.lineEdit_path.text())
    
    def dlggetStrPath(self):
        dlgfilepath = QtGui.QFileDialog.getExistingDirectory(self, 'choose directory', './')
        self.lineEdit_path.setText(dlgfilepath)


class Code_MainWindow(Ui_MainWindow):
    signal_getDateparam = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionFFT.triggered.connect(self.openFFTDlg)
        self.actionPath.triggered.connect(self.openPathDlg)
        self.actionSerial.triggered.connect(self.openSerialDlg)
        self.actionNet.triggered.connect(self.openNetDlg)
        
        self.actionConnect.triggered.connect(self.Connect)
        self.actionCut.triggered.connect(self.Cut)
        
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

    def Cut(self):
        self.mplCanvas.client.needtosend = False
        self.actionConnect.setEnabled(True)
        self.actionCut.setEnabled(False)
        self.mplCanvas.client.disconnect()
 
    def Connect(self):
        global serverIP
        global serverPort
        self.mplCanvas.client.connect(serverIP, serverPort)
        self.mplCanvas.client.needtosend = True
        self.actionConnect.setEnabled(False)
        self.actionCut.setEnabled(True)
        
    def openNetDlg(self):
        ui_Net= Code_NetWindow(self)
        ui_Net.show()
        ui_Net.signal_getNetparam.connect(self.getDictNet)
 
    def openSerialDlg(self):
        ui_Serial = Code_SerialWindow(self)
        ui_Serial.show()
        ui_Serial.signal_getSerialparam.connect(self.getListSerial)
 
    def openFFTDlg(self):
        ui_FFT = Code_FFTWindow(self)
        ui_FFT.show()
        ui_FFT.signal_getFFTparam.connect(self.getDictFFT)
    
    def openPathDlg(self):  
        ui_Path = Code_PathWindow(self)  
        ui_Path.show() 
        ui_Path.signal_getPathparam.connect(self.getStrPath)

    @QtCore.pyqtSlot()
    def getDate(self):
        global datechoosed
        global channelchoosed
        channelchoosed = self.comboBox_chselect.currentText()
        datechoosed = self.dateEdit.date().toString('yyyy-MM-dd')
        self.mplCanvas.canvas.displayhistory(datechoosed, channelchoosed)

    @QtCore.pyqtSlot(list)
    def getListSerial(self, SerialParam):
        global glb_seriallist
        glb_seriallist = SerialParam
        i = 0
        for x in self.mplCanvas.canvas.datalist:
            if glb_seriallist[0][i] == 2:
                x['enabled'] = True
                x['device'] = glb_seriallist[1][i]
            else:
                x['enabled'] = False
                x['device'] = glb_seriallist[1][i]
            i = i + 1

    
    @QtCore.pyqtSlot(dict)
    def getDictNet(self, NetParam):
        global serverIP
        global serverPort
        global hostIP
        global hostPort
        serverIP = NetParam['serverIP']
        serverPort = NetParam['serverPort']
        hostIP = NetParam['hostIP']
        hostPort = NetParam['hostPort']
 
    @QtCore.pyqtSlot(str)
    def getStrPath(self, PathStr):
        global filepath
        PathStr = unicode(PathStr.toUtf8(), 'utf-8', 'ignore')
        filepath = PathStr
        path = filepath.split("\\")
        path = [x + os.path.sep for x in path]
        path = ''.join(path)
        self.mplCanvas.canvas.filepath = path

    @QtCore.pyqtSlot(dict)
    def getDictFFT(self,FFTParam):
        global fftnum
        global fftfreq
        global fftwindow
        global fftrepeat

        fftnum = FFTParam['num']
        fftfreq = FFTParam['freq']
        fftwindow = FFTParam['window']
        fftrepeat = FFTParam['repeat']

        listrepeatrate = fftrepeat.split('/')
        if len(listrepeatrate) is 1:
            repeatrate = 0
        else:
            repeatrate = float(listrepeatrate[0]) / float(listrepeatrate[1])

        self.mplCanvas.canvas.fftnum = fftnum
        self.mplCanvas.canvas.fftfreq = float(fftfreq)
        self.mplCanvas.canvas.fftwindow = fftwindow
        self.mplCanvas.canvas.fftrepeat = repeatrate

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    app = QtGui.QApplication(sys.argv)
    ui_main = Code_MainWindow()
    ui_main.show()
sys.exit(app.exec_())
