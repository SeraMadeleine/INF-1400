from numpy import half
import pygame
import os       # to add the picture, and the picture file 

'''
This file contains information that should be available in all of the other files.
To avoid double-sided importation, it is placed here rather than in the main. 
They are placed here for easy access if the programmer wishes to modify some of 
the game variables.
'''

# Information about the screen
screen_width = 800      # Screen witdh 
screen_height = 600     # Screen heihjt 
SCREEN = (screen_width, screen_height) 
screen = pygame.display.set_mode(SCREEN, 0, screen_height )  # Has to be here because of the draw text function

# Define the colors 
BLUE = (187,255,255)
BLUE1 = (174,238,238) 
BLUE2 = (150,205,205) 
BLUE3 = (102,139,139)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

# Some defined colors 
REC_COLOR = [BLUE1, BLUE2, BLUE3, BLUE]   # The colors used on the wall's rectangles
bg = BLACK                                # Background color 
text_col = WHITE                          # Text color 
paddle_col = WHITE                        # Paddel color 

# Some game varibles 
game_over = 0
score = 0   # The score. For each block removed, the player receives one point.
lives = 3   # The player's number of lives
live_ball = False  # Determine whether or not the game has begun

# Varibles for the paddle 
paddle_dimension = [(screen_width // 6), 10 ]
paddle_speed = 10  # As many pixels the paddle moves for each time the player press the key
paddle_pos = pygame.Vector2((screen_width//2), (screen_height - 50)) # The paddle position 
halfcircle_rad = (paddle_dimension[0]-2)//2

# Varibles for the wall
rows = 9        # Number of rows 
columns = 6     # Number of columns 
rec = [(screen_width // columns), (int((screen_height * 0.5)//rows))]  # Rectangle witdh and height

# Varibles for the ball 
ball_radius = 15
ball_angle = 45
ball_speed_x = 5
ball_speed_y = -5

# Picture of the ball; https://opengameart.org/content/buttonssquarecirclerecord
game_folder = os.path.dirname(__file__)             # Figures out the path to image folder.
img_folder = os.path.join(game_folder, 'img')       # Make a image folder in the same folder as the game 
ball_img = pygame.image.load(os.path.join(img_folder, 'circle.png'))   

# A function to draw text on the screen 
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
