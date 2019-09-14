# USAGE
# python object_movement.py --video object_tracking_example.mp4
# python object_movement.py

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import calibration


contrail_length = 32

# define the lower and upper boundaries of the "green"
# ball in the HSV color space

# Tennis ball
ctrler1_min = (26, 65, 95)
ctrler1_max = (141, 158, 165)

# Red ball
ctrler2_min = (0, 160, 84)
ctrler2_max = (56, 255, 192)



# initialize the list of tracked points, the frame counter,
# and the coordinate deltas
pts = deque(maxlen=contrail_length)
counter = 0
(dX, dY) = (0, 0)
direction = ""

# if a video path was not supplied, grab the reference
# to the webcam

vs = VideoStream(src=0).start()




# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	frame = vs.read()

	frame = cv2.flip(frame, 1)

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask1 = cv2.inRange(hsv, ctrler1_min, ctrler1_max)
	mask1 = cv2.erode(mask1, None, iterations=2)
	mask1 = cv2.dilate(mask1, None, iterations=2)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask2 = cv2.inRange(hsv, ctrler2_min, ctrler2_max)
	mask2 = cv2.erode(mask2, None, iterations=2)
	mask2 = cv2.dilate(mask2, None, iterations=2)



	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts1 = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts1 = imutils.grab_contours(cnts1)
	center1 = None

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL,
							 cv2.CHAIN_APPROX_SIMPLE)
	cnts2 = imutils.grab_contours(cnts2)
	center2 = None



	# only proceed if at least one contour was found
	if len(cnts1) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c1 = max(cnts1, key=cv2.contourArea)
		((x1, y1), radius1) = cv2.minEnclosingCircle(c1)
		M1 = cv2.moments(c1)
		center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))

		# only proceed if the radius meets a minimum size
		if radius1 > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x1), int(y1)), int(radius1),
				(0, 255, 255), 2)
			cv2.circle(frame, center1, 5, (0, 0, 255), -1)
			pts.appendleft(center1)

	# only proceed if at least one contour was found
	if len(cnts2) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c2 = max(cnts2, key=cv2.contourArea)
		((x2, y2), radius2) = cv2.minEnclosingCircle(c2)
		M2 = cv2.moments(c2)
		center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

		# only proceed if the radius meets a minimum size
		if radius2 > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x2), int(y2)), int(radius2),
					   (255, 0, 255), 2)
			cv2.circle(frame, center2, 5, (0, 0, 255), -1)
			pts.appendleft(center2)

	# loop over the set of tracked points
	for i in np.arange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue

		# check to see if enough points have been accumulated in
		# the buffer
		if len(pts) > 9:
			if counter >= 10 and i == 1 and pts[-10] is not None:
				# compute the difference between the x and y
				# coordinates and re-initialize the direction
				# text variables
				dX = pts[-10][0] - pts[i][0]
				dY = pts[-10][1] - pts[i][1]
				(dirX, dirY) = ("", "")

				# ensure there is significant movement in the
				# x-direction
				if np.abs(dX) > 20:
					dirX = "East" if np.sign(dX) == 1 else "West"

				# ensure there is significant movement in the
				# y-direction
				if np.abs(dY) > 20:
					dirY = "North" if np.sign(dY) == 1 else "South"

				# handle when both directions are non-empty
				if dirX != "" and dirY != "":
					direction = "{}-{}".format(dirY, dirX)

				# otherwise, only one direction is non-empty
				else:
					direction = dirX if dirX != "" else dirY

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(contrail_length / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

	# show the movement deltas and the direction of movement on
	# the frame
	cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (0, 0, 255), 3)
	cv2.putText(frame, "dx: {}, dy: {}".format(dX, dY),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 0, 255), 1)

	# show the frame to our screen and increment the frame counter
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	counter += 1

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break



# otherwise, release the camera
vs.stop()



# close all windows
cv2.destroyAllWindows()