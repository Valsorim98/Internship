import cv2  # Read image/video input
from pyzbar.pyzbar import decode    # Read barcode
from pyzbar import pyzbar
import numpy as np
import time

def main():
    """Function to decode barcodes from a live video.

    Returns:
        list: The decoded ID and baudrate of the barcode.
    """

    # Read video
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # 3 Width, 640 pixels
    cap.set(4, 480) # 4 Height, 480 pixels

    # List to store device ID and baudrate
    device_settings = []
    camera = True

    while camera == True:
        success, frame = cap.read()

        # Decode the barcode
        for barcode in pyzbar.decode(frame):
            print("Approved!")
            print(barcode.type)
            print(barcode.data.decode('utf-8'))

            # The barcode data as a string:
            bc_data = "Donkger/XY-MD02/9600/2" # Place barcode.data.decode('utf-8') here
            bc_data_split = bc_data.split("/")[-0:]

            manufacturer = bc_data_split[0]
            print(f"Manufacturer: {manufacturer}")
            model = bc_data_split[1]
            print(f"Model: {model}")

            # Sleep for two seconds after a barcode is given
            time.sleep(2)

            # Check if the given barcode is valid
            if model != "XY-MD02" or manufacturer != "Donkger":
                print("Wrong barcode! Insert a valid one.")
                break
            if int(bc_data_split[3]) < 1 or int(bc_data_split[3]) > 247:
                print("Invalid ID number! Insert a valid barcode.")
                break
            if int(bc_data_split[2]) != 9600 and int(bc_data_split[2]) != 14400 and int(bc_data_split[2]) != 19200:
                print("Invalid baudrate! Insert a valid barcode.")
                break

            # If the barcode is valid to store the id and baudrate in a list
            else:
                id = int(bc_data_split[3])
                baudrate = int(bc_data_split[2])
                print(f"ID: {id}")
                print(f"Baudrate: {baudrate}")

                # If the list is empty to append with id and baudrate
                if not device_settings:
                    device_settings.append(id)
                    device_settings.append(baudrate)
                print(device_settings)
                camera = False      # When closing the window an error pops up

        # Shows the window
        cv2.imshow("Video capture", frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
