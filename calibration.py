#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calibrate HSV values to track controllers

import cv2


def callback(value):
    pass


def setup_trackbars(range_filter):
# Set up trackbars to adjust values
    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255

        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)





def get_trackbar_values(range_filter):
# Get HSV values from trackbars
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)

    return values


def main():

    range_filter = 'HSV'.upper()

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    setup_trackbars(range_filter)

    while True:

        ret, image = camera.read()
        image = cv2.flip(image, 1)

        if not ret:
            break

        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # HSV values from trackbars
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

        # Filter according to HSV values
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        # Show images
        cv2.imshow("Original", image)
        cv2.imshow("Thresh", thresh)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
    return ((v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

if __name__ == '__main__':
    main()
