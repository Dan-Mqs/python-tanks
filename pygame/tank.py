import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load('desert.jpg')

tank = pygame.transform.scale(pygame.image.load('tanque.png'), (200,75))

x,y = 0,0
move_x, move_y = 0,0
orientation = 0

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
                orientation = 0
            if event.key == K_RIGHT:
                move_x = 10
                orientation = 180
            if event.key == K_UP:
                move_y = -10
                orientation = -90
            if event.key == K_DOWN:
                move_y = 10
                orientation = 90
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            if event.key == K_RIGHT:
                move_x = 0
            if event.key == K_UP:
                move_y = 0
            if event.key == K_DOWN:
                move_y = 0

        x += move_x
        y += move_y

        screen.blit(background, (0,0))
        
        screen.blit(pygame.transform.rotate(tank, orientation),(x,y))
        
        pygame.display.update()
        
