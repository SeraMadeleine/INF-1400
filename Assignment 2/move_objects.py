import pygame
from pygame import Vector2
import random 
from game_variables import * 

# The parrent class 
class MovingObjects(pygame.sprite.Sprite): 
    def __init__(self, radius):
        super().__init__()
        self.radius = radius 
        self.pos = Vector2(random.randrange(boids_radius*2, screen_width-(boids_radius*2)), random.randrange(boids_radius*2, screen_height-(boids_radius*2)))
        self.velocity = Vector2(random.randrange(1, 5), random.randrange(1, 5))
        self.acceleration = Vector2()
