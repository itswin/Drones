import cv2
from bebop import Bebop
import pygame
import time
from commands import *
import numpy

cnt = 0
f = open( "./images/video.h264", "wb" )

def videoCallback( frame, drone, debug=False ):
    global cnt
    if isinstance(frame, tuple):
        # print("h.264 frame - (frame# = %s, iframe = %s, size = %s)" % (frame[0], frame[1], len(frame[2])))
        f.write(frame[-1])
        f.flush()
    else:
        if drone.frameWidth == 0:
            drone.frameWidth = numpy.size(frame, 1)
        if drone.frameHeight == 0:
            drone.frameHeight = numpy.size(frame, 0)

        # convert image to grayscale and blur it
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if drone.thisFrame is None:
            drone.lastFrame = frame
        else:
            drone.lastFrame = drone.thisFrame
        drone.thisFrame = frame

        grayLastFrame = cv2.cvtColor(drone.lastFrame, cv2.COLOR_BGR2GRAY)
        grayLastFrame = cv2.GaussianBlur(grayLastFrame, (21, 21), 0)

        # if (cnt % 2) == 0:
        #     drone.backgroundMotionDetectionImage = gray

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

            drone.objectCenterX = (x + w) / 2
            drone.objectCenterY = (y + h) / 2

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('delta', frameDelta)
        cnt = cnt + 1
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)


def scale(value, scaler):
    if abs(value) < 0.03:
        return 0
    return value * scaler

def clip(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    else:
        return value

cnt = 0
frames = 0
lastFrames = 0

# Video variables
f = open( "./images/video.h264", "wb" )

print("Connecting to drone...")
drone = Bebop( metalog=None, onlyIFrames=True, jpegStream=True)
drone.trim()
drone.videoCbk = videoCallback
drone.videoEnable()
for i in xrange(20):
    drone.update()
print("Connected.")

pygame.init()
size = [100, 100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drone Teleop")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initializes joystick
if pygame.joystick.get_count() == 0:
    print("No joysticks found")
    done = True
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Initialized %s" % (joystick.get_name()))
    print("Number of buttons %d. Number of axis %d, Number of hats %d" %
          (joystick.get_numbuttons(), joystick.get_numaxes(),
           joystick.get_numhats()))

MAX_SPEED = 60

tilt = 0
tiltMin = -70
tiltMax = 40

pan = 0
panMin = -40
panMax = 40

secondsCounter = 0
frames = 0

printCounter = 0

# -------- Main Program Loop -----------
while not done:
    try:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # Deltas for controlling the camera
        tiltDelta = 0
        panDelta = 0

        if joystick.get_button(3) == 1 and not drone.findSphero:
            drone.findSphero = True
            drone.moveScaler = 0.2

        if joystick.get_button(2) and drone.findSphero:
            drone.findSphero = False

        if drone.findSphero:
            xCenteringPower = (drone.objectCenterX - (drone.frameWidth >> 2)) * drone.moveScaler
            yCenteringPower = ((drone.frameHeight >> 2) - drone.objectCenterY) * drone.moveScaler
            if (printCounter % 5) == 0:
                print("Finding Sphero")
                print(xCenteringPower)
                print(yCenteringPower)

            drone.update(cmd=movePCMDCmd(True, xCenteringPower, yCenteringPower, 0, 0))

        # A and Back to emergency land
        if joystick.get_button(0) == 1 and joystick.get_button(6) == 1:
            drone.emergency()

        # Back to land
        if joystick.get_button(6) == 1:
            print("Landing...")
            if drone.flyingState is None or drone.flyingState == 1: # if taking off then do emegency landing
                drone.emergency()
            drone.land()

        # Start to takeoff
        if joystick.get_button(7) == 1:
            if drone.flyingState == 0:
                drone.takeoff()

        # --- Flying ---
        # Power values
        roll = scale(joystick.get_axis(0), MAX_SPEED)
        pitch = -scale(joystick.get_axis(1), MAX_SPEED)
        yaw = scale(joystick.get_axis(3), MAX_SPEED)
        gaz = -scale(joystick.get_axis(4), MAX_SPEED)

        drone.update(cmd=movePCMDCmd(True, roll, pitch, yaw, gaz))

        # --- Move camera ---

        # Triggers to tilt
        if not(joystick.get_button(0) == 1) and joystick.get_axis(2) > 0.05:
            tiltDelta = scale(joystick.get_axis(2), -10)

        if not(joystick.get_button(0) == 1) and joystick.get_axis(5) > 0.05:
            tiltDelta = scale(joystick.get_axis(5), 10)

        tilt = clip(tilt + tiltDelta, tiltMin, tiltMax)
        pan = clip(pan + panDelta, panMin, panMax)

        # Reset camera on LB
        if joystick.get_button(4) == 1:
            tilt = 0
            pan = 0

        if joystick.get_button(5) == 1:
            print("Flying to altitude: 2.25")
            drone.flyToAltitude(2.25)

        drone.moveCamera(tilt, pan)

        # Limit to 20 frames per second
        clock.tick(20)
    except:
        print("Error")
        if drone.flyingState is None or drone.flyingState == 1:
            # if taking off then do emergency landing
            drone.emergency()
        drone.land()
        done = True

# Close the window and quit.
pygame.quit()