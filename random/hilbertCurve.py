import pygame, sys
from pygame.locals import *

order = 4
n = int(pow(2, order))
total = n * n

path = ['' for num in range(total)]

pygame.init()
DISPLAY=pygame.display.set_mode((768,768),0,32)
BLACK=(0,0,0)
DISPLAY.fill(BLACK)

WHITE=(255,255,255)

w, h = pygame.display.get_surface().get_size()



def hilbert(i):
    points = [(0,0), (0,1), (1,1), (1,0)]

    
    index = i & 3
    v = points[index]

    for num in range(1, order):
        num = int(pow(2, num))
        i = i >> 2
        index = i & 3

        x,y = v

        if index == 0:
            v = y,x
        elif index == 1:
            v = (x, y+num)
        elif index == 2:
            v = (x+num, y+num)
        elif index == 3:
            y,x = num-1-x,num-1-y
            v = (x+num, y)
        
    return v


for i in range(total):
    path[i] = hilbert(i)
    scale = w // n
    path[i] = tuple([scale * num for num in path[i]])
    path[i] = tuple([num + (scale/2) for num in path[i]])

for i in range(total-1):
    pygame.draw.line(DISPLAY, WHITE, path[i], path[i+1])


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()