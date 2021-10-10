import math
import random
import sys
import pygame
import time 

PLAYERSPEED = 2
PLAYER_START_X = 300
PLAYER_START_Y = 400

# Player in game 1
class Player():
    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.img = pygame.image.load(r'img/Layer 1.png')
        self.speed = PLAYERSPEED
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.speed
