# USAGE

from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import calibration
import pygame, sys
from pygame.locals import *
from imutils.video import FPS

# Initialise pygame window
pygame.init()
displaysurf = pygame.display.set_mode((1100, 700), pygame.RESIZABLE)
pygame.display.set_caption('SABER STRONKEST')

# Initialise pygame settings
quit_game = False

# Colour settings
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)

# Text settings
CourierNewObj = pygame.font.SysFont('couriernew.ttf', 22)


# Define the colours of controllers 1 and 2 in terms of min and max colours in HSV colour space.
# Use calibration.main to determine.
# (ctrler1_min, ctrler1_max) = calibration.main()
# (ctrler2_min, ctrler2_max) = calibration.main()

# Tennis ball
ctrler1_min = (21, 53, 46)
ctrler1_max = (91, 255, 255)
# Red ball
ctrler2_min = (0, 123, 30)
ctrler2_max = (164, 255, 255)

# Initialize the list of tracked points, ...
contrail_length = 32
pts1 = deque(maxlen=contrail_length)
pts2 = deque(maxlen=contrail_length)
# the frame counter, ...
frame_counter = 0
# changes in x, y positions, ...
(dX1, dY1) = (0, 0)
(dX2, dY2) = (0, 0)
# direction, ...
direction1 = 0
direction2 = 0


# Initialise videostream from webcam
vs = VideoStream(src=0).start()

# Pause 2.0s to allow the camera to warm up
time.sleep(2.0)

# Initialise fps
fps = FPS().start()

