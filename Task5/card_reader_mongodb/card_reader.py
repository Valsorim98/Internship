import serial

class ACT230():
    """Create class for card readers.
    """

    def __init__(self, port, reader_id):
        """Constructor for card readers.

        Args:
            port (str): Which port is the card reader using.
        """        
        
        self.__serialPort = serial.Serial(port = port, baudrate=9600,
                                    bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

        self._reader_id = 1914

    # Make the reader_id argument of the constructor 'read-only'
    @property
    def _reader_id(self):
        return self._reader_id

    def set_card_cb(self, cb):

        self.__card_reader_cb = cb

    def update(self):
        """Method to get the input from a token and decode it to a string.
        """        

        if (self.__serialPort.in_waiting > 0):
            byte_data = self.__serialPort.readline()
            str_data = byte_data.decode('Ascii')
            card_id = str_data.replace("?\r\n", "")

            if self.__card_reader_cb is not None:
                self.__card_reader_cb(card_id)
