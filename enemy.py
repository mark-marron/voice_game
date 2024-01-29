import pygame
from random import randint

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2