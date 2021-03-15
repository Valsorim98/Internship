import serial
from whitelist import Whitelist

class ACT_230_RFID():

    serialPort = serial.Serial(port = "COM3", baudrate=9600,
                                bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    def update(self):

        while(1):

            if (self.serialPort.in_waiting > 0):
                serialString = self.serialPort.readline()
                x = serialString.decode('Ascii')
                rep = x.replace("?\r\n", "")
                print(rep)

                if rep == "6E536046010080FF":
                    print("Access granted.")
                else:
                    print("Access denied.")


           # for i in Whitelist().arr_cards:
           #     rep == i.
