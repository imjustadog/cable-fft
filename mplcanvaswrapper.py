# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot
import numpy as np
import struct
import time
import random
import os
import threading
from datetime import datetime
from datetime import timedelta
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DateFormatter
from datasender import tcpclient

Y_MAX = 10
Y_MIN = 1
INTERVAL = 1
INTERVAL_COUNT = 3
MAXCOUNTER = 48


class MplCanvas(FigureCanvas):
    fftnum = 0
    fftfreq = 0
    fftwindow = ''
    fftrepeat = 0
    filepath = ''

    def __init__(self):
        self.fig = Figure(facecolor='w')
        
        self.ax_data = self.fig.add_subplot(211)
        self.ax_data.set_xlabel("time/s")
        self.ax_data.set_ylabel('value')
        # self.ax_data.legend()
        # self.ax_data.set_ylim(-5,5)
        # self.ax_data.xaxis.set_major_locator(MultipleLocator(100))  # every minute is a major locator
        # self.ax_data.xaxis.set_minor_locator(MultipleLocator(10)) # every 10 second is a minor locator
        
        self.ax_freq = self.fig.add_subplot(212)
        self.ax_freq.set_ylabel('frequency')
        # self.ax_freq.legend()
        # self.ax_freq.set_ylim(Y_MIN, Y_MAX)
        self.ax_freq.xaxis.set_major_locator(HourLocator([3, 6, 9, 12, 15, 18, 21]))  # every minute is a major locator
        #self.ax_freq.xaxis.set_minor_locator(SecondLocator([10, 20, 30, 40, 50]))  # every 10 second is a minor locator
        self.ax_freq.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter
        
        self.fig.subplots_adjust(top=0.92, bottom=0.13, left=0.10, right=0.95)

        self.datalist = []
        for i in range(8):
            datadict = {}
            datadict["enabled"] = False
            datadict["device"] = '1-' + str(i + 1)
            datadict['datay'] = []
            datadict['freqcurve'] = None
            datadict['freqpoint'] = None

            self.datalist.append(datadict)

        self.datay = []
        self.mag = []

        self.curveObj_data = None
        self.clickObj_data = None
        self.annotate_data = None
        self.pointObj_data = None

        self.clickObj_freq = None
        self.annotate_freq = None

        '''
        self.curveObj_freq = None  # draw object
        '''

        self.cid = None
        
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    
    def displayhistory(self, year, month, day):
        filepathym = self.filepath + year + u'年' + \
            os.path.sep + month + u'月'
        if os.path.exists(filepathym):
            foldernamelisttemp = os.listdir(filepathym)
            for folder in foldernamelisttemp:
                date = folder.split(' ')[0]
                if date.split('-')[2] is day:
                    filepathtime = filepathym + os.path.sep + folder + os.path.sep + folder
                    traversefolder(filepathtime, self.datalist, self.fftnum, self.fftrepeat, self.fftfreq)

    def plot_freq(self, datax, counter):
        for x in self.datalist:
            if x['enabled']:
                if x['freqcurve'] is None:
                    # create draw object once
                    x['freqcurve'], = self.ax_freq.plot(
                                                        np.array(datax),
                                                        np.array(x['datay']),
                                                        '-',
                                                        picker=False,
                                                        linewidth=2.5
                                                        )

                    x['freqpoint'], = self.ax_freq.plot(
                                                        np.array(datax),
                                                        np.array(x['datay']),
                                                        'o',
                                                        picker=5,
                                                        mew=0
                                                        )
                else:
                    # update data of draw object
                    x['freqcurve'].set_data(np.array(datax), np.array(x['datay']))
                    x['freqpoint'].set_data(np.array(datax), np.array(x['datay']))
        # update limit of X axis,to make sure it can move
        if counter >= MAXCOUNTER:
            self.ax_freq.set_xlim(datax[0], datax[-1])
        else:
            self.ax_freq.set_xlim(datax[0], datax[0]+timedelta(hours=24))
        ticklabels = self.ax_freq.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)
        self.draw()

    def click_data(self, device, time):
        path = self.filepath + "1#" + device + ".tim"
        self.mag, self.datay = fft(path, self.fftnum, self.fftrepeat)
        self.plot_data()
        
    def plot_data(self):
        if self.annotate_data is not None:
            self.annotate_data.remove()
            self.annotate_data = None
        if self.clickObj_data is not None:
            self.clickObj_data.remove()
            self.clickObj_data = None
        datax = range(len(self.datay))
        datax = [x / self.fftfreq for x in datax]
        self.ax_data.set_xlabel("time/s")
        self.ax_data.set_xlim(datax[0], datax[-1])
        if self.curveObj_data is None:
            self.curveObj_data,  = self.ax_data.plot(
                                                     np.array(datax),
                                                     np.array(self.datay),
                                                     '-',
                                                     picker=False,
                                                     linewidth=1,
                                                     color='b'
                                                    )

            self.pointObj_data, = self.ax_data.plot(
                                                    np.array(datax),
                                                    np.array(self.datay),
                                                    'o',
                                                    picker=5,
                                                    mew=0,
                                                    markersize=1.5,
                                                    color='b'
                                                    )
        else:
            self.curveObj_data.set_data(np.array(datax), np.array(self.datay))
            self.pointObj_data.set_data(np.array(datax), np.array(self.datay))
        self.draw()
    
    def plot_FFT(self):
        if self.annotate_data is not None:
            self.annotate_data.remove()
            self.annotate_data = None
        if self.clickObj_data is not None:
                self.clickObj_data.remove()
                self.clickObj_data = None
        if self.curveObj_data is None:
            pass
        else:
            datax = range(int(self.fftnum / 2.56))
            datax = [x * self.fftfreq / self.fftnum for x in datax]
            self.ax_data.set_xlim(datax[0], datax[-1])
            self.ax_data.set_xlabel("frequent/Hz")
            self.curveObj_data.set_data(np.array(datax), np.array(self.mag))
            self.pointObj_data.set_data(np.array(datax), np.array(self.mag))
        self.draw()
        
    def onclick(self, event):
        xdata = event.artist.get_xdata()[event.ind][0]
        ydata = event.artist.get_ydata()[event.ind][0]
        for x in self.datalist:
            if event.artist == x['freqpoint']:
                if self.clickObj_freq is None:
                    self.clickObj_freq, = self.ax_freq.plot(xdata, ydata, '*', markersize=15, mew=0)
                else:
                    self.clickObj_freq.set_data(xdata, ydata)

                if self.clickObj_data is not None:
                    self.clickObj_data.remove()
                    self.clickObj_data = None
                if self.annotate_data is not None:
                    self.annotate_data.remove()
                    self.annotate_data = None
                if self.annotate_freq is not None:
                    self.annotate_freq.remove()
                str_datay = str(round(ydata, 2))
                self.annotate_freq = self.ax_freq.annotate(str_datay, xy=(xdata, ydata))

                time_clicked = [xdata.hour, xdata.minute, xdata.second]
                print time_clicked
                self.click_data(x['device'],time_clicked)
                break
        
        if event.artist == self.pointObj_data:
            if self.clickObj_data is None:
                self.clickObj_data, = self.ax_data.plot(xdata, ydata, '*', markersize=8, mew=0)
            else:
                self.clickObj_data.set_data(xdata, ydata)
            if self.annotate_data is not None:
                self.annotate_data.remove()
            str_datay = str(round(float(ydata), 2))
            str_datax = str(round(float(xdata), 2))
            self.annotate_data = self.ax_data.annotate(str_datax+','+str_datay, xy=(xdata, ydata))
        self.draw()


