import pygame, sys
from pygame.locals import *

# Initialise pygame settings
pygame.init()
displaysurf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
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

# Main game loop
while True:
    if quit_game == True:
        break
    # Refresh screen
    displaysurf.fill(black)

    

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