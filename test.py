import math
import random
import sys
import pygame
import time
from GameEngine import Judge, Button
from Object import Player

pygame.init()

# Set hyperpara
# WINDOW_WIDTH = 600
# WINDOW_HEIGHT = 800
# 
# GAME_WIN_LINE = 100
# FPS = 30
# fpsClock = pygame.time.Clock()
# 
# # Intialize screen
# screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
# pygame.display.set_caption("Squid Game")
# 
# button = Button(True)
# 
# while True:
#     screen.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     button.drawButton(screen)
#     pygame.display.update()
#     fpsClock.tick(FPS)

# pygame.mixer.music.load(r"./Music/y2mate.com - RED LIGHT GREEN LIGHT TikTok Remix  Squid Game Music.mp3")
# pygame.mixer.music.play(-1)
# while True:
#     pass

circleMap = list()
    
file = open(r"./Map/CircleMap.txt", 'r')

for i in range(600):
    line = file.readline().split(' ')
    arr = [int(x) for x in line[:-2]]
    circleMap.append(arr)

print(circleMap)