import pygame 
from game_variables import * 
import random

class Obstacelas(pygame.sprite.Sprite):
    def __init__ (self, color, radius):
        super().__init__()

        max = Vector2(screen_width - radius*2, screen_height - radius*2)    
        min = Vector2(radius*2, radius*2)
        # A vector for the posistion of the obsticals 
        self.pos = Vector2(random.randrange(min.x, max.x), random.randrange(min.y, max.y))

        self.image = pygame.Surface([radius, radius])         # What the paddle will look like
        self.image.fill(color)                                  # The paddle color 
        self.rect = self.image.get_rect(center = self.pos)    # The starting position of the paddle




