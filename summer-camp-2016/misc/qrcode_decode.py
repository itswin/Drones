import zbar
import PIL.Image as Image
import cv2
from bardecoder import Barcode
import numpy as np

scanner = zbar.ImageScanner()
scanner.parse_config('enable')


cam = cv2.VideoCapture(0)

while True:
    (grabbed_frame, frame) = cam.read()

    if grabbed_frame:
        # obtain image data
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pil = Image.fromarray(gray)
        width, height = pil.size
        raw = pil.tobytes()

        # wrap image data
        image = zbar.Image(width, height, 'Y800', raw)

        # scan the image for barcodes
        scanner.scan(image)

        barcodes = []
        # extract results
        for symbol in image:
            barcode = Barcode(symbol)
            barcodes.append(barcode)
            # do something useful with results
            print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

        if len(barcodes) > 0:
            frameCenterX = np.size(frame, 1) / 2
            frameCenterY = np.size(frame, 0) / 2
            i = barcodes[0]
            x = (i.location[0][0] + i.location[1][0] + i.location[2][0] + i.location[3][0]) / 4
            y = (i.location[0][1] + i.location[1][1] + i.location[2][1] + i.location[3][1]) / 4
            print(x,y)
            print("Frame center")
            print(frameCenterX, frameCenterY)

            xDistance = frameCenterX - x
            yDistance = frameCenterY - y

            print(xDistance, yDistance)


        cv2.imshow("Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break