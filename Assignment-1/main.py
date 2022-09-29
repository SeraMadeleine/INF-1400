import pygame
from paddle import *
from wall import *
from ball import *
from game_variables import *

# Create objects by calling on their class 
paddle = Paddle(paddle_speed, paddle_col, paddle_pos)
ball = Ball(ball_radius, ball_speed_x, ball_speed_y) 

pygame.init()
pygame.display.set_caption("Breakout Game, assignment 1") # Name the window 

clock = pygame.time.Clock()
font1 = font = pygame.font.Font(None, 36)   # Define a text font 
font2 = font = pygame.font.Font(None, 50)   # Define a text font 

# Make a grupe for all the sprites and add all the sprites to the grupe 
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(paddle, ball, rectangel_group)

# The game-loop, which will run indefinitely as long as the game is active.
while True: 
    events = pygame.event.get()
    screen.fill(bg) 

    # Provides an overview of the player's score and the number of lives he has remaining.
    draw_text("Your score:  " + str(score), font1, text_col, (screen_width // 2 ) - (screen_width * 0.45 ) , screen_height //32)  # Her kommer scoren opp
    draw_text("Remaining lives:  " + str(lives), font1, text_col, (screen_width // 2 ) + (screen_width * 0.18 ) , screen_height //32) # Str må inn for å få programmet til å virke 

    # Draw objects 
    all_sprites_group.draw(screen)

    # Determines whether or not the game is active
    if live_ball:     
        # Updates the objects
        all_sprites_group.update()
        rectangel_group.update()
        # If the ball collides with the paddle 
        paddle_collide = pygame.sprite.collide_rect(ball, paddle)
        if paddle_collide: 
            ball.circle_speed_y *= -1
            kollisjon = (paddle.rect.x + paddle.sx//2) - ball.ball_position  # rect.x- sx//2, to find the middle of the platform
            ball.circle_speed_x = 1 * kollisjon//10

        # Use maske to be sure that every part of the ball can be hit, and the wall will be distroyd 
        block_remove = pygame.sprite.spritecollide(ball, rectangel_group, False, pygame.sprite.collide_mask) 
        for block in block_remove: 
            score += 1      # Modifies the score displayed on the screen.
            ball.update()   # Calls the ball object's refresh function
            ball.bounce_wall()   # Uses the ball's bounce function
            block.kill()    # Removes the block with which the ball collided
            if score == rows * columns: 
                game_over = 1

        # One life is lost every time the ball lands at the bottom of the screen.
        if ball.rect.bottom > screen_height:
            if lives > 0:
                lives -= 1   
        # If the player does not have any additional lives, the game is over.
            if lives == 0: 
                ball.circle_speed_x = 0    # The ball will come to a halt in the x direction as a result of this.
                ball.circle_speed_y = 0    # The ball will come to a halt in the y direction as a result of this.
                game_over = -1             # The value -1 informs the game that the player has lost.
        # This is required to notify the game when it is over.
        if game_over != 0: 
            live_ball = False

    # Specify which messages should be displayed on the screen at any given time in the game.
    if not live_ball: 
        if game_over == 0:  
            draw_text('Click anywhere to start', font2, text_col, screen_width//4, screen_height // 2 - 50)
        elif game_over == 1:
            draw_text('You WON!!', font2, text_col, screen_width//3, screen_height // 2 + 50)
        elif game_over == -1:
            draw_text('You LOST!!', font2, text_col, screen_width//3, screen_height // 2 + 50)

    # The player can exit the game by closing the window.
    for event in events: 
        if event.type == pygame.QUIT: 
            exit()
        # Allows the player to begin the game by clicking on the screen with the mouse
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            all_sprites_group.draw(screen)

    time_passed = clock.tick(30) / 1000.0 

    pygame.display.flip()