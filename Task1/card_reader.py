import serial
import serial.tools.list_ports
from whitelist import Whitelist

class ACT_230_RFID():
    """Create class for card readers.
    """

    comPorts = list(serial.tools.list_ports.comports())
    print(comPorts)

    def __init__(self, port):
        """Constructor for card readers.

        Args:
            port (str): Which port is the card reader using.
        """        
        
        port = port
        __serialPort = serial.Serial(port = "COM3", baudrate=9600,
                                    bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    def update(self):
        """Method to get the input from a token, decode it to a string and compare to see if its whitelisted.
        """        

        if (self.serialPort.in_waiting > 0):
            serialString = self.serialPort.readline()
            x = serialString.decode('Ascii')
            rep = x.replace("?\r\n", "")
            print(rep)

            if rep == "6E536046010080FF":
                print("Access granted.")
            else:
                print("Access denied.")


        #for i in Whitelist().arr_cards:
        #    rep == i
        #    print(rep)
