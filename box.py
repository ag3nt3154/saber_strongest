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




class Box(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, box_data):
        # Call the parent class (Sprite) constructor
        super().__init__()

        start_time, position, type, direction = box_data

        self.start_time = start_time
        self.direction = direction
        self.position = position
        
        
        if box_data[2] == 0:
            colour = gray
        elif box_data[2] == 1:
            colour = green
        elif box_data[2] == 2:
            colour = red
        else:
            colour = blue

        x, y = misc_fn.start_xy(box_data[1])
        x = int(x)
        y = int(y)

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([1000, 600])
        self.image.fill(white)
        self.image.set_colorkey(white)
        
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, colour, [x, y, 20, 20])
        
        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()

    def update(self, current_time):
        time_diff = current_time - self.start_time
        if misc_fn.col(self.position) == 0:
            self.rect.x = self.rect.x - (36 / 4E4) * time_diff
        elif misc_fn.col(self.position) == 1:
            self.rect.x = self.rect.x - (18 / 4E4) * time_diff
        elif misc_fn.col(self.position) == 2:
            self.rect.x = self.rect.x + 0 * time_diff
        elif misc_fn.col(self.position) == 3:
            self.rect.x = self.rect.x + (18 / 4E4) * time_diff

        if misc_fn.row(self.position) == 0:
            self.rect.y = self.rect.y - (28 / 4E4) * time_diff
        elif misc_fn.row(self.position) == 1:
            self.rect.y = self.rect.y - (10 / 4E4) * time_diff
        elif misc_fn.row(self.position) == 2:
            self.rect.y = self.rect.y + (8 / 4E4) * time_diff

        self.size  = self.size * (time_diff/1E5)
        
        # self.image = pygame.transform.scale(self.image, (int(self.size*(time_diff/1E5)), int(self.size*(time_diff/1E5))))
        # self.rect = self.image.get_react()
          
        
class Box1(pygame.sprite.Sprite):
    def __init__(self, box_data):
        super().__init__()
        self.start_time, self.position, self.type, self.direction = box_data
        if self.type == 1:
            self.image = pygame.image.load("box1.jpg").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("box2.jpg").convert_alpha()
        
        # Store a reference to the original to preserve the image quality.
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = misc_fn.start_xy(self.position, 20)
        
    def update(self, current_time):
        time_diff = (current_time - self.start_time)
        passage_time = 2E3
        dsize = int(20 + (180/passage_time) * time_diff)
        
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
        
        
        
    

    
        
        
