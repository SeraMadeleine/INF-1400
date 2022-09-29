import pygame
from pygame import Vector2

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
RED = (205,51,51)
YELLOW = (255,215,0)
BLUE = (187,255,255)

# Screen 
screen_width = 800      # Screen witdh 
screen_height = 600     # Screen heihjt 
SCREEN = (screen_width, screen_height) 
screen = pygame.display.set_mode(SCREEN, 0, screen_height)
bg = BLACK              # Background color 

# Boids 
color_boids = BLUE
boids_height = 30
boids_width = 40
num_boids = 130
boids_radius = 4

# Hoiks 
color_hoiks = RED 
num_hoiks = 3
radius_hoiks = 8

# Obstacelas
num_obstacelas = 2
color_obstaclas = YELLOW
radius_obs = 50