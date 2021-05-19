> # Documentation for video_read_barcode project.

* The live video barcode decoding program runs from main function in main.py.

* The barcode decoding from image program runs from read_image.py

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the programs:

* opencv-python - install with command in cmd:
```py
pip install opencv-python
```

* pyzbar - install with command in cmd:
```py
pip install pyzbar
```

---
* The live video barcode decoding runs from main.py:

```py
def main():

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
```

* The barcode decoding from an image runs from read_image.py:

```py
def main():

    # Change the path
    path = "C:\\Users\\m1ro0\\Documents\\Git_repos\\Work\\Task9\\video_read_barcode\\donkger.png"

    # Read the image
    img = cv2.imread(path)

    # Decode the barcode from the image
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
        cv2.putText(img, text,(x+150,y-10),cv2.FONT_ITALIC,0.5,(0,0,255),2)

    # Create white image for a background
    white_image = np.zeros([400,900,3],dtype=np.uint8)
    white_image.fill(255)

    # Set x,y offset for the smaller image
    x_offset=100
    y_offset=80
    white_image[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img

    # Show the window
    cv2.imshow("Decode from image", white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
