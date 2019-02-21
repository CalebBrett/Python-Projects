import pygame
import math
import random

white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
orange = (255,127,39)

size = (40,40)

class Entity(pygame.sprite.Sprite):
        def __init__(self, size, colour):
                pygame.sprite.Sprite.__init__(self)
                self.imageMaster = pygame.image.load('Images\Enemy2.jpg').convert()
                self.image = self.imageMaster
                self.rect = self.image.get_rect()
                self.image.set_colorkey(white)

                self.dx = 0
                self.dy = 0
                self.distance = 0
                
        def draw(self, screen):
                pygame.draw.rect(screen, self.colour, self.rect)

        def move(self):
                if (self.rect.x < 0):
                       self.dx *= -1
                        
                self.rect.x += self.dx
                self.rect.y += self.dy


        def update(self):
                self.move()
                if self.rect.y > HEIGHT - 90:
                        self.rect.y = 5

class PlayerClass(Entity):
        levelnum = 1
        lives = 3
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.imageMaster = pygame.image.load('Images\Ship-Idle.bmp').convert()
                self.image = self.imageMaster
                self.rect = self.image.get_rect()
                self.image.set_colorkey(white)
                
        def move(self):                        
                        
                self.rect.x += self.dx
                self.rect.y += 0
                
        def finish(self):
                if self.rect.right > WIDTH:
                        self.levelnum += 1
                        self.rect.x = 0
                                
                        if self.levelnum == 2:
                                for i in range(1000):
                                        Enemy = Entity(10, white)
                                        Enemy.rect.x = random.randrange(0,WIDTH)
                                        Enemy.rect.y = 5
                                        Enemy.dx = 0
                                        Enemy.dy = random.randrange(1,10)
                                        Enemy_list.add(Enemy)


pygame.init()

font = pygame.font.Font(None, 36)

# Setting up the window
WIDTH = 1320
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((SIZE), pygame.FULLSCREEN)

#Player
Player = PlayerClass()
Player.rect.x = 50
Player.rect.y = 50
Player.dx = 0
Player.dy = 5

player_list = pygame.sprite.Group()
player_list.add(Player)

Enemy_list = pygame.sprite.Group()

bg = pygame.image.load("Images\stars.jpg").convert()
bg = pygame.transform.scale(bg, [WIDTH, HEIGHT])


# Boolean for the game loop
done = False
# Framerate for the game
FPS = 120

# Clock object to simulate animation
clock = pygame.time.Clock()

# Main Loop!
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                Player.dx = 2

                        if event.key == pygame.K_LEFT:
                                Player.dx = -2
                                
                        if event.key == pygame.K_UP:
                                Player.rect.y -= 100
                                Player.dy = 5

                        if event.key == pygame.K_ESCAPE:
                                done = True

                if event.type == pygame.KEYUP:

                        if event.key == pygame.K_RIGHT:
                                Player.dx = 0

                        if event.key == pygame.K_LEFT:
                                Player.dx = 0


                

        screen.blit(bg, [0,0])

        Enemy_list.update()
        player_list.update()
        Player.finish()

        text = font.render("Level : " + str(Player.levelnum), True, green)
        textpos = [10,10]
        screen.blit(text, textpos)

        text = font.render("Lives : " + str(Player.lives), True, green)
        textpos = [WIDTH - 100,10]
        screen.blit(text, textpos)
        
       
        if pygame.sprite.groupcollide (Enemy_list, player_list, True, False):
                Player.lives -= 1
                Player.rect.x = 10
        
        player_list.draw(screen)
        Enemy_list.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()
