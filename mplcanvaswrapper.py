# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot
import numpy as np
import struct
import time
import operator
import os
import threading
from datetime import datetime
from datetime import timedelta
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DateFormatter
from datasender import tcpclient

Y_MAX = 10
Y_MIN = 1
INTERVAL = 1
INTERVAL_COUNT = 60
MAXCOUNTER = 48

send_lock = threading.Lock()


class MplCanvas(FigureCanvas):
    fftnum = 0
    fftfreq = 0
    fftwindow = ''
    fftrepeat = 0
    filepath = ''
    clickdate = []
    test = ''

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
        for i in range(16):
            datadict = {}
            datadict["enabled"] = False
            datadict["device"] = ''
            datadict['datay'] = []
            datadict['freqcurve'] = None
            datadict['freqpoint'] = None
            self.datalist.append(datadict)

        self.datalisthistory = self.datalist

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
    
    def displayhistory(self, date, channel):
        dataX = []

        thechannel = int(channel.split(' ')[1])
        i = 0
        for x in self.datalisthistory:
            x['datay'] = []
            x['device'] = self.datalist[i]['device']
            if thechannel == i + 1:
                x['enabled'] = True
            else:
                x['enabled'] = False
            i += 1

        dates = date.split('-')
        year = dates[0]
        month = str(int(dates[1]))
        day = dates[2]
        filepathym = self.filepath + year + u'年' + \
                     os.path.sep + month + u'月'
        self.clickdate = [filepathym, date]

        if os.path.exists(filepathym):
            foldernamelisttemp = os.listdir(filepathym)
            foldernamelisttemp.sort()
            for folder in foldernamelisttemp:
                folder = str(folder)
                if folder.find('.') > 0:
                    continue
                dateandtime = folder.split(' ')
                date = dateandtime[0].split('-')
                clock = dateandtime[1].split('-')
                if date[2] == day:
                    dataX.append(datetime(int(date[0]), int(date[1]), int(date[2]),
                                          int(clock[0]), int(clock[1]), int(clock[2])))
                    filepathtime = filepathym + os.path.sep + folder + os.path.sep + folder
                    self.test = filepathtime
                    traversefolder(filepathtime, self.datalisthistory, self.fftnum, self.fftrepeat, self.fftfreq, self.fftwindow)
            if dataX != []:
                self.plot_freq(self.datalisthistory, dataX, 0)

    def plot_freq(self, datalist, datax, counter):
        clear_freq_annotate(self)
        for x in datalist:
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
            else:
                if x['freqcurve'] is not None:
                    x['freqcurve'].remove()
                    x['freqpoint'].remove()
                    x['freqcurve'] = None
                    x['freqpoint'] = None
        # update limit of X axis,to make sure it can move
        if counter >= MAXCOUNTER:
            self.ax_freq.set_xlim(datax[0], datax[-1])
        else:
            self.ax_freq.set_xlim(datax[0], datax[0]+timedelta(hours=24))
        #y_all = sum([x['datay'] for x in datalist if x['enabled']], [])
        #self.ax_freq.set_ylim(min(y_all), max(y_all))
        self.ax_freq.set_ylim(3, 7)
        ticklabels = self.ax_freq.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)
        self.draw()

    def click_data(self, device, clicktime):
        foldername = self.clickdate[1] + ' ' + clicktime
        path = self.clickdate[0] + os.path.sep + foldername + os.path.sep + foldername + "#" + device + ".tim"
        self.mag, self.datay = fft(path, self.fftnum, self.fftrepeat, self.fftwindow)
        self.plot_data()
        
    def plot_data(self):
        clear_data_annotate(self)
        datax = range(len(self.datay))
        datax = [x / self.fftfreq for x in datax]
        self.ax_data.set_xlabel("time/s")
        self.ax_data.set_xlim(datax[0], datax[-1])
        self.ax_data.set_ylim(min(self.datay), max(self.datay))
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
        clear_data_annotate(self)
        if self.curveObj_data is None:
            pass
        else:
            datax = range(int(self.fftnum / 2))
            datax = [x * self.fftfreq / self.fftnum for x in datax]
            self.ax_data.set_xlim(datax[0], datax[-1])
            self.ax_data.set_ylim(0, max(self.mag))
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

                clear_data_annotate(self)
                clear_freq_annotate(self)

                str_datay = str(round(ydata, 2))
                self.annotate_freq = self.ax_freq.annotate(str_datay, xy=(xdata, ydata))

                clicktime = xdata.strftime('%H-%M-%S')
                self.click_data(x['device'], clicktime)
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
    signal_tcpsend = QtCore.pyqtSignal(bool)

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

        self.signal_tcpsend.connect(self.sendtoremote)
        self.__generating = False
        self.__exit = False
        self.dataX = []
        self.counter = 0
        self.foldernamelist = []
        self.canvas.cid = self.canvas.fig.canvas.mpl_connect('pick_event', self.canvas.onclick)

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
        self.tHeartBeat = threading.Thread(name="heartbeatGenerator", target=self.generateHeartBeat)
        self.tHeartBeat.start()

    def releasePlot(self):
        self.__exit  = True

    def generateHeartBeat(self):
        while True:
            if self.__exit:
                break
            self.signal_tcpsend.emit(False)
            time.sleep(30)


    def generateData(self):
        while True:
            self.filepathym = self.canvas.filepath + str(time.localtime().tm_year) + u'年' + \
                os.path.sep + str(time.localtime().tm_mon) + u'月'
            if self.__exit:
                break
            isnewData = self.readfilename()
            if isnewData:
                newTime = datetime.now()
                self.dataX.append(newTime)
                self.signal_tcpsend.emit(True)
                if self.__generating:
                    self.canvas.plot_freq(self.canvas.datalist, self.dataX, self.counter)
                    if self.counter >= MAXCOUNTER:
                        self.dataX.pop(0)
                        for x in self.canvas.datalist:
                            if x['enabled']:
                                x['datay'].pop(0)
                    else:
                        self.counter += 1
            time.sleep(60)


    def readfilename(self):
        flag = False
        if os.path.exists(self.filepathym):
            foldernamelisttemp = os.listdir(self.filepathym)
            for folder in foldernamelisttemp:
                if folder.find('.') > 0:
                    continue
                if folder not in self.foldernamelist and self.foldernamelist != []:
                    flag = True
                    filepathtime = self.filepathym + os.path.sep + folder + os.path.sep + folder
                    break
            self.foldernamelist = foldernamelisttemp
            if not flag:
                return False
            time.sleep(900)
            traversefolder(filepathtime, self.canvas.datalist,
                           self.canvas.fftnum, self.canvas.fftrepeat, self.canvas.fftfreq, self.canvas.fftwindow)

        return flag

    @QtCore.pyqtSlot(bool)
    def sendtoremote(self, isData):
        global send_lock
        if send_lock.acquire():
            if isData:
                self.client.senddata(self.canvas.datalist)
            else:
                self.client.senddata('E')
            send_lock.release()


