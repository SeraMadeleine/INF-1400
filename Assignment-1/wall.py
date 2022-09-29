import pygame 
from game_variables import *

# Sprites are used to create rectangles that will fill the wall.
class Rectangle(pygame.sprite.Sprite): 
    def __init__(self, sx, sy, x, y, color): 
        super().__init__()
        self.sx = sx  # Width of rectangle.
        self.sy = sy  # Height of rectangle.

        # Definerer det som må til for å lage rektanglene 
        self.image = pygame.Surface([self.sx, self.sy])  # The size of the rectangles  
        self.image.fill(color)                           # The colour of the rectangles
        self.rect = self.image.get_rect()
        self.rect.x = x  # The x-position of the rectangle
        self.rect.y = y  # The y-position of the rectangle 

# Creates a group that contains all of the rectangles that are created.
rectangel_group = pygame.sprite.Group()
for row in range(rows): 
    for col in range(columns): 
        if row <=  2:  # For the first tree rows
            rec_x = ((col * (rec[0] + 2)))    # x-position for each rectangle, + 2 for spaces between each block
            rec_y = ((row * (rec[1] + 2)) + screen_height // 12)   # y-position for each rectangle, + 2 for spaces between each block
            rectangel = Rectangle(rec[0] , rec[1], rec_x, rec_y, REC_COLOR[0])  # Makes the rectangles 
        elif row <= 5: # For the next three rows
            rec_x = ((col * (rec[0]  + 2)))   
            rec_y = ((row * (rec[1] + 2)) + screen_height // 12)    
            rectangel = Rectangle(rec[0] , rec[1], rec_x, rec_y, REC_COLOR[1])
        elif row >= 6: # For the rest of the rows 
            rec_x = ((col * (rec[0]  + 2)))    
            rec_y = ((row * (rec[1]  + 2)) + screen_height // 12)    
            rectangel = Rectangle(rec[0] , rec[1], rec_x, rec_y, REC_COLOR[2])

        rectangel_group.add(rectangel)   # Adds all the rectangles to rectangel_group

