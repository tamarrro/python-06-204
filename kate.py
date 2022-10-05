import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))


def draw_house(surface, x, y, width, height, color):
    
    

 rect(surface,color,(x,y,width,height))
 rect(surface,(0,0,0),(x,y,width,height),2)
 polygon(surface,color, [(x,y),(x+width/2, y-height/3), (x+width,y)])
 polygon(surface,(0,0,0), [(x,y),(x+width/2, y-height/3), (x+width,y)],2)
 rect(surface, 'pink', (x+width/3, y+height/3, width/3, height/3))
 rect(surface, (0,0,0), (x+width/3, y+height/3, width/3, height/3),2)

draw_house(screen, 100, 100, 100, 100,(0,255,0))

def draw_animal(surface, a, b, wid, hei, color):
    rect(surface,color, (a,b,wid*2/3,hei*2/3))
    circle(surface, color, (a+wid*5/6, b+hei/6), wid/6)
    ellipse(surface,'pink', (a+wid/10,b+hei/2+20,20,30))
    ellipse(surface,'pink', (a+wid*5/10,b+hei/2+20,20,30))
    rect(surface,color,(a-40,b+hei/2,40,10))
    
    
draw_animal(screen,450,100,200,150, 'pink')   







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()