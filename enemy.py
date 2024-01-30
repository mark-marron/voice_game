import pygame

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1

    def collided_with(self, bullets):
        for bullet in bullets:
            if bullet.x > self.x and bullet.x < self.x + 37 and bullet.y < self.y + 101 and bullet.y > self.y:
                return True
        return False