class MplCanvasWrapper(QtGui.QWidget):
    def __init__(self, parent=None):
        pyplot.style.use('bmh')
        QtGui.QWidget.__init__(self, parent)
        self.client = tcpclient()
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.__generating = False
        self.__exit = False
        self.dataX = []
        self.counter = 0
        self.foldernamelist = []
    
    def showDataorFreq(self):
        if self.canvas.ax_data.get_xlabel() == "time/s":
            self.canvas.plot_FFT()
        else:
            self.canvas.plot_data()   
    
    def startPlot(self):
        if self.canvas.cid is not None:
            self.canvas.fig.canvas.mpl_disconnect(self.canvas.cid)
        self.dataX = []
        for x in self.canvas.datalist:
            x['datay'] = []
        self.counter = 0
        self.__exit = False
        self.__generating = True

    def pausePlot(self):
        self.canvas.cid = self.canvas.fig.canvas.mpl_connect('pick_event', self.canvas.onclick)
        self.__generating = False

    def initDataGenerator(self):
        self.tData = threading.Thread(name="dataGenerator", target=self.generateData)
        self.tData.start()

    def releasePlot(self):
        self.__exit  = True

    def generateData(self):

        filepathym = self.canvas.filepath + str(time.localtime().tm_year) + u'年' + \
                     os.path.sep + str(time.localtime().tm_mon) + u'月'
        if os.path.exists(filepathym):
            self.foldernamelist = os.listdir(filepathym)

        while True:
            if self.__exit:
                break
            newData = self.readfilename()
            if newData:
                newTime = datetime.now()
                self.dataX.append(newTime)
                if self.client.needtosend:
                    self.client.senddata(newData)
                if self.__generating:
                    self.canvas.plot_freq(self.dataX, self.counter)
                    if self.counter >= MAXCOUNTER:
                        self.dataX.pop(0)
                        for x in self.canvas.datalist:
                            if x['enabled']:
                                x['datay'].pop(0)
                    else:
                        self.counter += 1
            time.sleep(INTERVAL * INTERVAL_COUNT)

    def readfilename(self):
        flag = False
        filepathym = self.canvas.filepath + str(time.localtime().tm_year) + u'年' + \
            os.path.sep + str(time.localtime().tm_mon) + u'月'

        if os.path.exists(filepathym):
            foldernamelisttemp = os.listdir(filepathym)
            for folder in foldernamelisttemp:
                if folder not in self.foldernamelist:
                    flag = True
                    filepathtime = filepathym + os.path.sep + folder + os.path.sep + folder
                    break
            self.foldernamelist = foldernamelisttemp
            if not flag:
                return False
            traversefolder(filepathtime, self.canvas.datalist,
                           self.canvas.fftnum, self.canvas.fftrepeat, self.canvas.fftfreq)

        return flag