# Main loop through frames from videostream
while True:
    # quit_game event
    if quit_game == True:
        break

    # Refresh screen for pygame window
    displaysurf.fill(black)
    
    # Read the current frame and flip it horizontally to correct orientation
    frame = vs.read()
    frame = cv2.flip(frame, 1)

    # End of video
    if frame is None:
        break

    # Resize the frame, ...
    frame = imutils.resize(frame, width=1000)
    # blur it, ...
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    # and convert it to the HSV colour space
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # TRACKING CONTROLLER 1
    # Construct a mask for the colour of controller 1, ...
    mask1 = cv2.inRange(hsv, ctrler1_min, ctrler1_max)
    # and perform a series of erosions and dilations to remove any small blobs left in the mask
    mask1 = cv2.erode(mask1, None, iterations=2)
    mask1 = cv2.dilate(mask1, None, iterations=2)

    # Find contours in the mask, ...
    cnts1 = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)
    # and initialize the current(x, y) center of the ball
    center1 = None

    # If at least one contour was found:
    if len(cnts1) > 0:

        # Find the largest contour in the mask
        c1 = max(cnts1, key=cv2.contourArea)
        # Compute minimum enclosing circle
        ((x1, y1), radius1) = cv2.minEnclosingCircle(c1)
        # Find centroid of the circle
        M1 = cv2.moments(c1)
        center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))

        # If the circle is of a certain minimum radius:
        if radius1 > 10:
            # Draw the circle and centroid on the frame
            cv2.circle(frame, (int(x1), int(y1)), int(radius1), (0, 255, 255), 2)
            cv2.circle(frame, center1, 5, (0, 0, 255), -1)
            # Update the list of tracked points
            pts1.appendleft(center1)

    # Loop over the set of tracked points
    for i in np.arange(1, len(pts1)):
        # If any of the tracked points are None, ignore them
        if pts1[i - 1] is None or pts1[i] is None:
            continue
        
        # Find direction of movement of controller
        # Check to see if enough points have been accumulated in the contrail
        if len(pts1) > 10:
            if frame_counter >= 10 and i == 1 and pts1[-10] is not None:
                
                # Find dy, dx
                dX1 = pts1[-10][0] - pts1[i][0]
                dY1 = pts1[-10][1] - pts1[i][1]
                # Initialise direction variables
                (dirX1, dirY1) = (0, 0)

                # If there is significant movement in the x-direction
                if np.abs(dX1) > 20:
                    dirX1 = -1.5 if np.sign(dX1) == 1 else 1.5

                # If there is significant movement in the y-direction
                if np.abs(dY1) > 20:
                    dirY1 = 1 if np.sign(dY1) == 1 else -1
                
                # Compute overall direction
                direction1 = dirX1 + dirY1

        # Draw the contrail
        thickness = int(np.sqrt(contrail_length / float(i + 1)) * 2.5)
        cv2.line(frame, pts1[i - 1], pts1[i], (0, 0, 255), thickness)

    # TRACKING CONTROLLER 2
    # Construct a mask for the colour of controller 1, ...
    mask2 = cv2.inRange(hsv, ctrler2_min, ctrler2_max)
    # and perform a series of erosions and dilations to remove any small blobs left in the mask
    mask2 = cv2.erode(mask2, None, iterations=2)
    mask2 = cv2.dilate(mask2, None, iterations=2)

    # Find contours in the mask, ...
    cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)
    # and initialize the current(x, y) center of the ball
    center2 = None

    # If at least one contour was found:
    if len(cnts2) > 0:

        # Find the largest contour in the mask
        c2 = max(cnts2, key=cv2.contourArea)
        # Compute minimum enclosing circle
        ((x2, y2), radius2) = cv2.minEnclosingCircle(c2)
        # Find centroid of the circle
        M2 = cv2.moments(c2)
        center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

        # If the circle is of a certain minimum radius:
        if radius2 > 10:
            # Draw the circle and centroid on the frame
            cv2.circle(frame, (int(x2), int(y2)), int(radius2), (255, 0, 255), 2)
            cv2.circle(frame, center2, 5, (0, 0, 255), -1)
            # Update the list of tracked points
            pts2.appendleft(center2)

    # Loop over the set of tracked points
    for i in np.arange(1, len(pts2)):
        # If any of the tracked points are None, ignore them
        if pts2[i - 1] is None or pts2[i] is None:
            continue
    
        # Find direction of movement of controller
        # Check to see if enough points have been accumulated in the contrail
        if len(pts2) > 10:
            if frame_counter >= 10 and i == 1 and pts2[-10] is not None:
            
                # Find dy, dx
                dX2 = pts2[-10][0] - pts2[i][0]
                dY2 = pts2[-10][1] - pts2[i][1]
                # Initialise direction variables
                (dirX2, dirY2) = (0, 0)
            
                # If there is significant movement in the x-direction
                if np.abs(dX2) > 20:
                    dirX2 = -1.5 if np.sign(dX2) == 1 else 1.5
            
                # If there is significant movement in the y-direction
                if np.abs(dY2) > 20:
                    dirY2 = 1 if np.sign(dY2) == 1 else -1
            
                # Compute overall direction
                direction2 = dirX2 + dirY2
    
        # Draw the contrail
        thickness = int(np.sqrt(contrail_length / float(i + 1)) * 2.5)
        cv2.line(frame, pts2[i - 1], pts2[i], (0, 0, 255), thickness)

    # Show direction of movement
    cv2.putText(frame, str(direction1), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 3)
    cv2.putText(frame, str(direction2), (310, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 3)
    
    # Show contrails
    cv2.putText(frame, "dx: {}, dy: {}".format(dX1, dY1), (10, frame.shape[0] - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.putText(frame, "dx: {}, dy: {}".format(dX2, dY2), (310, frame.shape[0] - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # Update frame in tracking window
    cv2.imshow("Frame", frame)
    
    if center1 is not None and center2 is not None:
        # Draw controllers on the pygame window
        pygame.draw.rect(displaysurf, green, (center1[0], center1[1], 10, 10))
        pygame.draw.rect(displaysurf, red, (center2[0], center2[1], 10, 10))

    
    # Update pygame window
    pygame.display.update()
    
    frame_counter += 1
    fps.update()
    fps.stop()
    
    # if the 'esc' key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        quit_game = True

    # Event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.__dict__['key'] == 27:
                quit_game = True
        # Exit if window is closed
        if event.type == QUIT:
            quit_game = True


# Exit procedure after quiting
# Exit pygame
pygame.quit()
# Release the webcam
vs.stop()
# Close all windows
cv2.destroyAllWindows()
sys.exit()
