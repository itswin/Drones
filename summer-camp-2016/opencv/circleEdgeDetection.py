import cv2
import numpy
from mergeSort import mergeSort

camera = cv2.VideoCapture(0)
grabbed, frame = camera.read()

if grabbed:
    print("Frame width: " + str(numpy.size(frame, 1)))
    print("Frame height: " + str(numpy.size(frame, 0)))

printCounter = 0

lastFrame = None
thisFrame = None

# Range for amount of edges detected
minEdgeVal = 5
maxEdgeVal = 20

# Range of circle radii measured in pixels
minCircleRadius = 60
maxCircleRadius = 100

while True:
    grabbed, frame = camera.read()

    # Breaks loop if you have reached the end of the video
    if not grabbed:
        break

    # convert image to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Save frames to compare to on next iteration
    if thisFrame is None:
        lastFrame = frame
    else:
        lastFrame = thisFrame
    thisFrame = frame

    # Grays the last frame and then blurs it
    grayLastFrame = cv2.cvtColor(lastFrame, cv2.COLOR_BGR2GRAY)
    grayLastFrame = cv2.GaussianBlur(grayLastFrame, (21, 21), 0)

    # compute the absolute difference between the current frame and
    frameDelta = cv2.absdiff(grayLastFrame, gray)

    # Find edges after motion detection
    edges = cv2.Canny(frameDelta, minEdgeVal, maxEdgeVal)

    # Dilate/erode the edges to make circles easier to detect
    kernel = numpy.ones((5, 5), numpy.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.Canny(edges, minEdgeVal, maxEdgeVal)

    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.erode(edges,kernel,iterations=1)
    edges = cv2.Canny(edges, minEdgeVal, maxEdgeVal)

    # Finds the circles in the frame
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=minCircleRadius, maxRadius=maxCircleRadius)

    # Draws the median circle in the edges frame
    if not circles is None:
        circles = numpy.uint16(numpy.around(circles))
        # Lists to save center (x,y) and radius
        listX = []
        listY = []
        listR = []

        # Save the values into the corresponding lists
        for i in circles[0, :]:
            # draw the outer circle
            # cv2.circle(edges, (i[0], i[1]), i[2], (255, 255, 255), 2)
            # draw the center of the circle
            # cv2.circle(edges, (i[0], i[1]), 2, (255, 255, 255), 3)

            # Save the centers and radii
            listX.append(i[0])
            listY.append(i[1])
            listR.append(i[2])
            print("Edges circle center at: " + str(i[0]) + ", " + str(i[1]))

        # Sort the centers and radii
        sortedX = mergeSort(listX)
        sortedY = mergeSort(listY)
        sortedR = mergeSort(listR)

        # Find the medians
        medianX = sortedX[len(sortedX) // 2]
        medianY = sortedY[len(sortedY) // 2]
        medianR = sortedR[len(sortedR) // 2]

        # Draw/print the median circle
        cv2.circle(edges, (medianX, medianY), medianR, (255, 255, 255), 2)
        cv2.circle(edges, (medianX, medianY), 2, (255, 255, 255), 2)
        print("Median edges circle center: " + str(medianX) + ", " + str(medianY) + " with radius " + str(medianR))
        cv2.imshow("Edges Circle", edges)

    # Find circles in the motion frame
    circles = cv2.HoughCircles(frameDelta, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=minCircleRadius, maxRadius=maxCircleRadius)

    # Draws the median circle in the motion frame
    if not circles is None:
        circles = numpy.uint16(numpy.around(circles))
        # Lists to save center (x,y) and radius
        listX = []
        listY = []
        listR = []

        # Save the values into the corresponding lists
        for i in circles[0, :]:
            # draw the outer circle
            # cv2.circle(edges, (i[0], i[1]), i[2], (255, 255, 255), 2)
            # draw the center of the circle
            # cv2.circle(edges, (i[0], i[1]), 2, (255, 255, 255), 3)

            # Save the centers and radii
            listX.append(i[0])
            listY.append(i[1])
            listR.append(i[2])
            print("Motion circle center at: " + str(i[0]) + ", " + str(i[1]))

        # Sort the centers and radii
        sortedX = mergeSort(listX)
        sortedY = mergeSort(listY)
        sortedR = mergeSort(listR)

        # Find the medians
        medianX = sortedX[len(sortedX) // 2]
        medianY = sortedY[len(sortedY) // 2]
        medianR = sortedR[len(sortedR) // 2]

        # Draw/print the median circle
        cv2.circle(frameDelta, (medianX, medianY), medianR, (255, 255, 255), 2)
        cv2.circle(frameDelta, (medianX, medianY), 2, (255, 255, 255), 2)
        print("Median motion circle center: " + str(medianX) + ", " + str(medianY) + " with radius " + str(medianR))
        cv2.imshow("Motion Circle", frameDelta)

    # Display all the frames
    cv2.imshow('original', frame)
    cv2.imshow('delta', frameDelta)
    cv2.imshow('edges', edges)
    # cv2.imshow('detected circles',grayFrameDelta)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()