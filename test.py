import pygame, sys
from pygame.locals import *
import os
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
displaysurf = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
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
FPS = 10
fpsClock = pygame.time.Clock()

# Text
fontObj = pygame.font.SysFont('couriernew.ttf', 22)

# Quit
quit_game = False

status = "load_song"


# Main game loop
while True:
    if quit_game:
        break
    # Refresh screen
    displaysurf.fill(black)

    if status == "load_song":
        pygame.mixer.music.load(music_list[song_to_load]["music_path"])
        pygame.mixer.music.play()
        status = "playing"
        box_counter = 0
        box_list = pygame.sprite.Group()

    if status == "playing":
        # Set center of screen as (500, 250)
        pygame.draw.line(displaysurf, white, (0, 470), (500, 250), 3)
        pygame.draw.line(displaysurf, white, (1000, 470), (500, 250), 3)
        
        pygame.draw.line(displaysurf, red, (500, 250), (0, 125))
        pygame.draw.line(displaysurf, red, (500, 250), (0, 0))
        pygame.draw.line(displaysurf, red, (500, 250), (500, 0))
        pygame.draw.line(displaysurf, red, (500, 250), (1000, 0))
        
        pygame.draw.line(displaysurf, blue, (500, 250), (0, 375))
        pygame.draw.line(displaysurf, blue, (500, 250), (0, 500))
        pygame.draw.line(displaysurf, blue, (500, 250), (500, 1000))
        pygame.draw.line(displaysurf, blue, (500, 250), (1000, 500))
        
        pygame.draw.line(displaysurf, green, (500, 250), (0, 625))
        pygame.draw.line(displaysurf, green, (500, 250), (0, 1000))
        pygame.draw.line(displaysurf, green, (500, 250), (500, 1000))
        pygame.draw.line(displaysurf, green, (500, 250), (1000, 1000))
        
        song_timer = pygame.mixer.music.get_pos()
        game_play = music_list[song_to_load]["game_play"]
        for i in range(len(game_play)):
            if box_counter > len(game_play) - 1:
                break
            elif song_timer < game_play[box_counter][0]:
                break
            else:
                box = Box1(game_play[box_counter])
                box_list.add(box)
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
    

    

    pygame.display.update()
    # fpsClock.tick(FPS)
    
pygame.quit()