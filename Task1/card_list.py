import serial

class Tokens():

    serialPort = serial.Serial(port = "COM3", baudrate=9600,
                                bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    serialString = ""

    while(1):

        if (serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            x = serialString.decode('Ascii')
            rep = x.replace("?\r\n", "")
            print(rep)

        
        if rep == "6E536046010080FF"
            print("Access granted.")
        else:
            print("Access denied.")
