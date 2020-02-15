import pygame, sys
from pygame.locals import *

pygame.init()
win=pygame.display.set_mode((768,768),0,32)
win.fill((0,0,0))

w, h = pygame.display.get_surface().get_size()


class hilbert(object):
    def __init__(self, screen_width):
        self.order = 0
        self.points = [(0,0), (0,1), (1,1), (1,0)]
        self.counter = 0
        self.w = screen_width
        self.total = 0
        self.path = []

    def hilbert(self, i):
        index = i & 3
        v = self.points[index]

        for num in range(1, self.order):
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

    def generate_next(self):
        n = int(pow(2, self.order))
        scale = self.w // n
        self.total = n * n
        self.path = ['' for num in range(self.total)]

        for i in range(self.total):
            self.path[i] = self.hilbert(i)
            self.path[i] = tuple([scale * num for num in self.path[i]])
            self.path[i] = tuple([num + (scale/2) for num in self.path[i]])
        
        self.order += 1

    def generate_specific(self, order):
        pass

    def redraw(self, win):
        for i in range(self.counter-1):
            pygame.draw.line(win, (255,255,255), self.path[i], self.path[i+1])

        pygame.display.update()
        
        if self.counter == self.total:
            self.counter = 0
            self.generate_next()
            win.fill((0,0,0))
        
        self.counter +=1

hilbert1 = hilbert(w)

# main loop
while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    hilbert1.redraw(win)
