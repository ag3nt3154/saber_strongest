from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time


def outline_tracking(frame, HSV, colour_min, colour_max):
    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask1 = cv2.inRange(hsv, ctrler1_min, ctrler1_max)
    mask1 = cv2.erode(mask1, None, iterations=2)
    mask1 = cv2.dilate(mask1, None, iterations=2)
    return None
