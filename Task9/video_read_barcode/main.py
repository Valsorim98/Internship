#!/usr/bin/env python3
# -*- coding: utf8 -*-

import cv2  # Read image/video input
#from pyzbar.pyzbar import decode    # Read barcode
from pyzbar import pyzbar
from PIL import Image
import numpy as np
import time

def main():

    path = "C:\\Users\\m1ro0\\Documents\\Git_repos\\Work\\Task9\\video_read_barcode\\donkger.png"
    blank_path = "C:\\Users\\m1ro0\\Documents\\Git_repos\\Work\\Task9\\video_read_barcode\\white_image.png"

    img = cv2.imread(path)
    white_image = cv2.imread(blank_path)

    barcode = pyzbar.decode(img)

    for code in barcode:
        x, y, w, h = code.rect
        
        # Draw a rectangle on the barcode
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        barcode_data = code.data.decode("utf-8")
        print(barcode_data)
        barcode_type = code.type
        print(barcode_type)

        # Type the barcode data and type over the barcode
        text = f"{barcode_data}, {barcode_type}"
        cv2.putText(img, text,(x+110,y-10),cv2.FONT_ITALIC,0.5,(0,0,255),2)
    
    # Show the window
    #big = Image.new('RGB', (800, 800))
    # big.putdata(img)

    white_image = np.zeros([550,800,3],dtype=np.uint8)
    white_image.fill(255)
    result = cv2.imwrite(blank_path, white_image)
    if result == True:
        print("done")
    else:
        print("cant save the file")

    #white_image.paste(img)
    cv2.imshow("Testing", white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # Read video
    # cap = cv2.VideoCapture(0)
    # cap.set(3, 640) # 3 Width
    # cap.set(4, 480) # 4 Height

    # # used_codes = []

    # camera = True

    # while camera == True:
    #     success, frame = cap.read()

    #     for barcode in pyzbar.decode(frame):
    #         # if barcode.data.decode('utf-8') not in used_codes:
    #         print("Approved!")
    #         print(barcode.type)
    #         print(barcode.data.decode('utf-8'))
    #         # used_codes.append(barcode.data.decode('utf-8'))
    #         time.sleep(3)

    # cv2.imshow("Testing", frame)
    # cv2.waitKey(1)

if __name__ == "__main__":
    main()
