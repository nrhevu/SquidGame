import pygame
from PIL import Image
import numpy as np

def loadShapeMap(filepath):
    shapeMap = list()
    
    file = open(filepath, 'r')

    for i in range(600):
        line = file.readline().split(' ')
        arr = [int(x) for x in line[:-2]]
        shapeMap.append(arr)
    return shapeMap

def generateShapeMap(shape_name):
    im =  Image.open(r"./img/ShapeForMapping/{}.png".format(shape_name)).convert('L')
    arr = np.asarray(im)
    file = open(r"./Map/{}Map.txt".format(shape_name), 'w')

    for i in arr:
        for j in i:
            if(j == 255):
                file.write('0' + ' ')
            else : 
                file.write('1' + ' ')
        file.write('\n')
        
def drawText(surface, font, size, text, color, coordinates):
    FONT = pygame.font.Font('./Font/{}'.format(font), size)
    text_draw = FONT.render(text, 0, color)
    surface.blit(text_draw, coordinates)
    


