import cv2
import numpy as np

camera = cv2.VideoCapture(0)
grabbed, frame = camera.read()

print("Frame width: " + str(np.size(frame, 1)))
print("Frame height: " + str(np.size(frame, 0)))

printCounter = 0

lastFrame = None
thisFrame = None

# Range for amount of edges detected
minEdgeVal = 5
maxEdgeVal = 19

# Range of circle radii measured in pixels
minCircleRadius = 100
maxCircleRadius = 175

while True:
    grabbed, frame = camera.read()

    # Breaks loop if you have reached the end of the video
    if not grabbed:
        break

    # convert image to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if thisFrame is None:
        lastFrame = frame
    else:
        lastFrame = thisFrame
    thisFrame = frame

    grayLastFrame = cv2.cvtColor(lastFrame, cv2.COLOR_BGR2GRAY)
    grayLastFrame = cv2.GaussianBlur(grayLastFrame, (21, 21), 0)

    # compute the absolute difference between the current frame and
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


    # grayFrameDelta = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(frameDelta, minEdgeVal, maxEdgeVal)

    # Finds the circles in the frame
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=minCircleRadius, maxRadius=maxCircleRadius)

    if not circles is None:
        # if (printCounter % 10) == 0:
        #     print("No circles found")
        #     print
        #     printCounter += 1
    # else:
        circles = np.uint16(np.around(circles))
        centers = []

        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(edges,(i[0],i[1]),i[2],(255,255,255),2)
            # draw the center of the circle
            cv2.circle(edges,(i[0],i[1]),2,(255,255,255),3)
            centers.append(i)
            print("Edges circle center at: " + str(i[0]) + ", " + str(i[1]))

        averageX = 0
        averageY = 0

        for i in centers:
            averageX += i[0]
            averageY += i[1]

        averageX /= len(centers)
        averageY /= len(centers)

        print("Average edges circle center: " + str(averageX) + ", " + str(averageY))

    circles = cv2.HoughCircles(frameDelta, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=minCircleRadius, maxRadius=maxCircleRadius)

    if not circles is None:
        # if (printCounter % 10) == 0:
        #     print("No circles found")
        #     print
        #     printCounter += 1
        # else:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(frameDelta, (i[0], i[1]), i[2], (255, 255, 255), 2)
            # draw the center of the circle
            cv2.circle(frameDelta, (i[0], i[1]), 2, (255, 255, 255), 3)
            print("Motion circle center at: " + str(i[0]) + ", " + str(i[1]))

        averageX = 0
        averageY = 0

        for i in centers:
            averageX += i[0]
            averageY += i[1]

        averageX /= len(centers)
        averageY /= len(centers)

        print("Average motion circle center: " + str(averageX) + ", " + str(averageY))

    # Display all the frames
    cv2.imshow('original', frame)
    cv2.imshow('delta', frameDelta)
    cv2.imshow('edges', edges)
    # cv2.imshow('detected circles',grayFrameDelta)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()