import math
import random
import sys
import pygame
import time
from GameEngine import Judge, Button
from Object import Player

#pygame.init()
#
##Set hyperpara
#WINDOW_WIDTH = 600
#WINDOW_HEIGHT = 800
#
#GAME_WIN_LINE = 100
#FPS = 30
#fpsClock = pygame.time.Clock()
#
## Intialize screen
#screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
#pygame.display.set_caption("Squid Game")
#
#button = Button(True)
#img = pygame.image.load("./img/Untitled-1.png")
#while True:
#    screen.fill((0, 0, 0))
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            sys.exit()
#    screen.blit(img, (0, 0))
#    pygame.display.update()
#    fpsClock.tick(FPS)

# pygame.mixer.music.load(r"./Music/y2mate.com - RED LIGHT GREEN LIGHT TikTok Remix  Squid Game Music.mp3")
# pygame.mixer.music.play(-1)
# while True:
#     pass

time_in_red_or_green_light = random.randint((a,b for a, b in (5,9)))
print (time_in_red_or_green_light)
