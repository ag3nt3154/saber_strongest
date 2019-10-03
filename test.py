import pygame, sys
from pygame.locals import *
import os
from imutils.video import FPS

import misc_fn
from box import Box1

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

# Initialise pygame settings
pygame.init()
displaysurf = pygame.display.set_mode((1200, 630), pygame.RESIZABLE)
pygame.display.set_caption('SABER STRONKEST')

# Colour setting
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

# FPS setting

fpsClock = pygame.time.Clock()

# Text
fontObj = pygame.font.SysFont('couriernew.ttf', 22)

# Quit
quit_game = False

status = "load_song"

fps = FPS().start()

# Main game loop
while True:

    if quit_game:
        break
    # Refresh screen
    displaysurf.fill(black)
    pygame.draw.rect(displaysurf, white, (0, 0, 1000, 600), 1)
    if status == "load_song":
        pygame.mixer.music.load(music_list[song_to_load]["music_path"])
        pygame.mixer.music.play()
        status = "playing"
        box_counter = 0
        # box_list = pygame.sprite.Group()
        box_list = pygame.sprite.LayeredUpdates()

    if status == "playing":
        # Set center of screen as (500, 250)
        pygame.draw.line(displaysurf, white, (0, 600), (450, 150), 3)
        pygame.draw.line(displaysurf, white, (1000, 600), (550, 150), 3)

        # pygame.draw.line(displaysurf, white, (0, 100), (500, 45), 1)
        # pygame.draw.line(displaysurf, white, (1000, 100), (500, 45), 1)
        
        
        # grid 1
        n1 = 4 - 200
        pygame.draw.line(displaysurf, white, (460, 250 + n1), (540, 250 + n1), 2)
        pygame.draw.line(displaysurf, white, (460, 270 + n1), (540, 270 + n1), 2)
        pygame.draw.line(displaysurf, white, (460, 290 + n1), (540, 290 + n1), 2)
        pygame.draw.line(displaysurf, white, (460, 310 + n1), (540, 310 + n1), 2)

        pygame.draw.line(displaysurf, white, (460, 250 + n1), (460, 310 + n1), 2)
        pygame.draw.line(displaysurf, white, (540, 250 + n1), (540, 310 + n1), 2)
        pygame.draw.line(displaysurf, white, (500, 250 + n1), (500, 310 + n1), 2)
        pygame.draw.line(displaysurf, white, (520, 250 + n1), (520, 310 + n1), 2)
        pygame.draw.line(displaysurf, white, (480, 250 + n1), (480, 310 + n1), 2)


        # grid 2
        n2 = 10 - 200
        pygame.draw.line(displaysurf, red, (400, 250 + n2), (600, 250 + n2), 2)
        pygame.draw.line(displaysurf, red, (400, 300 + n2), (600, 300 + n2), 2)
        pygame.draw.line(displaysurf, red, (400, 350 + n2), (600, 350 + n2), 2)
        pygame.draw.line(displaysurf, red, (400, 400 + n2), (600, 400 + n2), 2)

        pygame.draw.line(displaysurf, red, (400, 250 + n2), (400, 400 + n2), 2)
        pygame.draw.line(displaysurf, red, (450, 250 + n2), (450, 400 + n2), 2)
        pygame.draw.line(displaysurf, red, (500, 250 + n2), (500, 400 + n2), 2)
        pygame.draw.line(displaysurf, red, (550, 250 + n2), (550, 400 + n2), 2)
        pygame.draw.line(displaysurf, red, (600, 250 + n2), (600, 400 + n2), 2)

        
        # grid 3
        n3 = 20 - 200
        pygame.draw.line(displaysurf, blue, (300, 250 + n3), (700, 250 + n3), 2)
        pygame.draw.line(displaysurf, blue, (300, 350 + n3), (700, 350 + n3), 2)
        pygame.draw.line(displaysurf, blue, (300, 450 + n3), (700, 450 + n3), 2)
        pygame.draw.line(displaysurf, blue, (300, 550 + n3), (700, 550 + n3), 2)
        
        pygame.draw.line(displaysurf, blue, (300, 250 + n3), (300, 550 + n3), 2)
        pygame.draw.line(displaysurf, blue, (400, 250 + n3), (400, 550 + n3), 2)
        pygame.draw.line(displaysurf, blue, (500, 250 + n3), (500, 550 + n3), 2)
        pygame.draw.line(displaysurf, blue, (600, 250 + n3), (600, 550 + n3), 2)
        pygame.draw.line(displaysurf, blue, (700, 250 + n3), (700, 550 + n3), 2)


        # grid 4
        n4 = 30 - 200
        pygame.draw.line(displaysurf, green, (200, 250 + n4), (800, 250 + n4), 2)
        pygame.draw.line(displaysurf, green, (200, 400 + n4), (800, 400 + n4), 2)
        pygame.draw.line(displaysurf, green, (200, 550 + n4), (800, 550 + n4), 2)
        pygame.draw.line(displaysurf, green, (200, 700 + n4), (800, 700 + n4), 2)
        
        pygame.draw.line(displaysurf, green, (200, 250 + n4), (200, 700 + n4), 2)
        pygame.draw.line(displaysurf, green, (350, 250 + n4), (350, 700 + n4), 2)
        pygame.draw.line(displaysurf, green, (500, 250 + n4), (500, 700 + n4), 2)
        pygame.draw.line(displaysurf, green, (650, 250 + n4), (650, 700 + n4), 2)
        pygame.draw.line(displaysurf, green, (800, 250 + n4), (800, 700 + n4), 2)


        
        song_timer = pygame.mixer.music.get_pos()

        SongText = fontObj.render('Time: {}'.format(song_timer/1E3), True, white)
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

        
        box_list.update(song_timer)
        box_list.draw(displaysurf)
        
        

    # Event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.__dict__['key'] == 113 or event.__dict__['key'] == 27:
                quit_game = True
        # Exit if window is closed
        if event.type == QUIT:
            quit_game = True
    

    fps.update()
    fps.stop()
    print(fps.fps())

    pygame.display.update()
    # fpsClock.tick(FPS)
    
pygame.quit()