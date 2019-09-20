import pygame
import misc_fn
import numpy as np

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
        self.size = 10
        self.start_time, self.position, self.type, self.direction = box_data
        if self.type == 1:
            self.image = pygame.image.load("box1.jpg").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("box2.jpg").convert_alpha()
        
        # Store a reference to the original to preserve the image quality.
        self.orig_image = self.image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = misc_fn.start_xy(self.position, self.size)
        
    def update(self, current_time):
        time_diff = (current_time - self.start_time)
        passage_time = 2E3
        dsize = int(self.size + (100/passage_time) * time_diff)
        
        if misc_fn.col(self.position) == 0:
            self.rect.x = 460 - (360/passage_time * time_diff)
        elif misc_fn.col(self.position) == 1:
            self.rect.x = 480 - (180/passage_time * time_diff)
        elif misc_fn.col(self.position) == 2:
            self.rect.x = 500
        elif misc_fn.col(self.position) == 3:
            self.rect.x = 520 + (180/passage_time * time_diff)

        if misc_fn.row(self.position) == 0:
            self.rect.y = 280 - (280/passage_time) * time_diff
        elif misc_fn.row(self.position) == 1:
            self.rect.y = 300 - (100/passage_time) * time_diff
        elif misc_fn.row(self.position) == 2:
            self.rect.y = 320 + (80/passage_time) * time_diff
            
        self.image = pygame.transform.smoothscale(self.orig_image, (dsize, dsize))
        if time_diff >= passage_time:
            self.kill()
        
        
        
    

    
        
        
