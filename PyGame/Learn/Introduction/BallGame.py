import pygame
from pygame.locals import *

size = 640, 240
width, height = size
GREEN = (0, 255, 0)
RED = (255, 0, 0) 
# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode(size) # Set the screen size
running = True
# Set the caracteristics of the ball
ball = pygame.image.load('Learn/Introduction/ball.gif')
rect = ball.get_rect()
speed = [2,2]

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          rect = rect.move(speed)
          if rect.left < 0 or rect.right > width:
               speed[0] = -speed[0]
          if rect.top < 0 or rect.bottom > height:
               speed[1] = -speed[1]
          screen.fill(GREEN)
          pygame.draw.rect(screen, RED, rect, 1)
          screen.blit(ball, rect)
          pygame.display.update()

pygame.quit()