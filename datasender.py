import socket

class tcpclient():
    def __init__(self):
        self.__connected = False
        self.clientsocket = None
        self.needtosend = False

    def connect(self, ip, port):
        self.HOST = ip    # The remote host
        self.PORT = port              # The same port as used by the server
        for res in socket.getaddrinfo(self.HOST, self.PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                self.clientsocket = socket.socket(af, socktype, proto)
                #self.clientsocket.bind(('127.0.0.1', 11560))
            except socket.error, msg:
                self.clientsocket = None
                print msg
                continue
            try:
                self.clientsocket.connect(sa)
            except socket.error, msg:
                self.clientsocket.close()
                self.clientsocket = None
                print msg
                continue
            break
        if self.clientsocket is not None:
            self.__connected = True
            return True
        else:
            self.__connected = False
            return False

    def disconnect(self):
        self.__connected = False
        if self.clientsocket is not None:
            self.clientsocket.close()
            self.clientsocket = None

    def senddata(self, data):
        buf = str(data)
        if not self.__connected:
            if self.connect(self.HOST, self.PORT):
                try:
                    self.clientsocket.send(buf)
                except socket.error, msg:
                    self.clientsocket.close()
        else:
            try:
                self.clientsocket.send(buf)
            except socket.error, msg:
                self.__connected = False
                self.clientsocket.close()
