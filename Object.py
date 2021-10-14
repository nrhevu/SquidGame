import math
import random
import sys
import pygame
import time 

from __ultis__ import loadShapeMap

# Player in game 1
class Player():
    direction = 'Ahead'
    sprite_num = 1  
    reached = False
    map = loadShapeMap(r"./Map/Map.txt")
    
    def __init__(self, x ,y, speed):
        self.x = x
        self.y = y
        self.img = pygame.image.load(r'img/player/Back_1.png')
        self.speed = speed
    def draw(self, screen):
        if(self.sprite_num > 3):
            self.sprite_num = 1
        self.img = pygame.image.load(r'img/player/{}_{}.png'.format(self.direction, self.sprite_num))
        screen.blit(self.img, (self.x, self.y))
    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            if(self.direction != 'Left'):
                self.direction = 'Left'
                self.sprite_num = 1
            self.sprite_num += 1
            for i in range(3,18):
                if(self.map[self.y + i][self.x - self.speed] == 1) :
                    return
            if(self.map[self.y + i][self.x - self.speed] == 2) : 
                self.reached = True
            self.x -= self.speed
        if moveRight == True:
            if(self.direction != 'Right'):
                self.direction = 'Right'
                self.sprite_num = 1  
            self.sprite_num += 1 
            for i in range(3,18):
                if(self.map[self.y + i][self.x + 14 + self.speed] == 1) :
                    return
            if(self.map[self.y + i][self.x + 14 + self.speed] == 2) : 
                self.reached = True
            self.x += self.speed
        if moveUp == True:
            if(self.direction != 'Back'):
                self.direction = 'Back'
                self.sprite_num = 1  
            self.sprite_num += 1
            for i in range(2,12):
                if(self.map[self.y - self.speed][self.x + i] == 1) :
                    return
            if(self.map[self.y - self.speed][self.x] == 2) : 
                self.reached = True
            self.y -= self.speed
        if moveDown == True:
            if(self.direction != 'Ahead'):
                self.direction = 'Ahead'
                self.sprite_num = 1  
            self.sprite_num += 1
            for i in range(2,12):
                if(self.map[self.y + 19 + self.speed][self.x] == 1) :
                    return
            if(self.map[self.y + 19 + self.speed][self.x] == 2) : 
                self.reached = True
            self.y += self.speed
