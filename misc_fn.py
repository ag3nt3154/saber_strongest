# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""
import json
import pygame
import numpy as np
import time


def dump(data, filename):
    """
    Save JSON object to file
    """
    with open(filename, 'w') as f:
        data = json.dump(data, f)


def load(filename):
    """
    Load JSON object from file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def generate_box(box_data, displaysurf):
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
    box_size = 20
    x = ((box_data[1]+3) % 4) * box_size + 600 - 2 * box_size
    y = np.floor(box_data[1] / 5) + 350 - box_size
    if box_data[2] == 0:
        colour = gray
    elif box_data[2] == 1:
        colour = blue
    elif box_data[2] == 2:
        colour = purple
        
    pygame.draw.rect(displaysurf, colour, (x, y, box_size, box_size), 1)
    return x, y, colour, box_size, time.time()


def move_box(box, displaysurf):
    (x, y, colour, box_size, start_time) = box
    time_diff = time.time() - start_time
    box_size = 20 * (10 / 4) * (time_diff)
    
    pass
