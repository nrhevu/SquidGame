import math
import random
from random import Random
import sys
import pygame
import time 

# Game 1 engine

# Constants
BUTTON_TIME_LIMIT = 3

TIMER_TIME_LIMIT = 1 * 60

""" Button must be hitted in red light to remain balanced """
class Button():
    def __init__(self, movingOkStatus):
        self.movingOkStatus = movingOkStatus
        self.time_limit = BUTTON_TIME_LIMIT
        self.button_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.button = random.choice(self.button_set[1:])
        self.start_hit_button_time = 0
        self.remain_time = 0
    def generateButton(self):
        self.start_hit_button_time = time.time()
        self.button = random.choice(self.button_set)
    # Hit button function
    """ return True if hit right button in time time_limit
        return False if hit wrong button or exceed time limit """
    def hitButton(self, key) -> bool:
        self.remain_time = self.time_limit - (time.time() - self.start_hit_button_time)
        if(self.remain_time <= 0):
            return False
        if(key != None): 
            if(key == self.button):
                return True
            else:
                print('kk')
                return False
        else :
            return None
    def drawButton(self, screen):
        BUTTON_FONT = pygame.font.Font('./Font/Digital Dismay.otf', 50)
        button_draw = BUTTON_FONT.render(str(self.button), 0, 'White')
        screen.blit(button_draw, (400,300))

""" Timer use in game 1 to define whenever is green light or red light """
class Timer():
    def __init__(self, movingOkStatus):
        self.start_time = time.time()
        self.turn_time = time.time()
        self.time_in_redOrgreen_light = 2
        self.green_light = movingOkStatus
        self.time_limit = TIMER_TIME_LIMIT
        self.remain_time = self.time_limit
        self.play_main_music = True
        self.start_red_light = False
    def changeStatus(self):
        start_red_light = False
        if(time.time() - self.turn_time >= self.time_in_redOrgreen_light - 0.10):
            if(self.green_light == True):
                self.play_main_music = False
            elif(self.green_light == False):
                self.play_main_music = True
        if(time.time() - self.turn_time >= self.time_in_redOrgreen_light):
            if(self.green_light == True):
                self.start_red_light = True
                self.green_light = False
                self.turn_time = time.time()
                self.time_in_redOrgreen_light = random.uniform(5,9)
            elif(self.green_light == False):
                self.green_light = True
                self.turn_time = time.time()
                self.time_in_redOrgreen_light = random.uniform(3,9)
    """ If moved in red light return True
        Else return False """
    def moveInRedLight(self, moved) -> bool:
        if(self.green_light == True):
                return False
        elif(self.green_light == False):
            if (moved):
                return True
            else :
                return False
    def outOfTime(self):
        if(self.remain_time <= 0):
            return True
    # Remaining time draw function
    def drawTime(self, screen):
        self.remain_time = int(self.time_limit -(time.time() - self.start_time))
        m, s = divmod(self.remain_time, 60)
        h, m = divmod(m, 60)
        timeLeft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        color = pygame.Color('Green')
        if self.green_light == False:
            color = pygame.Color('Red')
        GAME_FONT = pygame.font.Font('./Font/Digital Dismay.otf', 50)

        timer = GAME_FONT.render(timeLeft, 0, color)

        s = pygame.Surface((timer.get_width()+20, 48))
        s.fill('#000000')
        screen.blit(timer, (0,0))

# Game 2 engine


