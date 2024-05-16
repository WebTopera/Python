import random
import pygame
from pygame.locals import *
import time

SIZE = 40
class Game():
     def __init__(self):
          pygame.init()
          pygame.display.set_caption("Snake Game")
          pygame.mixer.init()
          self.surface = pygame.display.set_mode((1000, 760))
          self.Snake = Snake(self.surface, 4)
          self.Snake.draw()
          self.Apple = Apple(self.surface)
          self.Apple.draw()

     def background(self):
          bg = pygame.image.load('Snake_game/resources/background.jpg')
          self.surface.blit(bg, (0, 0))

     def play_bg_music(self):
          pygame.mixer.music.load('Snake_game/resources/BG_music.wav')
          pygame.mixer.music.play(loops=1000)

     def is_collision(self, x1,y1,x2,y2):
          if x1 < x2 + SIZE and x1 + SIZE > x2 and y1 < y2 + SIZE and y1 + SIZE > y2:
               return True
          return False        

     def play(self):
          self.background()
          self.Snake.walk()
          self.Apple.draw()
          self.display_score()
          pygame.display.flip()
          # Snake colliding with apple
          if self.is_collision(self.Snake.block_x[0], self.Snake.block_y[0], self.Apple.block_x, self.Apple.block_y):
               sound = pygame.mixer.Sound('Snake_game/resources/ding.mp3')
               pygame.mixer.Sound.play(sound)
               self.Snake.incresse_lenght()
               self.Apple.move()

          # Snake colliding with itself
          for i in range(3, self.Snake.length):
               if self.is_collision(self.Snake.block_x[0], self.Snake.block_y[0], self.Snake.block_x[i], self.Snake.block_y[i]):
                    sound = pygame.mixer.Sound('Snake_game/resources/crash.mp3')
                    pygame.mixer.Sound.play(sound)
                    raise "Game Over"
          # Snake colliding with the boundries of the window
          if not((0 <= self.Snake.block_x[0] <= 1000) and (0 <= self.Snake.block_y[0] <= 760)):
               sound = pygame.mixer.Sound('Snake_game/resources/crash.mp3')
               pygame.mixer.Sound.play(sound)
               raise "Game Over"
          
     def display_score(self):
          font = pygame.font.SysFont('arial', 30)
          score = font.render(f"Score: {self.Snake.length}", True, (255, 255, 255))
          self.surface.blit(score, (800, 10))

     def show_game_over(self):
          self.surface.fill((0,0,0))
          font = pygame.font.SysFont('arial', 40)
          line1 = font.render(f"Game is over! Your score is {self.Snake.length}", True, (255, 255, 255))
          self.surface.blit(line1, (200, 200))
          line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
          self.surface.blit(line2, (200, 300))
          pygame.display.flip()
          pygame.mixer.music.pause()
          while True:
               for event in pygame.event.get():
                    if event.type == QUIT:
                         pygame.quit()
                    if event.type == KEYDOWN:
                         if event.key == K_RETURN:
                              self.__init__()
                              self.run()
                              pygame.mixer.music.unpause()
                         if event.key == K_ESCAPE:
                              pygame.quit()
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
               
               try:
                    self.play()
               except Exception as e:
                    self.show_game_over()

               time.sleep(0.1999)
          pygame.quit()

class Snake():
     def __init__(self, parent_screen, lenght):
          self.length = lenght
          self.parent_screen = parent_screen
          self.block = pygame.image.load('Snake_game/resources/head/head_right.png').convert_alpha()
          self.block_x, self.block_y = [SIZE]*lenght, [SIZE]*lenght
          self.direction = 'right'
          self.rotate = 0

     def draw(self):
          for i in range(self.length):
               if i == 0:
                    self.block = pygame.image.load(f'Snake_game/resources/head/head_{self.direction}.png').convert_alpha()
               elif i == self.length-1:
                    self.block = pygame.image.load(f'Snake_game/resources/tail/tail_{self.direction}.png').convert_alpha()
               else:
                    self.block = pygame.image.load(f'Snake_game/resources/body/body_{self.direction}.png').convert_alpha()
               self.block = pygame.transform.rotate(self.block, self.rotate)
               self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
          pygame.display.update()

     def incresse_lenght(self):
          self.length += 1
          self.block_x.append(-1)
          self.block_y.append(-1)

     def move_up(self):
          if self.direction == 'down' or self.direction == 'up':
               return
          else:
               self.direction = 'up' # Move the snake up by 10 pixels

     def move_down(self):
          if self.direction == 'up' or self.direction == 'down':
               return
          else:
               self.direction = 'down'
               
     def move_left(self):
          if self.direction == 'right' or self.direction == 'left':
               return
          else:
               self.direction = 'left'
          
     def move_right(self):
          if self.direction == 'left' or self.direction == 'right':
               return
          else:
               self.direction = 'right'

     def walk(self):

          for i in range(self.length-1, 0, -1):
               self.block_x[i] = self.block_x[i-1]
               self.block_y[i] = self.block_y[i-1]

          if self.direction == 'up':
               self.block_y[0] -= SIZE

          elif self.direction == 'down':
               self.block_y[0] += SIZE

          elif self.direction == 'left':
               self.block_x[0] -= SIZE

          elif self.direction == 'right':
               self.block_x[0] += SIZE

          self.draw()

class Apple():
     def __init__(self, parent_screen):
          self.parent_screen = parent_screen
          self.block = pygame.image.load('Snake_game/resources/apple.jpg').convert()
          self.move()
     def draw(self):
          self.parent_screen.blit(self.block, (self.block_x, self.block_y))
          pygame.display.update()
     def move(self):
          self.block_x = random.randint(0, (1000//SIZE) -1)*SIZE
          self.block_y = random.randint(0, (760//SIZE) -1)*SIZE
     
if __name__ == "__main__":
     game = Game()
     game.play_bg_music()
     game.run()

     
               
               