import pygame
import misc_fn
import numpy as np
import time
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init() #turn all of pygame on.

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
          
        
class Box1(pygame.sprite.Sprite):
    def __init__(self, box_data):
        super().__init__()
        self.size = 20
        self.start_time, self.position, self.type, self.direction = box_data
        if self.type == 1:
            self.image = pygame.image.load("VFX/box1.jpg").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("VFX/box2.jpg").convert_alpha()
        
        # Store a reference to the original to preserve the image quality.
        self.orig_image = self.image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = misc_fn.start_xy(self.position, self.size)

        
    def update(self, current_time):
        time_diff = (current_time - self.start_time)
        passage_time = 1.2E3

        vel_1 = 260

        dsize = int(self.size + (vel_1 * 0.5/passage_time) * time_diff)
        
        
        if misc_fn.col(self.position) == 0:
            self.rect.x = 460 - (vel_1/passage_time * time_diff)
        elif misc_fn.col(self.position) == 1:
            self.rect.x = 480 - (vel_1 * 0.5/passage_time * time_diff)
        elif misc_fn.col(self.position) == 2:
            self.rect.x = 500
        elif misc_fn.col(self.position) == 3:
            self.rect.x = 520 + (vel_1 * 0.5/passage_time * time_diff)

        if misc_fn.row(self.position) == 0:
            self.rect.y = 54 + (vel_1 * 0.1/passage_time) * time_diff
        elif misc_fn.row(self.position) == 1:
            self.rect.y = 74 + (vel_1 * 0.6/passage_time) * time_diff
        elif misc_fn.row(self.position) == 2:
            self.rect.y = 94 + (vel_1 * 1.1/passage_time) * time_diff

        self.image = pygame.transform.smoothscale(self.orig_image, (dsize, dsize))
        
        if time_diff >= 1E3:
            pygame.mixer.Sound(os.path.join(dir_path, "SFX/beat.wav")).play()
            self.kill()
        if time_diff >= passage_time:
            self.kill()


class Box2(pygame.sprite.Sprite):
    def __init__(self, box_data):
        super().__init__()
        self.size = 20
        self.start_time, self.position, self.type, self.direction = box_data
        if self.type == 1:
            self.image = pygame.image.load("VFX/box1.jpg").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("VFX/box2.jpg").convert_alpha()

        # Store a reference to the original to preserve the image quality.
        self.orig_image = self.image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = misc_fn.start_xy(self.position, self.size)

    def update(self, current_time, center):
        time_diff = (current_time - self.start_time)
        passage_time = 1.2E3

        vel_1 = 260

        dsize = int(self.size + (vel_1 * 0.5 / passage_time) * time_diff)

        if misc_fn.col(self.position) == 0:
            self.rect.x = 460 - (vel_1 / passage_time * time_diff)
        elif misc_fn.col(self.position) == 1:
            self.rect.x = 480 - (vel_1 * 0.5 / passage_time * time_diff)
        elif misc_fn.col(self.position) == 2:
            self.rect.x = 500
        elif misc_fn.col(self.position) == 3:
            self.rect.x = 520 + (vel_1 * 0.5 / passage_time * time_diff)

        if misc_fn.row(self.position) == 0:
            self.rect.y = 54 + (vel_1 * 0.1 / passage_time) * time_diff
        elif misc_fn.row(self.position) == 1:
            self.rect.y = 74 + (vel_1 * 0.6 / passage_time) * time_diff
        elif misc_fn.row(self.position) == 2:
            self.rect.y = 94 + (vel_1 * 1.1 / passage_time) * time_diff

        self.image = pygame.transform.smoothscale(self.orig_image, (dsize, dsize))

        if time_diff >= 0.5E3:
            if self.rect.x < center[0] < self.rect.x + self.image.get_width() \
                    and self.rect.y < center[1] < self.rect.y + self.image.get_height():
                pygame.mixer.Sound(os.path.join(dir_path, "SFX/beat1.wav")).play()
                self.kill()
            # if time_diff >= passage_time:
            #     self.kill()

        
    

    
        
        
