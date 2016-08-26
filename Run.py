import pygame, sys
from pygame.locals import *

pygame.init() # init pygame library
FPS = 30
fpsClock = pygame.time.Clock()
DISPLYSURF = pygame.display.set_mode((700,700)) # it is function for set your screen in pixel like x and y so and it use tuple
pygame.display.set_caption('Animation by cat') # set name of your title in display
WHITE = (255,255,255)
CatImg = pygame.image.load('cat1.png')
CatImg1 = pygame.image.load('cat2.png')
x1 = y1 = 50
x = y = 100 
while True:
    DISPLYSURF.fill(WHITE)
    DISPLYSURF.blit(CatImg, (x1,y1))
    DISPLYSURF.blit(CatImg1, (x,y))
    D = ((x - x1)**2 + (y-y1)**2)**(1/2)
    FP = int(D/10)
    try :
        x = int((x1 - x) / FP + x)
        y  = int((y1- y) / FP + y )
    except ZeroDivisionError:
        
        x = y = 0 
        
        
    
    
    
    for event in pygame.event.get(): # check all your event what you do
        if event.type == QUIT or event.type == MOUSEBUTTONUP:
            pygame.quit() # deactivates the python library
            sys.exit() # it close your program
        elif event.type == pygame.MOUSEMOTION:
            x1,y1 = event.pos
            
            
            
            
    pygame.display.update()
    fpsClock.tick(FPS)
