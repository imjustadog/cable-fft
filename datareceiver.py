import serial


class serialreceiver():
    def __init__(self):
        self.__newdata = False

    def openserial(self, seriallist):
        for i in seriallist[0]:
            if i:
                serial.Serial(seriallist[1], seriallist[2])

