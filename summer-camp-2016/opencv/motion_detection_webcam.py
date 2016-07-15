import cv2
import numpy

camera = cv2.VideoCapture(0)
grabbed, frame = camera.read()

if grabbed:
    print("Frame width: " + str(numpy.size(frame, 1)))
    print("Frame height: " + str(numpy.size(frame, 0)))

thisFrame = None
lastFrame = None

while True:
    (grabbed, frame) = camera.read()

    # convert image to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Save frames to compare to on next iteration
    if thisFrame is None:
        lastFrame = frame
    else:
        lastFrame = thisFrame
    thisFrame = frame

    grayLastFrame = cv2.cvtColor(lastFrame, cv2.COLOR_BGR2GRAY)
    grayLastFrame = cv2.GaussianBlur(grayLastFrame, (21, 21), 0)

    # compute the absolute difference between the current frame and
    # first frame
    frameDelta = cv2.absdiff(grayLastFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _, x) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        # if the contour is too small, ignore it
        # if cv2.contourArea(c) < 100:
        #     continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('original', frame)
    cv2.imshow('delta', frameDelta)

    if cv2.waitKey(1) == 27:
        exit(0)