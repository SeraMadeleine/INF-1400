# Asignment 1

In this assignment you will create a simple game, more specifically a clone of the classic
game Breakout. The game will be written in Python, using the pygame library, with
a goal of using the principles of object-oriented programming as best possible. That
means you will implement the game using classes and methods.
2 Implementation

Your game must support the basic mechanics of the original game. In Breakout, the
player controls a platform at the bottom of the screen, and attempts to hit a ball. On
the top half of the screen there is a set of bricks. When the ball hits the bricks they
disappear. The game is won by removing all the bricks on the screen. If the player
misses the ball so it disappears below the screen, the game is lost.
It is important that the ball bounces off the platform with an angle dependant on where
it hits the platform, so the player can control the ball. To implement this it may help
to think of the platform as a semicircle, you may also draw the platform as a semicircle.
The look of the game is up to you, you can use the built-in functions in pygame for
drawing rectangles and circles of different colors, or import images for a more pleasing
aesthetic.

### Required elements in the implementation
1. Implement the game in accordance with object-oriented design, use objects and classes.
2. The platform should be controlled by the mouse or keyboard.
3. The ball should bounce in a different direction based on where on the
platform it hits.
4. A brick disappears when the ball hits it.
5. The ball bounces off the wall and ceiling, angle in = angle out.
5. The game is won when all bricks are removed, the game is lost when the
ball hits the bottom of the screen.
6. Well structured and commented code.
