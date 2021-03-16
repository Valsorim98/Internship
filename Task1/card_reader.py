import serial
#from whitelist import Whitelist

class ACT_230_RFID():
    """Create class for card readers.
    """

    def __init__(self, port):
        """Constructor for card readers.

        Args:
            port (str): Which port is the card reader using.
        """        
        
        self.__serialPort = serial.Serial(port = port, baudrate=9600,
                                    bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    def update(self):
        """Method to get the input from a token, decode it to a string and compare to see if its whitelisted.
        """        

        if (self.__serialPort.in_waiting > 0):
            serialString = self.__serialPort.readline()
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
