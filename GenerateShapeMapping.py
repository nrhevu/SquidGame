import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

im =  Image.open(r"./img/Flower.png").convert('L')
arr = np.asarray(im)
file = open(r"./Map/FlowerMap.txt", 'w')

for i in arr:
    for j in i:
        if(j == 255):
            file.write('0' + ' ')
        else : 
            file.write('1' + ' ')
    file.write('\n')

