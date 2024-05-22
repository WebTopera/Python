import pygame
from pygame import mixer
from pygame.locals import *
import random

Clock = pygame.time.Clock()
fps = 60
running = True
rows = 5
cols = 5
alien_cooldown = 1000

screen_width = 600
screen_height = 800

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

background_fx = pygame.mixer.Sound('resources/Background_fx.mp3')
background_fx.set_volume(0.75)
background_fx.play(1000)
#colors
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

explosion_fx = pygame.mixer.Sound('resources/explosion.wav')
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound('resources/explosion2.wav')
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound('resources/laser.wav')
laser_fx.set_volume(0.25)

last_alien_shot = pygame.time.get_ticks()
coutdown = 3
last_cout = pygame.time.get_ticks()
game_over = 0

# Load images
bg = pygame.image.load('resources/background.png')

def draw_background():
    screen.blit(bg, (0, 0))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
    def update(self):
        speed = 8

        cooldown = 500

        game_over = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed
        
        time_now = pygame.time.get_ticks()

        # draw bullets
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            Bullet_group.add(bullet)
            self.last_shot = time_now

        #update maks
        self.mask = pygame.mask.from_surface(self.image)

        #draw health bar
        pygame.draw.rect(screen, red,(self.rect.x, (self.rect.bottom + 10), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green,(self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 10))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery,3)
            Explosion_group.add(explosion)
            self.kill()
            explosion2_fx.play()
            game_over = -1
        return game_over

# create bullet class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        self.rect.y -=5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Aliens_group, True, pygame.sprite.collide_mask):
            self.kill()
            explosion_fx.play()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            Explosion_group.add(explosion)

# create aliens class
class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'resources/alien{random.randint(1,5)}.png')
        self.image.set_colorkey((0,0,0)) # make black background transparent
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.move_counter = 0
        self.move_direction = 1
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        self.mask = pygame.mask.from_surface(self.image)

# create aliens bullet clas
class AliensBullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/alien_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, SpaceShip_group, False, pygame.sprite.collide_mask):
            self.kill()
            for spaceship in SpaceShip_group:
                SpaceShip.health_remaining -= 1
                explosion_fx.play()
                explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                Explosion_group.add(explosion)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'resources/exp{num}.png')
            if size == 1:
                img = pygame.transform.scale(img, (20,20))
            if size == 2:
                img = pygame.transform.scale(img, (40,40))
            if size == 3:
                img = pygame.transform.scale(img, (160,160))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
    def update(self):
        explosion_speed = 3
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()

# create sprite groups
SpaceShip_group = pygame.sprite.Group()
Bullet_group = pygame.sprite.Group()
Aliens_group = pygame.sprite.Group()
AliensBullet_group = pygame.sprite.Group()
Explosion_group = pygame.sprite.Group()

def Create_aliens():
    for row in range(rows):
            for item in range(cols):
                alien = Aliens(100 + item * 100, 100 + row * 70)
                Aliens_group.add(alien)

Create_aliens()
#create player
SpaceShip = SpaceShip(int(screen_width/2),screen_height -100, 3)
SpaceShip_group.add(SpaceShip)

while running:
    Clock.tick(fps)

    draw_background()

    if coutdown == 0:     
        #create random alien bullets
        time_now = pygame.time.get_ticks()
        if (time_now - last_alien_shot > alien_cooldown) and len(AliensBullet_group) < 5 and len(Aliens_group) > 0:
            attacking_alien = random.choice(Aliens_group.sprites())
            aliens_bullet = AliensBullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            AliensBullet_group.add(aliens_bullet)
            laser_fx.play()
            last_alien_shot = time_now

        if len(Aliens_group) == 0:
            game_over = 1

        if game_over == 0:
            game_over = SpaceShip.update()

            Bullet_group.update()
            AliensBullet_group.update()
            Aliens_group.update()
        else:
            if game_over == -1:
                draw_text('GAME OVER!', font40, white, int(screen_width/2 - 110), int(screen_height/2 +50))

            if game_over == 1:
                draw_text('YOU WIN!', font40, white, int(screen_width/2 - 110), int(screen_height/2 +50))
    if coutdown > 0:
        draw_text('GET READY!', font40, white, int(screen_width/2 - 110), int(screen_height/2 +50))
        draw_text(str(coutdown), font30, white, int(screen_width/2 - 10), int(screen_height/2 +100))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_cout > 1000:
            coutdown -= 1
            last_cout = count_timer
    Explosion_group.update() #Update explosion group

    SpaceShip_group.draw(screen)
    Bullet_group.draw(screen)
    AliensBullet_group.draw(screen)
    Aliens_group.draw(screen)
    Explosion_group.draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()