def fft(path, fftnum, fftrepeat):
    count = 0
    datay = []
    fileinfo = os.stat(path)
    time.localtime(fileinfo.st_ctime)
    f = open(path, "rb")
    try:
        while True:
            a_pack = f.read(2)
            if not a_pack:
                break
            itemp, = struct.unpack('h', a_pack)
            dtemp = itemp / 6.5536
            datay.append(dtemp)
            count += 1
    finally:
        f.close()

    index = 0
    magnitude = []
    while True:
        data = datay[index:index + fftnum]
        data = np.abs(np.fft.fft(data, fftnum)) / (fftnum / 2)
        magnitude.append(data)
        index += int(fftnum * (1 - fftrepeat))
        if index + fftnum > count:
            break

    mag = sum(np.array(magnitude)) / len(magnitude)
    mag = list(mag)
    mag = mag[0: int(fftnum / 2.56)]

    return mag, datay


def findfreq(mag, fftnum, fftfreq):
    rate = []
    for i in range(len(mag) - 1):
        rate.append(mag[i + 1] - mag[i])
    freq = []
    for i in range(len(rate) - 1):
        if rate[i] > 0 and rate[i + 1] < 0 and mag[i + 1] > 50:
            freq.append(i + 1)

    if len(freq) >= 2:
        freq_step2 = freq[1] * fftfreq / fftnum
        freq_result = freq_step2 / 2
    else:
        freq_result = freq[0] * fftfreq / fftnum
    # freq_result = freq[1] * self.canvas.fftfreq / self.canvas.fftnum
    # freq_result = random.uniform(1, 5)
    return freq_result


def traversefolder(filepathtime, datalist, fftnum, fftrepeat, fftfreq):
    for x in datalist:
        if x['enabled']:
            path = filepathtime + '#' + x['device'] + '.tim'
            if not os.path.exists(path):
                continue
            mag, ty = fft(path, fftnum, fftrepeat)
            freq_result = findfreq(mag, fftnum, fftfreq)
            x['datay'].append(freq_result)

