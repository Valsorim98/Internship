#!/usr/bin/env python3
# -*- coding: utf8 -*-

import cv2  # Read image/video input
from pyzbar.pyzbar import decode    # Read barcode
from pyzbar import pyzbar
import numpy as np
import time

def main():
    """Main function.
    """

    # Read video
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # 3 Width, 640 pixels
    cap.set(4, 480) # 4 Height, 480 pixels

    camera = True

    while camera == True:
        success, frame = cap.read()

        # Decode the barcode
        for barcode in pyzbar.decode(frame):
            print("Approved!")
            print(barcode.type)
            print(barcode.data.decode('utf-8'))
            time.sleep(3)

        # Shows the window
        cv2.imshow("Video capture", frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
