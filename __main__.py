import math
import random
import sys
import pygame
import pygame.gfxdraw
import time

from GameEngine import Judge, Button
from Object import Player

# Intialize the game 
pygame.init()
pygame.mixer.init()

# Set hyperpara
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

GAME_WIN_LINE = 100

FPS = 30
fpsClock = pygame.time.Clock()

# Intialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Squid Game")

# Background

# Load music
pygame.mixer.music.load(r"./Music/RED LIGHT GREEN LIGHT.mp3")
channel = pygame.mixer.Channel(1)
red_light_song = pygame.mixer.Sound(r"./Music/BLACKPINK  How You Like That.mp3")

# Game Over 
def gameOver1(game_win):
    if(game_win):
        pass
    else:
        pass


# Game 1
def gamePlay1(player, judge, button):
    # init variable
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    
    game_win = False
    
    hit_wrong_button = False
    
    key = None

    # Music
    pygame.mixer.music.play(-1)
    channel.play(red_light_song)
    channel.pause()

    # Game Loop
    while True:
        screen.fill((0, 0, 0))
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if event.key == pygame.K_LEFT:
                    moveLeft = True
                if event.key == pygame.K_RIGHT:
                    moveRight = True
                if event.key == pygame.K_UP:
                    moveUp = True
                if event.key == pygame.K_DOWN:
                    moveDown = True
            # if event.type == pygame.KEYUP:
            #    key = None
            #    if event.key == pygame.K_LEFT:
            #        moveLeft = False
            #    if event.key == pygame.K_RIGHT:
            #        moveRight = False
            #    if event.key == pygame.K_UP:
            #        moveUp = False
            #    if event.key == pygame.K_DOWN:
            #        moveDown = False
        
        
        # Game Rule

        # Music Player
        if(judge.play_main_music == False):
            pygame.mixer.music.pause()
            channel.unpause()
        elif(judge.play_main_music == True):
            channel.pause()
            pygame.mixer.music.unpause()
        # move min red light time
        judge.changeStatus()
        judge.drawTime(screen)
        moved_in_red_light = judge.moveInRedLight(moveLeft or moveRight or moveUp or moveDown)
        # hit button in red light time
        if(judge.start_red_light):
            button.generateButton()
            judge.start_red_light = False
        if(not judge.green_light):
            button.drawButton(screen)
            hitButton = button.hitButton(key)
            if(hitButton == None): 
                pass
            elif(hitButton == True):
                # generate new button
                button.generateButton()
            elif(hitButton == False):
                hit_wrong_button = True
        # Out of time
        out_of_time = judge.outOfTime()
        # win the game
        if(player.y <= GAME_WIN_LINE):
            game_win = True
            pygame.quit()
        
        # Draw
        player.draw(screen)
        player.update(moveLeft, moveRight, moveUp, moveDown)

        pygame.display.update()
        fpsClock.tick(FPS)

        # Reset button
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        
        key = None
        
        # Game Over
        if(moved_in_red_light or out_of_time or hit_wrong_button):
            pygame.quit()

def loadShapeMap(filepath) -> list:
    shapeMap = list()
    
    file = open(filepath, 'r')

    for i in range(600):
        line = file.readline().split(' ')
        arr = [int(x) for x in line[:-2]]
        shapeMap.append(arr)
    return shapeMap

# Game 2
def gamePlay2():
    circleMap = loadShapeMap(r"./Map/FlowerMap.txt")
    
    img = pygame.image.load(r"./img/Flower.png")
    
    green = pygame.Color(0,255, 0, 255)
    
    surface = pygame.Surface((800,600))
    
    surface.blit(img, (0, 0))
    
    click_out_of_bound = False
    
    max_pixel = 0
    for i in circleMap :
        for x in i :
            if x == 1:
                max_pixel += 1
    
    pixel = 0
        
    print(max_pixel)    
    # Game Loop
    
    mousedown = False
    while True:
        screen.fill((0, 0, 0))
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
        if(mousedown == True): 
            width, height = pygame.mouse.get_pos()
            if(circleMap[height][width] != 0):
                for i in range(-20,21,1):
                    for j in range(-20,21,1):
                        x = height + i
                        y = width + j
                        if(circleMap[x][y] == 1):
                            pygame.gfxdraw.pixel(surface, y, x, green)
                            circleMap[x][y] = 2
                            pixel += 1
            else : 
                click_out_of_bound = True
        
        #screen.blit(img, (0,0))
        screen.blit(surface, (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)
        
        if(pixel == max_pixel): 
            print(pixel)
            print(max_pixel)
            pygame.quit()
        
        # Game Over!
        # if(click_out_of_bound):
        #     pygame.quit()

        

def main():
    judge = Judge(True)
    player = Player()
    button = Button(True)
    while True:
        #gamePlay1(player, judge, button)
        gamePlay2()

main()