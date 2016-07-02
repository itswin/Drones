from bebop import Bebop
from commands import *
from bardecoder import *
import pygame
import cv2
import time

def videoCallback( frame, drone, debug=False ):
    global cnt
    global done
    if isinstance(frame, tuple):
       f.write(frame[-1])
       f.flush()
    else:
        if cnt % 15 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if cnt % 15 == 5:
            drone.barcodes = decoder.decode(frame)
            for i in drone.barcodes:
                cv2.polylines(frame, [np.int32(i.location)], True, 255, 3, 16)
                print("Barcode found:" + i.value)

        if drone.frameWidth == 0:
            drone.frameWidth = np.size(frame, 1)
        if drone.frameHeight == 0:
            drone.frameHeight = np.size(frame, 0)

        if drone.pictureBoolean:
            cv2.imwrite('savedImage.jpg', frame)
            print('Picture saved...')
            drone.pictureBoolean = False

        cnt += 1
        cv2.imshow("Drone Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            done = True

def scale(value, scaler):
    if abs(value) < 0.05:
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
decoder = Decoder()
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

current_milli_time = lambda: int(round(time.time() * 1000))

print("Connecting to drone...")
drone = Bebop( metalog=None, onlyIFrames=True, jpegStream=True)
drone.trim()
drone.videoCbk = videoCallback
drone.videoEnable()
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

lastTime = current_milli_time()
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

        # Displays battery every 5 seconds
        nowTime = current_milli_time()
        if (nowTime - lastTime) > 1000:
            secondsCounter += 1
            lastTime = nowTime

            if secondsCounter % 5 == 0:
                print("Battery: " + str(drone.battery))

        # Deltas for controlling the camera
        tiltDelta = 0
        panDelta = 0

        # Press X to take a picture
        if joystick.get_button(2) and not drone.pictureBoolean:
            print('Taking picture...')
            drone.pictureBoolean = True

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

        # --- Flips ---
        (hat_x, hat_y) = joystick.get_hat(0)

        # A and Hat direction to flip
        if joystick.get_button(0) == 1 and hat_y == 1:
            print("Executing Front Flip")
            drone.frontFlip()

        if joystick.get_button(0) == 1 and hat_y == -1:
            print("Executing Back Flip")
            drone.backFlip()

        if joystick.get_button(0) == 1 and hat_x == 1:
            print("Executing Right Flip")
            drone.rightFlip()

        if joystick.get_button(0) == 1 and hat_x == -1:
            print("Executing Left Flip")
            drone.leftFlip()

        if joystick.get_button(1) == 1:
            print("Battery: " + str(drone.battery))

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

        # A and triggers to pan
        if joystick.get_button(0) == 1 and joystick.get_axis(2) > 0.05:
            panDelta = scale(joystick.get_axis(2), -10)

        if joystick.get_button(0) == 1 and joystick.get_axis(5) > 0.05:
            panDelta = scale(joystick.get_axis(5), 10)

        tilt = clip(tilt + tiltDelta, tiltMin, tiltMax)
        pan = clip(pan + panDelta, panMin, panMax)

        # Reset camera on LB
        if joystick.get_button(4) == 1:
            tilt = 0
            pan = 0

        if joystick.get_button(5) == 1:
            print("Flying to altitude: 1.5")
            drone.flyToAltitude(1.5)

        drone.moveCamera(tilt, pan)

        # Barcode testing
        # Press Y to center
        if len(drone.barcodes) > 0 and joystick.get_button(3) == 1:
            printCounter += 1
            if printCounter > 5:
                print("Centering")
                printCounter = 0
            frameCenterX = drone.frameWidth / 2
            frameCenterY = drone.frameHeight / 2
            i = drone.barcodes[0]
            x = (i.location[0][0] + i.location[1][0] + i.location[2][0] + i.location[3][0]) / 4
            y = (i.location[0][1] + i.location[1][1] + i.location[2][1] + i.location[3][1]) / 4

            xDistance = frameCenterX - x
            yDistance = frameCenterY - y

            if xDistance > 30:
                drone.update(cmd=movePCMDCmd(True, 5, 0, 0, 0))
            if xDistance < -30:
                drone.update(cmd=movePCMDCmd(True, -5, 0, 0, 0))
            if yDistance > 30:
                drone.update(cmd=movePCMDCmd(True, 0, 5, 0, 0))
            if yDistance < -30:
                drone.update(cmd=movePCMDCmd(True, 0, -5, 0, 0))

            drone.hover()

        # Limit to 20 frames per second
        clock.tick(20)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            if drone.flyingState == 0 or drone.flyingState == 1:
                drone.emergency()
            drone.land()
            done = True
    except:
        print("Error")
        if drone.flyingState is None or drone.flyingState == 1:
            # if taking off then do emergency landing
            drone.emergency()
        drone.land()
        done = True

# Close the window and quit.
pygame.quit()