def fft(path, fftnum, fftrepeat,fftwindow):
    count = 0
    datay = []
    f = open(path, "rb")
    try:
        while True:
            a_pack = f.read(2)
            if not a_pack:
                break
            itemp, = struct.unpack('h', a_pack)
            dtemp = itemp / (-4.8)
            datay.append(dtemp)
            count += 1
    finally:
        f.close()

    index = 0
    magnitude = []
    while True:
        data = datay[index:index + fftnum]
        if fftwindow == u"汉宁窗":
            win = np.hanning(fftnum)
            data = np.array(data)
            data = np.multiply(data,win)
        data = np.abs(np.fft.fft(data, fftnum)) / (fftnum / 2)
        magnitude.append(data)
        index += int(fftnum * (1 - fftrepeat))
        if index + fftnum > count:
            break

    mag = sum(np.array(magnitude)) / len(magnitude)
    mag = list(mag)
    mag = mag[0: int(fftnum / 2)]
    mag[0] = 0

    return mag, datay


def findfreq(mag, fftnum, fftfreq):
    freq = []
    glo_max_amp = max(mag)
    margin_freq = 0.3
    margin_count = int(margin_freq * fftnum / fftfreq)
    max_amp = 0
    min_amp = glo_max_amp
    find_start = 0
    state = 'findmin'
    limit_range = int(30 * fftnum / fftfreq)

    for i in range(limit_range):
        if state == 'findmax':
            if mag[i] > max_amp:
                max_amp = mag[i]
                find_start = i
            elif i - find_start > margin_count and mag[find_start] > 4 * sum(mag[find_start:i]) / (i - find_start):
                state = 'findmin'
                freq.append(find_start)
                find_start = i
                max_amp = 0

            else:
                pass
        
        elif state == 'findmin':
            if i - find_start > margin_count:
                state = 'findmax'
                find_start = i
                min_amp = glo_max_amp
            elif mag[i] < min_amp:
                min_amp = mag[i]
                find_start = i
            else:
                pass

        else:
            pass

    choose_end = len(freq)

    if choose_end == 0:
        return 0

    elif choose_end == 1:
        return freq[0] * fftfreq / fftnum

    freq_main = []
    for r in range(2):
        rate = float(r + 2)/(r + 1)
        for i in range(choose_end - 1):
            for j in range(i + 1, choose_end):
                freq_dict = {}
                freq_dict['margin'] = abs(rate * freq[i] - freq[j]) * fftfreq / fftnum / (r + 2)
                freq_dict['freq'] = freq[i] * fftfreq / fftnum / (r + 1)
                freq_dict['i'] = freq[i] * fftfreq / fftnum
                freq_dict['j'] = freq[j] * fftfreq / fftnum
                freq_dict['magi'] = mag[freq[i]]
                freq_dict['magj'] = mag[freq[j]]
                freq_main.append(freq_dict)

    freq_sort_margin = sorted(freq_main, key=operator.itemgetter('margin'))
    for index, item in enumerate(freq_sort_margin):
        if item['margin'] < 0.6:
            if index < len(freq_sort_margin) - 1:
                if item['magi'] < 15 or item['magj'] < 15:
                    continue
                elif item['freq'] < 4 or item['freq'] > 7:
                    continue
                else:
                    return item['freq']
            else:
                return item['freq']

    return freq[0] * fftfreq / fftnum


def traversefolder(filepathtime, datalist, fftnum, fftrepeat, fftfreq, fftwindow):
    for x in datalist:
        if x['enabled']:
            path = filepathtime + '#' + x['device'] + '.tim'
            if not os.path.exists(path):
                continue
            mag, ty = fft(path, fftnum, fftrepeat, fftwindow)
            freq_result = findfreq(mag, fftnum, fftfreq)
            x['datay'].append(freq_result)


def clear_data_annotate(self):
    if self.annotate_data is not None:
        self.annotate_data.remove()
        self.annotate_data = None
    if self.clickObj_data is not None:
        self.clickObj_data.remove()
        self.clickObj_data = None


def clear_freq_annotate(self):
    if self.clickObj_freq is not None:
        self.clickObj_freq.remove()
        self.clickObj_freq = None
    if self.annotate_freq is not None:
        self.annotate_freq.remove()
        self.annotate_freq = None