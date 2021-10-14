import math
import random

import os
import sys

import pygame
import pygame.gfxdraw

import time

from GameEngine import Judge, Button, Timer
from Object import Player
from __ultis__ import loadShapeMap, drawText, generateShapeMap

# Set constants
# Player
PLAYER_SPEED = 5
PLAYER_START_X = 300
PLAYER_START_Y = 400
# Judge


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


# Game Over 
def gameOver():
    sound = pygame.mixer.Sound(r"./music/Omaewa mou shindeiru Sound effect .mp3")
    sound.play()



# Game 1
def gamePlay1():
    # init object and ultis
    judge = Judge(True, 3 * 60)
    player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED)
    button = Button(True, 10)
    
    # Load music
    music = pygame.mixer.Channel(1)
    song = pygame.mixer.Sound(r"./Music/RED LIGHT GREEN LIGHT.mp3")
    music.play(song)
    
    # backgroud
    backgroud = pygame.image.load(r"./img/MapGame.png")
    
    # init variable
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    
    game_over = False
    win = False
    
    hit_wrong_button = False
    
    key = None

    # Game Loop
    while True:
        screen.blit(backgroud, (0, 0))
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_DOWN:
                    move_down = True
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
            music.pause()
        elif(judge.play_main_music == True):
            music.unpause()
        # move in red light time
        judge.changeStatus()
        judge.drawTime(screen)
        if (judge.moveInRedLight(move_left or move_right or move_up or move_down)) :
            game_over = True
        
        # hit button in red light time
        # Bắt đầu đèn đỏ thì tạo 1 nút mới
        if(judge.start_red_light):
            button.generateButton()
            judge.start_red_light = False
        if(not judge.green_light):
            button.drawButton(screen)
            hit_button = button.hitButton(key) # return None True False
            if(hit_button == None): 
                pass
            elif(hit_button == True):
                # generate new button
                button.generateButton()
            elif(hit_button == False):
                game_over = True
        
        # Out of time
        if(judge.outOfTime()):
            game_over = True
        # win the game
        if(player.y <= GAME_WIN_LINE):
            game_win = True
            pygame.quit()
        
        # Draw
        player.update(move_left, move_right, move_up, move_down)
        player.draw(screen)

        pygame.display.update()
        fpsClock.tick(FPS)

        # Reset button
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        
        key = None
        
        # Game Over
        if(game_over):
            gameOver()
        if(player.reached):
            pygame.quit()

# Game 2
def gamePlay2():
    
    CURSOR_MARGIN = 10
    
    timer = Timer()
    
    shape_name = "Circle"
    
    # init
    # load data
    if(not os.path.exists(r"./Map/{}Map.txt".format(shape_name))) :
        generateShapeMap(shape_name)
        
    shape_map = loadShapeMap(r"./Map/{}Map.txt".format(shape_name))
    
    img = pygame.image.load(r"./img/{}.png".format(shape_name))
    # Đếm số pixel cần phải tô màu để thắng
    max_pixel = 0
    for i in shape_map :
        for x in i :
            if x == 1:
                max_pixel += 1

    # init surface and color
    green = pygame.Color(0,255, 0, 255)
    
    background_sur = pygame.Surface((800,600))
    
    # draw base image
    background_sur.blit(img, (0, 0))
    
    
    # init variable
    game_over = False
    
    pixel = 0
    
    remaining_life = 3
        
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
                
        # Game Rule
        if(mousedown == True): 
            width, height = pygame.mouse.get_pos()
            # Di chuột trong vùng cho phép
            if(shape_map[height][width] != 0):
                for i in range(-CURSOR_MARGIN, CURSOR_MARGIN + 1, 1):
                    for j in range(-CURSOR_MARGIN, CURSOR_MARGIN + 1, 1):
                        x = height + i
                        y = width + j
                        if(shape_map[x][y] == 1):
                            pygame.gfxdraw.pixel(background_sur, y, x, green)
                            shape_map[x][y] = 2
                            pixel += 1
            # Di chuyển chuột ra ngoài
            else : 
                remaining_life -= 1
                mousedown = False
                if remaining_life == 0:
                    game_over = True
        
        # out of Time
        if(timer.outOfTime()):
            game_over = True
            
        #screen.blit(img, (0,0))
        screen.blit(background_sur, (0,0))
        timer.drawTime(screen)
        drawText(screen, font='LEMONMILK-Regular.otf', size=30,
                 text='Remaning Life : {}'.format(remaining_life), color='Black', coordinates = (500,0))
        pygame.display.update()
        fpsClock.tick(FPS)
        
        if(pixel == max_pixel): 
            print(pixel)
            print(max_pixel)
            pygame.quit()
        
        # Game Over!
        if(game_over):
            gameOver()


def main():
    while True:
        gamePlay1()
        #gamePlay2()

main()