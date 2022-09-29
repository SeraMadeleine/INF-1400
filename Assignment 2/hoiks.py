import imp
import pygame 
from move_objects import * 
from boids import *

class Hoiks(MovingObjects): 
    def __init__(self, radius, color, group_hoiks, group_boids): 
        super().__init__(radius)
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.group = group_hoiks       # A group for all the hoiks 
        self.boids = group_boids       # A group for all the boids 

        pygame.draw.circle(self.image, color, (radius, radius), radius)     
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y)) 

        self.mask = pygame.mask.from_surface(self.image)

    # More or less the same code ass in boids.py
    # Hoiks trying to fly towards the center of all boids  
    def cohesion(self): 
        pc_j = Vector2()       # Perceived center 
        radius = 100           # Radius to the area of interest
        number_boids = 0       # The number of boids found in the area 

        for b in self.boids:                        # For each b in the boids group 
            distance = self.pos.distance_to(b.pos)
            if b != self and distance < radius:      # If b != self, and we are inside the area of interest
                pc_j += b.pos               # Update the vector with the boid position 
                number_boids += 1

        if number_boids != 0:               # If there are boids within the area of interest
            pc_j = pc_j //(number_boids)    # Takes the vector and scales it in terms of the number of boids in the area
            pc_j = (pc_j - self.pos)        # Subtracts the vector from the position of the boids
            if pc_j.length()!= 0:           # As long as the lengt of the vector is not 0 
                pc_j.scale_to_length(5)     # Scale the length to change the velocity 

            pc_j = (pc_j - self.velocity)   # The vector minus the velocity to the given boid 

        return pc_j 


    # Hoiks trying to keep a distance from eachother 
    def separation(self): 
        c = Vector2(0,0)        # Creata a zero vector 
        radius = 40             # Radius to the area of interest
        number_hoiks = 0        # The number of hoiks found in the area 

        for h in self.group:    # For each h in the group of hoiks 
            distance = self.pos.distance_to(h.pos)     # Find the distance between self and h 
            if h!= self and distance < radius and distance != 0:
                diff = self.pos - h.pos      # Find the diffrense between the two positions 
                diff /= distance             # Update the diffrence 
                c += diff                    # Add the diffrence to the c vector to find the new vector 
                number_hoiks += 1            # Change the number of hoiks found in the area 
        if number_hoiks != 0:
            c = c //(number_hoiks)           # To find the vector for one hoik, divide by the number of hoiks 
            if c.length()!= 0:               
                c.scale_to_length(5)         # Change the length to change the velocity 

            c -= self.velocity                        

        return c

    # Hoiks trying to to match velocity with nearby boids.
    def alignment(self): 
        pv_j = Vector2()    # A empty vector 
        radius = 100        # The area of intrest 
        number_boids = 0    # Number of boids 

        for b in self.boids:        # For each boid in the group of boids 
            distance = self.pos.distance_to(b.pos)  # Find the disctance 
            if b != self and distance < radius: 
                pv_j += b.velocity  # Update the vector with the velocity of the given boid 
                number_boids += 1   # Chang the number of boids 

        if number_boids != 0:
            pv_j = pv_j //(number_boids)   # To find the vector for one boid, divide by the number of boids 
            if pv_j.length()!= 0: 
                pv_j.scale_to_length(5)    # Scale the length to change the velocity 

            pv_j = (pv_j - self.velocity)

        return pv_j

    def update(self):
        self.acceleration *= 0 

        self.rect = pygame.Rect(self.pos.x, self.pos.y, boids_radius, boids_radius)
        # Screen bounding 
        if self.rect.x < 0: 
            self.pos.x = screen_width 
        if self.pos.x > screen_width: 
            self.pos.x = 0 

        if self.pos.y < 0: 
            self.pos.y = screen_height
        if self.pos.y > screen_height: 
            self.pos.y = 0 

        v1 = self.cohesion()      # Call on the cohesion 
        v2 = self.separation()    # Call on the separation 
        v3 = self.alignment()     # Call on the alignment 

        # Scale the vectors so the power does not become to excessive
        v1 *= 0.6   
        v2 *= 0.3
        v3 *= 0.1   

        self.acceleration += v1 + v2 + v3     # Add all the vectors to the acceleration
        
        self.velocity += self.acceleration    # Add the acceleration to the velocity
        self.velocity.scale_to_length(7)      # Scale the velocity
        self.pos += self.velocity             # Add the velocity to the posistion to change the position 
        


