from turtle import distance
import pygame 
from move_objects import * 
from pygame import Vector2


class Boids(MovingObjects): 
    def __init__(self, color, radius, group_boids, group_hoiks, group_obsticals): 
        super().__init__(radius) 
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.group = group_boids
        self.hoiks = group_hoiks
        self.obsticals = group_obsticals

        # pygame.draw.circle(self.image, color, (self.pos.x, self.pos.y), radius)
        pygame.draw.circle(self.image, color, (radius, radius), self.radius)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))

        self.mask = pygame.mask.from_surface(self.image)

    # Boids try to fly towards the centre of mass of neighboring  boids.
    # (source: http://www.kfish.org/boids/pseudocode.html)
            # Cohesion
    def Cohesion(self):
        pc_j = Vector2()    # Vector for the perceived center 
        radius = 100        # The area of intrest 
        number_boids = 0    # The number of boids inside the area of intrest 

        for b in self.group:        # For each boid b in the boids group      
            distance = self.pos.distance_to(b.pos)  # Find the distance between b and self 
            if b != self and distance < radius: 
                pc_j += b.pos       # Update the vector with the position of the boid 
                number_boids += 1   # Update the number of boids 

        if number_boids != 0:
            pc_j = pc_j //(number_boids)   # Fint the perceived center vector for all the boids inside the given radius 
            pc_j = (pc_j - self.pos)       
            if pc_j.length()!= 0: 
                pc_j.scale_to_length(5)     # Scale the vector 

            pc_j = (pc_j - self.velocity)   # Subtract the postion of the given boid from the vector for the perceived center 
        return pc_j
        
    # Boids try to keep a small distance away from other objects 
    # (source: http://www.kfish.org/boids/pseudocode.html)
        # Separation
    def Separation(self): 
        c = Vector2(0,0)    # Create a zero vector 
        radius = 40         # Radius for the area of intrest 
        number_boids = 0    # Number of boids in the area 
        number_hoiks = 0    # Number of hoiks in the area 
        number_obsticals = 0

        for b in self.group:       # For each boid b in the boids group
            distance = self.pos.distance_to(b.pos)  # Find the distance between self and b 
            if b!= self and distance < radius and distance != 0:
                diff = self.pos - b.pos   # Find the difference in position between self and b
                diff /= distance           
                c += diff                 # Add the difference to vector c 
                number_boids += 1

        for h in self.hoiks:    # For each hoik h in the hoiks group 
            distance = self.pos.distance_to(h.pos) # Find the distance between self and h 
            if h!= self and distance < 70 and distance != 0:  # 70 because we want the hoiks to keep a lager distance to eachother 
                diff = self.pos - h.pos   # Find the difference 
                diff /= distance          
                c += diff 
                number_hoiks += 1
        

        for o in self.obsticals:    # For each hoik h in the hoiks group 
            distance = self.pos.distance_to(o.pos) # Find the distance between self and h 
            if o!= self and distance < 90 and distance != 0:  # 70 because we want the hoiks to keep a lager distance to eachother 
                diff = self.pos - o.pos   # Find the difference 
                diff /= distance          
                c += diff 
                number_obsticals += 1


        # Because the boids will first try to get away from the hoikes, 
        # we must first determine whether or not there are any hoikes nearby.
        if number_obsticals != 0:
            c = c //(number_obsticals)
            if c.length()!= 0: 
                c.scale_to_length(70)  

        elif number_hoiks != 0:
            c = c //(number_hoiks)
            if c.length()!= 0: 
                c.scale_to_length(50)   
        
        elif number_boids != 0:
            c = c //(number_boids)
            if c.length()!= 0: 
                c.scale_to_length(5)    

            c = (c - self.velocity)
        
        return c

    # Boids try to match velocity with nearby boids.
    # (source: http://www.kfish.org/boids/pseudocode.html)
        # Alignment
    def Alignment(self): 
        pv_j = Vector2()
        radius = 100
        number_boids = 0 

        for b in self.group: 
            distance = self.pos.distance_to(b.pos)
            if b != self and distance < radius: 
                pv_j += b.velocity        # Add the velocity to the vector 
                number_boids += 1 

        if number_boids != 0:
            pv_j = pv_j //(number_boids)
            if pv_j.length()!= 0: 
                pv_j.scale_to_length(5)  # Scale 

            pv_j = (pv_j - self.velocity)

        return pv_j 

    # Used to update the hokis in main. This needs to be done because the boids will not 
    # use the hoik list otherwise 
    def update_hoik_list(self, liste):
        self.listhawks = liste

    def update(self):
        self.acceleration *= 0  # Set the accerleration to 0 for every update to make sure the speed does not encrease more 

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

        # Call on the rules for the boids 
        v1 = self.Cohesion()
        v2 = self.Separation()
        v3 = self.Alignment()

        # Scale the vectors to prevent that they become too powerful 
        v1 *= 0.08
        v2 *= 0.1
        v3 *= 0.1

        self.acceleration += v1 + v2 + v3   # Add the vectors to the acceleration
        
        self.velocity += self.acceleration  # Add the acceleration to the velocity
        self.velocity.scale_to_length(7)    # Scale the velocity
        self.pos += self.velocity           # Add the velocity to the position to change the position 
        




