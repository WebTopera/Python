import pygame

def DrawRect():
     pygame.draw.rect(screen, RED, (50, 20, 120, 100))
     pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
     pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))

     # Empty rectangles
     pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1) # The last argument is the thickness of the line
     pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4) # The basic value is 0, then the rectangle is filled
     pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8) # But if you put a value, it will be the thickness of the line
     pygame.display.update()

def DrawElipse():
     pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
     pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
     pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))

     pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
     pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
     pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)
     pygame.display.update()

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0,0,0))
running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DrawRect()
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_1: # Change the the shapes to rectangles, if 1 is pressed
                    screen.fill((0,0,0))
                    DrawRect()
               if event.key == pygame.K_2: # Change the the shapes to elipses, if 2 is pressed
                    screen.fill((0,0,0))
                    DrawElipse()
pygame.quit()
