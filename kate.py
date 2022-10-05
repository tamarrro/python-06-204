import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_house(surface, x, y, width, height, color):
    
    

 rect(surface,color,(x,y,width,height))
 rect(surface,(0,0,0),(x,y,width,height),2)
 polygon(surface,color, [(x,y),(x+width/2, y-height/3), (x+width,y)])
 polygon(surface,(0,0,0), [(x,y),(x+width/2, y-height/3), (x+width,y)],2)
 rect(surface, 'pink', (x+width/3, y+height/3, width/3, height/3))
 rect(surface, (0,0,0), (x+width/3, y+height/3, width/3, height/3),2)

draw_house(screen, 100, 100, 100, 100,(0,255,0))







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()