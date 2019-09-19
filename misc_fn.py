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


def col(position):
    return (position + 3) % 4


def row(position):
    return np.floor((position - 0.5) / 4)




def start_xy(position, box_size=20):
    x = col(position) * box_size + 500 - 2 * box_size
    y = row(position) * box_size + 300 - box_size
    return x, y



def generate_box(box_data, displaysurf, start_time):
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
    x = ((box_data[1]+3) % 4) * box_size + 500 - 2 * box_size
    y = np.floor(box_data[1] / 5) + 300 - box_size
    if box_data[2] == 0:
        colour = gray
    elif box_data[2] == 1:
        colour = blue
    elif box_data[2] == 2:
        colour = purple
        
    pygame.draw.rect(displaysurf, colour, (x, y, box_size, box_size))
    return x, y, colour, box_size, start_time, box_data


def move_box(box, displaysurf, current_time):
    (x, y, colour, box_size, start_time, box_data) = box
    time_diff = current_time - start_time
    box_size = 20 * (10 / 4) * (time_diff)
    if (box_data[1]+3) % 4 == 0:
        x = x - (360/4) * time_diff
    elif (box_data[1]+3) % 4 == 1:
        x = x - (180/4) * time_diff
    elif (box_data[1]+3) % 4 == 2:
        x = x + 0 * time_diff
    elif (box_data[1]+3) % 4 == 3:
        x = x + (180/4) * time_diff
    
    if np.floor(box_data[1] / 5) == 0:
        y = y - (280/4) * time_diff
    elif np.floor(box_data[1] / 5) == 1:
        y = y - (100/4) * time_diff
    elif np.floor(box_data[1] / 5) == 2:
        y = y + (80/4) * time_diff

    pygame.draw.rect(displaysurf, colour, (x, y, box_size, box_size))
    
    return x, y, colour, box_size, start_time, box_data


if __name__ == '__main__':
    x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(col(x))
    print(row(x))
    print(start_xy(x))