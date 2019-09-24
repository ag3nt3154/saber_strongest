# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""
import json
import pygame
import numpy as np
import time
import os


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
    x = col(position) * box_size + 460
    y = row(position) * box_size + 58
    return x, y


_image_library = {}


def get_image(path):
    # Usage: screen.blit(get_image('ball.png'), (20, 20))
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return image


_sound_library = {}


def play_sound(path):
    # Usage: play_sound(path)
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()


if __name__ == '__main__':
    x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(col(x))
    print(row(x))
    print(start_xy(x))