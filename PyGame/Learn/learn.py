import pygame
from pygame.locals import *

# Initialize the pygame
pygame.init()

key_dict = {K_k:(0, 0, 0),K_r:(255, 0, 0),K_g:(0, 255, 0),K_b:(0, 0, 255),K_y:(255, 255, 0),
K_c:(0, 255, 255), K_m:(255, 0, 255), K_w:(255, 255, 255)}
print(key_dict)
screen = pygame.display.set_mode((640, 240)) # Set the screen size
running = True
background = (255, 255, 0)
screen.fill(background)
pygame.display.update()

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          elif event.type == KEYDOWN:
               if event.key in key_dict:
                    # Change the background color with the color what i allowed
                    background = key_dict[event.key] 
                    # Set the title of the window with the color name
                    pygame.display.set_caption(f'Background color: {str(background)}') 
                    # Fill the screen with the new background color
                    screen.fill(background)
                    # Update the screen
                    pygame.display.update()
