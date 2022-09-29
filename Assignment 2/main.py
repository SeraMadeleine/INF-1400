#!/usr/bin/env python 3

import pygame 
from game_variables import * 
from move_objects import *
from boids import *
from hoiks import *
from obstacelas import *

pygame.init()   # Initialize the game
pygame.display.set_caption("Bodis, assignment 2")  # Name the window 

clock = pygame.time.Clock()     # For an even update

boids = pygame.sprite.Group()   # A group for all boids 
hoiks = pygame.sprite.Group()   # A group for all hoiks 
obstacles  = pygame.sprite.Group()

# Loops to add all the elemtens in the right groups 
for i in range(num_boids): 
    boid_ = Boids(color_boids, boids_radius, boids, hoiks, obstacles)
    boids.add(boid_) 

for i in range(num_hoiks): 
    hoik = Hoiks(radius_hoiks, color_hoiks, hoiks, boids)
    hoiks.add(hoik)


for i in range (num_obstacelas): 
    obs = Obstacelas(color_obstaclas, radius_obs)   # boids, hoiks, obsicals
    obstacles.add(obs)


all_objects = pygame.sprite.Group()         # A group for all objects 
all_objects.add(obstacles, boids, hoiks)     # Add all the objcts to the group 

# The game-loop, which will run indefinitely as long as the game is active.
while True: 
    events = pygame.event.get()
    screen.fill(bg)                 # Fill screen with color 
    all_objects.draw(screen)        # Draw all objects 

    all_objects.update()            # Update all objets 

    if pygame.sprite.groupcollide(boids, hoiks, True, False): 
        pass 

    for boid in boids:
        boid.update_hoik_list(hoiks)

    for event in events: 
        if event.type == pygame.QUIT: 
            exit()
    time_passed = clock.tick(30) / 1000.0 
    pygame.display.update()

