import pygame
from pygame.locals import *

class Game():
     def __init__(self):
          pygame.init()
          pygame.display.set_caption("Snake Game")
          self.surface = pygame.display.set_mode((1000, 500))
          self.surface.fill((255, 255, 255))
          self.Snake = Snake(self.surface)
          self.Snake.draw()

     def run(self):
          running = True

          while running:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         running = False
                    if event.type == KEYDOWN:
                         if event.key == K_ESCAPE:
                              running = False
                         if event.key == K_UP:
                              self.Snake.move_up() 
                         if event.key == K_DOWN:
                              self.Snake.move_down()
                         if event.key == K_LEFT:
                              self.Snake.move_left()
                         if event.key == K_RIGHT:
                              self.Snake.move_right()
          pygame.quit()

class Snake():
     def __init__(self, parent_screen):
          self.parent_screen = parent_screen
          self.block = pygame.image.load('Snake_game/resources/block.jpg').convert()
          self.block_x, self.block_y = 100, 100

     def draw(self):
          self.parent_screen.fill((255, 255, 255))
          self.parent_screen.blit(self.block, (self.block_x, self.block_y))
          pygame.display.flip()

     def move_up(self):
          self.block_y -= 10 # Move the snake up by 10 pixels
          self.draw()

     def move_down(self):
          self.block_y += 10
          self.draw()

     def move_left(self):
          self.block_x -= 10
          self.draw()
          
     def move_right(self):
          self.block_x += 10
          self.draw()

if __name__ == "__main__":
     game = Game()
     game.run()

     
               
               