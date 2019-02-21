# basic_pygame.py
# The basic pygame file to start out this game.
#
# David Murphy
# August 5th, 2013

import pygame
import math
import random

# Declare some colours to use
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

# Empty class definition for game entities
class Snow():
        def __init__(self, size, colour):
                self.rect = pygame.Rect(0,0,size,size)
                self.dx = 0
                self.dy = 0
                self.colour = colour

        def draw(self):
                pygame.draw.rect(screen, self.colour, self.rect)

        def move(self):
                self.rect.x += self.dx
                self.rect.y += self.dy

                if snow1.rect.y >= HEIGHT:
                        snow1.rect.x = random.randrange(5,790)
                        snow1.rect.y = 1
                        snow1.dy = random.randrange(1,10)
                        
                if snow2.rect.y >= HEIGHT:
                        snow2.rect.x = random.randrange(5,790)
                        snow2.rect.y = 1
                        snow2.dy = random.randrange(1,10)
                        
                if snow3.rect.y >= HEIGHT:
                        snow3.rect.x = random.randrange(5,790)
                        snow3.rect.y = 1
                        snow3.dy = random.randrange(1,10)
                        
                if snow4.rect.y >= HEIGHT:
                        snow4.rect.x = random.randrange(5,790)
                        snow4.rect.y = 1
                        snow4.dy = random.randrange(1,10)

                if (self.rect.x < 0 or self.rect.right > WIDTH):
                        self.dx *= -1
                
# Pygame must be initialized before using 
# any of its features
pygame.init()

# Setting up the window for Pygame
WIDTH = 800
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

# Instantiate the Entity object
snow1 = Snow(20, white)
snow1.rect.x = random.randrange(5,790)
snow1.rect.y = 1
snow1.dy = random.randrange(1,10)

snow2 = Snow(20, white)
snow2.rect.x = random.randrange(5,790)
snow2.rect.y = 1
snow2.dy = random.randrange(1,10)

snow3 = Snow(20, white)
snow3.rect.x = random.randrange(5,790)
snow3.rect.y = 1
snow3.dy = random.randrange(1,10)

snow4 = Snow(20, white)
snow4.rect.x = random.randrange(5,790)
snow4.rect.y = 1
snow4.dy = random.randrange(1,10)

ball = Entity(50, red)
ball.rect.x = random.randrange(5,790)
ball.rect.y = 1
ball.dx = 50
ball.dy = 50


# Boolean for the game loop
done = False
# Framerate for the game
FPS = 60
# Clock object to simulate animation
clock = pygame.time.Clock()

# Main Loop!
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Game Logic Below! i.e. movement

        # Drawing code below!
        screen.fill(blue)

        snow1.move()
        snow1.draw()

        snow2.move()
        snow2.draw()

        snow3.move()
        snow3.draw()

        snow4.move()
        snow4.draw()

        ball.move()
        ball.draw()
        
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
