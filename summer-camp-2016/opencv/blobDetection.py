import cv2
import numpy

list = []
print list[0 // 2]

im = cv2.imread("./images/BlobTest.jpg")

# im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# im = cv2.Canny(im, 30, 50)

# kernel = numpy.ones((5, 5), numpy.uint8)
# im = cv2.dilate(im, kernel, iterations=1)
# im = cv2.erode(im,kernel,iterations=1)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
# params.minThreshold = 10;
# params.maxThreshold = 200;

# Filter by Area.
# params.filterByArea = True
# params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.9

# Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87

# Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
print int(ver[0])
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, numpy.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for point in keypoints:
    print point.pt

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)