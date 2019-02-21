# basic_pygame.py
# The basic pygame file to start out this game.
# Pygame must be installed to run program.
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
brown = (139, 69, 13)
orange = (255,140,0)

# Empty class definition for game entities
class Entity():
        def __init__(self, size):
                pass

# Pygame must be initialized before using 
# any of its features
pygame.init()

# Setting up the window for pygame
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

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

        screen.fill(blue)

        pygame.draw.rect(screen, blue, (0,0,40,40))
        pygame.draw.line(screen, brown, (450,450), (300,500), 20)
        pygame.draw.line(screen, brown, (550,450), (700,500), 20)
        pygame.draw.circle(screen, white, (500,600), 100)
        pygame.draw.circle(screen, white, (500,500), 80)
        pygame.draw.circle(screen, white, (500,400), 50)
        pygame.draw.polygon(screen, orange, [[500, 400], [460, 410], [500, 410]], 10)
        pygame.draw.circle(screen, black, (500,600), 10)
        pygame.draw.circle(screen, black, (500,500), 10)
        pygame.draw.circle(screen, black, (465,380), 7)

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
