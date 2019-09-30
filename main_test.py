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
import misc_fn
import os
from box import Box1, Box2
from controller_tracking import tracking

# Path of directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Update music list to include all available tracks
mus_path = dir_path + "/music/"
music_list_filename = "music_list.json"
music_list = misc_fn.load(music_list_filename)

# Check for all available tracks
for filename in os.listdir(mus_path):
    if filename.endswith(".json"):
        music_list[os.path.splitext(filename)[0]] = misc_fn.load(mus_path + filename)

# Save to music list
misc_fn.dump(music_list, music_list_filename)

# loaded song
song_to_load = "new_divide"

# Initialise pygame window
pygame.init()
displaysurf = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)

# Initialise pygame settings
status = ""
status = "load_song"

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
contrail_length = 15
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

# Directional values for direction1 and direction2
#      -0.5     1     2.5
#          \    |    /
#           \   |   /
#            \  |  /
#      -1.5-----0-----1.5
#            /  |  \
#           /   |   \
#          /    |    \
#      -2.5    -1      0.5


# Initialise videostream from webcam
vs = VideoStream(src=0).start()

# Display pygame window
pygame.display.set_caption('SABER STRONKEST')
# Text
fontObj = pygame.font.SysFont('couriernew.ttf', 22)

# Pause 2.0s to allow the camera to warm up
time.sleep(2.0)

# Initialise fps
fps = FPS().start()

# Main loop through frames from videostream
while True:
    # quit_game event
    if status == "quit_game":
        break
    
    # Refresh screen for pygame window
    displaysurf.fill(black)
    pygame.draw.rect(displaysurf, white, (0, 0, 1000, 650), 1)
    
    # Read the current frame and flip it horizontally to correct orientation
    frame = vs.read()
    frame = cv2.flip(frame, 1)
    
    # End of video
    if frame is None:
        break
    
    center1, center2 = tracking(
                                frame=frame,
                                ctrler1_min=ctrler1_min, ctrler1_max=ctrler1_max,
                                ctrler2_min=ctrler2_min, ctrler2_max=ctrler2_max,
                                pts1=pts1, pts2=pts2,
                                frame_counter=frame_counter,
                                contrail_length=contrail_length,
                                direction1=direction1, direction2=direction2,
                                dX1=dX1, dY1=dY1,
                                dX2=dX2, dY2=dY2
                            )
    
    if center1 is not None and center2 is not None:
        # Draw controllers on the pygame window
        pygame.draw.rect(displaysurf, green, (center1[0], center1[1], 10, 10))
        pygame.draw.rect(displaysurf, red, (center2[0], center2[1], 10, 10))
    
    # Game window
    if status == "load_song":
        pygame.mixer.music.load(music_list[song_to_load]["music_path"])
        pygame.mixer.music.play()
        box_counter = 0
        box_list = pygame.sprite.LayeredUpdates()
        status = "playing"
        
    if status == "playing":
        
        song_timer = pygame.mixer.music.get_pos()
        
        SongText = fontObj.render('Time: {}'.format(song_timer / 1E3), True, white)
        SongTextRect = SongText.get_rect()
        SongTextRect.topleft = (630, 10)
        displaysurf.blit(SongText, SongTextRect)
        
        game_play = music_list[song_to_load]["game_play"]
        for i in range(len(game_play)):
            if box_counter > len(game_play) - 1:
                break
            elif song_timer < game_play[box_counter][0]:
                break
            else:
                box = Box1(game_play[box_counter])
                box_list.add(box, layer=(len(game_play) - box_counter))
                box_counter += 1
        if len(box_list) > 0:
            box_list.update(song_timer)
            box_list.draw(displaysurf)
    
    # Update pygame window
    pygame.display.update()
    
    frame_counter += 1
    fps.update()
    fps.stop()
    print(fps.fps())
    
    # if the 'esc' key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        status = "quit_game"
    
    # Event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.__dict__['key'] == 27:
                status = "quit_game"
        # Exit if window is closed
        if event.type == QUIT:
            status = "quit_game"


# Exit procedure after quiting
# Exit pygame
pygame.quit()
# Release the webcam
vs.stop()
# Close all windows
cv2.destroyAllWindows()
sys.exit()
