import math
import random

import os
import sys

import pygame
import pygame.gfxdraw

import time

from GameEngine import Game1Engine, Button, Timer
from Object import Player
from __ultis__ import loadShapeMap, drawText, generateShapeMap

# Set constants
# Player
PLAYER_SPEED = 4
PLAYER_START_X = 560
PLAYER_START_Y = 530


# Intialize the game 
pygame.init()
pygame.mixer.init()

# Set hyperpara
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

FPS = 30
fpsClock = pygame.time.Clock()

# Intialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Squid Game")
icon = pygame.image.load(r"./img/Logo_1.png")
pygame.display.set_icon(icon)

# Music
pygame.mixer.music.load(r"./Music/Squid Game Pink Soldiers  EPIC REMIX.mp3")


# Game Over 
def gameOver():
    sound = pygame.mixer.Sound(r"./music/Omaewa mou shindeiru Sound effect .mp3")
    game_over_img = pygame.image.load(r"./img/Game Over.png")
    
    pygame.mixer.music.pause()
    sound.play()
    time.sleep(9)
    
    while True:
        screen.blit(game_over_img, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        
        pygame.display.update()
        fpsClock.tick(FPS)
    
def gameWin():
    game_win_img = pygame.image.load(r"./img/Win.png")
    pygame.mixer.music.pause()
    while True:
        screen.blit(game_win_img, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        
        pygame.display.update()
        fpsClock.tick(FPS)

# Game 1
def gamePlay1(difficulty):
    
    # difficulty
    """ Easy thời gian bấm nut = 2s
        Hard thời gian bấm nút = 0.5s
        Insane thời gian bấm nút = 0.5s với chữ hinagana"""
    if(difficulty == 'Easy'):
        time_limit = 3.5
        font_name = 'LEMONMILK-Regular.otf'
    elif(difficulty == 'Hard'):
        time_limit = 1.5
        font_name = 'LEMONMILK-Regular.otf'
    elif(difficulty == 'Insane'):
        time_limit = 1.5
        hinagana = pygame.image.load(r"./img/Hinagana.png")
        font_name = 'hiragana tfb.ttf'
    
    # init object and ultis
    engine = Game1Engine(True, 10 * 60)
    player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED)
    button = Button(True, time_limit, font_name)
    
    # Load music
    pygame.mixer.music.pause()
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
        if(engine.play_main_music == False):
            music.pause()
        elif(engine.play_main_music == True):
            music.unpause()
        # move in red light time
        engine.changeStatus()
        engine.drawTime(screen)
        if(difficulty == 'Insane'):
            screen.blit(hinagana, (510,0))
        if (engine.moveInRedLight(move_left or move_right or move_up or move_down)) :
            game_over = True
        
        # hit button in red light time
        # Bắt đầu đèn đỏ thì tạo 1 nút mới
        if(engine.start_red_light):
            button.generateButton()
            engine.start_red_light = False
        if(not engine.green_light):
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
        if(engine.outOfTime()):
            game_over = True
        
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
            music.stop()
            gameWin()

# Game 2
def gamePlay2(difficulty):
    
    if(difficulty == 'Easy'):
        shape_set = ['Circle', 'Poly', 'Rec']
    elif(difficulty == 'Hard'):
        shape_set = ['Mail', 'Snow', 'Web']
    elif(difficulty == 'Insane'):
        shape_set = ['Ship', 'Tree', 'Dragon']
        
    crack_sound = pygame.mixer.Sound(r"./Music/Crack Sound Effect.mp3")
    
    
    CURSOR_MARGIN = 10
    
    if(difficulty == 'Easy'):
        timer = Timer(3 * 60)
    elif(difficulty == 'Hard'):
        timer = Timer(10 * 60)
    elif(difficulty == 'Insane'):
        timer = Timer(15 * 60)
    
    shape_name = random.choice(shape_set)
    
    # init
    # load data
    if(not os.path.exists(r"./Map/{}Map.txt".format(shape_name))) :
        generateShapeMap(shape_name)
        
    shape_map = loadShapeMap(r"./Map/{}Map.txt".format(shape_name))
    
    img = pygame.image.load(r"./img/Shape/{}.png".format(shape_name))
    # Đếm số pixel cần phải tô màu để thắng
    max_pixel = 0
    for i in shape_map :
        for x in i :
            if x == 1:
                max_pixel += 1

    # init surface and color
    green = pygame.Color(0,255, 0, 255)
    
    background_sur = pygame.Surface((800,600))
    
    # background
    background = pygame.image.load(r"./img/BG2_1.jpg")
    
    # draw base image
    background_sur.blit(background, (0, 0))
    background_sur.blit(img, (0, 0))
    
    
    # init variable
    game_over = False
    
    pixel = 0
    
    if(difficulty == 'Easy'):
        remaining_life = 3
    elif(difficulty == 'Hard'):
        remaining_life = 9
    elif(difficulty == 'Insane'):
        remaining_life = 15
        
    # Game Loop
    
    mousedown = False
    while True:
        
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
                crack_sound.play()
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
                 text='Remaning Life : {}'.format(remaining_life), color='White', coordinates = (500,0))
        
        pygame.display.update()
        fpsClock.tick(FPS)
        
        if(pixel == max_pixel): 
            gameWin()
        
        # Game Over!
        if(game_over):
            gameOver()

def difficulty_select():
    main_menu = pygame.image.load(r"./img/Level.png")
    while True:
        screen.blit(main_menu, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                y ,x = pygame.mouse.get_pos()
                # Circle
                if(x >= 226 and y >= 105 and x <= 368 and y <= 254):
                    return 'Easy'
                # Tri
                if(x >= 238 and y >= 322 and x <= 397 and y <= 507):
                    return 'Hard'
                # Rec
                if(x >= 217 and y >= 547 and x <= 387 and y <= 712):
                    return 'Insane'
        
        pygame.display.update()
        fpsClock.tick(FPS)
def main():
    main_menu = pygame.image.load(r"./img/Menu_1.png")
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(main_menu, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                y ,x = pygame.mouse.get_pos()
                # Circle
                if(x >= 226 and y >= 105 and x <= 368 and y <= 254):
                    difficulty = difficulty_select()
                    gamePlay2(difficulty)
                # Tri
                if(x >= 238 and y >= 322 and x <= 397 and y <= 507):
                    pygame.quit()
                # Rec
                if(x >= 217 and y >= 547 and x <= 387 and y <= 712):
                    difficulty = difficulty_select()
                    gamePlay1(difficulty)
        
        pygame.display.update()
        fpsClock.tick(FPS)

main()