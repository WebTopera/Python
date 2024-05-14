import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0,0,0))
running = True
start = (0,0)
size = (0,0)
drawing = False
rect_list = []
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
               start = event.pos
               size = 0,0
               drawing = True
          elif event.type == MOUSEBUTTONUP:
               end = event.pos
               size = end[0] - start[0], end[1] - start[1]
               rect = Rect(start, size)
               rect_list.append(rect)
               drawing = False
          elif event.type == MOUSEMOTION and drawing:
               end = event.pos
               size = end[0] - start[0], end[1] - start[1]
     screen.fill((0,0,0))
     for rect in rect_list:
          pygame.draw.rect(screen, (255,0,0), rect, 2)
     pygame.draw.rect(screen, (255,0,0), (start, size), 2)
     pygame.display.update()
pygame.quit()