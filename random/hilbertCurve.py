import pygame, sys
from pygame.locals import *

order = 2
n = int(pow(2, order))
total = n * n

path = ['' for num in range(total)]

pygame.init()
DISPLAY=pygame.display.set_mode((512,512),0,32)
BLACK=(0,0,0)
DISPLAY.fill(BLACK)

WHITE=(255,255,255)

w, h = pygame.display.get_surface().get_size()



def hilbert(i):
    points = [(0,0), (0,1), (1,1), (1,0)]
    index = i & 3

    v = points[index]

    i = i >> 2
    
    index = i & 3

    x,y = v

    if index == 0:
        pass
    elif index == 1:
        v = (x, y+order)
    elif index == 2:
        v = (x+order, y+order)
    elif index == 3:
        v = (x+order, y)

    return v


for i in range(total):
    path[i] = hilbert(i)
    print(path[i])
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