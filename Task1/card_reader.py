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
