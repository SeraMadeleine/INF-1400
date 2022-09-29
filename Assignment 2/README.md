# Assignment 2

In this assignment you will create a simple simulator, more specifically a clone of the
classic flock simulator boids, originally written by Craig Reynolds in 1986. The implementation will be written in Python, using the pygame library, with a goal of using
the principles of object-oriented programming as best possible. That means you will
implement the game using classes, methods and inheritance.
2 Implementation

The simulator should simulate a moving flock consisting of boids operating by a set of
rules. The goal is to make the flock move in a lifelike manner, without hard-coding the
movement. Each boid has a set of adjacent boids, and should follow these rules:
1. Boids steer towards the average position of local flockmates.
2. Boids attempt to avoid crashing into other boids.
3. Boids steer towards the average heading of local flockmates.
The simulator should also include some additional features:
 Obstacles the boids need to avoid.
 Predators (hoiks) that will try to eat the boids.
The appearance of the simulator is up to you. The visual elements can be represented
by sprites (images) or by simple shapes like circles or rectangles. The number of boids
is also optional, however the size of the flock should allow it to split into several smaller
flocks.

## Requirements
1. Implement the simulator in accordance with object-oriented design, using
objects and classes.
2. Inheritance must be used to implement at least one class.
3. The simulator must follow the rules described above.
4. Hoiks and obstacles must be implemented.
5. The report must give a description of inheritance in object-oriented programming, and how you have chosen to use this feature.
6. The hand-in must include a class diagram (as shown in lectures) which
describes relations between the different classes.
