import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((152,152,152))
running = True
drawing = False
points = []

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          elif event.type == pygame.KEYDOWN:
               if event.key == K_k:
                    if len(points) > 0:
                         points.pop()
          elif event.type == pygame.MOUSEBUTTONDOWN:
               points.append(event.pos)
               drawing = True
          elif event.type == MOUSEBUTTONUP:
               drawing = False
          elif event.type == MOUSEMOTION and drawing:
               points[-1] = event.pos
     screen.fill((152,152,152))
     if len(points) > 1:
          rect = pygame.draw.lines(screen, (255,0,0), True, points, 3)
          pygame.draw.rect(screen, (0,255,0), rect, 2)
     pygame.display.update()