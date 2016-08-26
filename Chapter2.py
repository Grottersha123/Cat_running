import pygame, sys
from pygame.locals import *

pygame.init() # init pygame library
FPS = 30
fpsClock = pygame.time.Clock()
DISPLYSURF = pygame.display.set_mode((300,300)) # it is function for set your screen in pixel like x and y so and it use tuple
pygame.display.set_caption('Animation by cat') # set name of your title in display
WHITE = (255,255,255)
CatImg = pygame.image.load('cat.png')
CatImg1 = pygame.image.load('cat.png')
CatImg2 = pygame.image.load('cat.png')
catX = 400
catY = 10
direction = 'left'
catX1 = -10
catY1 = 50
direction1 = 'right'

while True:
    DISPLYSURF.fill(WHITE)
    if  direction == 'left':
        catX -= 10
        if catX <= -100:
            catX += 400
            direction = 'left'
    DISPLYSURF.blit(CatImg, (catX,catY))
    if direction1 == 'right':
        catX1 += 10
        if catX1 >= 300:
            catX1 += -300
            direction1 = 'right'
    DISPLYSURF.blit(CatImg1, (catX1,catY1))
    
    

    for event in pygame.event.get(): # check all your event what you do
        if event.type == QUIT or event.type == MOUSEBUTTONUP:
            pygame.quit() # deactivates the python library
            sys.exit() # it close your program
    pygame.display.update()
    fpsClock.tick(FPS)

