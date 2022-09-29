import pygame
from game_variables import *
from ball import *

# Sprites are used to create the paddle 
class Paddle(pygame.sprite.Sprite):
    def __init__(self, speed, color, paddle_pos):
        super().__init__()
        self.sx = paddle_dimension[0]      # Width of rectangle.
        self.sy = paddle_dimension[1]      # Height of rectangle.

        self.image = pygame.Surface([self.sx, self.sy])         # What the paddle will look like
        self.image.fill(color)                                  # The paddle color 
        self.rect = self.image.get_rect(center = paddle_pos)    # The starting position of the paddle
        self.speed = speed                                      # speed  
        

    # This function allows the player to move the paddle around by using the arrow keys.
    def update(self):         
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:  # Checks if the right key is pressed 
            self.rect.x += self.speed                 
        elif key[pygame.K_LEFT] and self.rect.left > 0:             # Checks if the left key is pressed 
            self.rect.x -= self.speed