import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0,0,0))
running = True

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          elif event.type == pygame.MOUSEBUTTONDOWN: # When the mouse button is pressed
               print(event.pos)
          elif event.type == MOUSEBUTTONUP: # When the mouse button is released
               print(event)
          elif event.type == MOUSEMOTION:   # When the mouse is moved
               print(event)

pygame.quit()