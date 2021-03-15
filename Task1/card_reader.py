import serial

class ACT_230_RFID():

    def __init__(self, port, baudrate, bytesize, timeout, stopbits):
        """Constructor for card readers.

        Args:
            port (str): Which port is the card reader using.
            baudrate (int): The baudrate of the card reader.
            bytesize (int): The bytesize of the card reader.
            stopbits (int): The card reader is using one stopbit.
        """

        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits

    def update(self):

        serialString = ""

        serialPort = serial.Serial(port = "COM3", baudrate=9600,
                                    bytesize=8, stopbits=serial.STOPBITS_ONE)

        if (serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            x = serialString.decode('Ascii')
            rep = x.replace("?\r\n", "")
            print(rep)
            if rep == "6E536046010080FF":
                print("Access granted.")
            else:
                print("Access denied.")
