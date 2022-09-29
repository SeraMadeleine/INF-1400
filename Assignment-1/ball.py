import pygame
from game_variables import *

class Ball(pygame.sprite.Sprite): 
    def __init__(self, radius, ball_speed_x, ball_speed_y):
        super().__init__()
        # Takes the image of the ball and scales it
        self.image = ball_img # importes the image from the game variables 
        self.image = pygame.transform.scale(self.image, [(radius * 2), (radius * 2)])
        
        # Obtains the image's rectangle and determines where the ball should be positioned
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2((screen_width//2), (screen_height - (50 + ball_radius))) 

        # Defines the ball's position, radius, and speed
        self.circle_radius = radius    
        self.circle_speed_x = ball_speed_x
        self.circle_speed_y = ball_speed_y

        self.mask = pygame.mask.from_surface(self.image)

    def update(self): 
        # Updates the position of the ball with respect to speed        
        self.rect.x += self.circle_speed_x 
        self.rect.y += self.circle_speed_y

        # Determines whether the ball collide with the top of the screen or whether it hits 
        # The bottom of the screen, and adjust the ball-speed accordingly.  
        if self.rect.bottom > screen_height or self.rect.top < 0:
            self.circle_speed_y *= -1
    
        # Determines whether the ball collides with the right or left side of the screen.        
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.circle_speed_x  *= -1

        self.ball_position = self.rect.x + self.circle_radius   # Used in main to change the angle of the ball

    # Creates a function for the ball to bounce of the wall 
    def bounce_wall(self): 
        self.circle_speed_x *= -1
        self.circle_speed_y *= -1