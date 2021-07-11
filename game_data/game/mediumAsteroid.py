
import random
import math
from asteroid import Asteroids
from constant import Constants
from smallAsteroid import SmallAsteroids


class MediumAsteroids(Asteroids):
    def __init__(self):
        super().__init__("meteor_med1.png")
        self.radius = Constants.MEDIUM_ROCK_RADIUS
        self.speed= Constants.BIG_ROCK_SPEED
        self.velocity.dx= math.cos(math.radians(self.direction))* self.speed
        self.velocity.dy= math.sin(math.radians(self.direction))* self.speed

    def advance(self):
        super().advance()
        self.angle += Constants.MEDIUM_ROCK_SPIN

    def break_apart(self, asteroids):
        small = SmallAsteroids()
        small.center.x = self.center.x
        small.center.y = self.center.y 
        small.velocity.dy = self.velocity.dy + 1.5
        small.velocity.dx = self.velocity.dx + 1.5

        small2 = SmallAsteroids()
        small2.center.x = self.center.x
        small2.center.y = self.center.y 
        small2.velocity.dy = self.velocity.dy - 1.5
        small2.velocity.dx = self.velocity.dx - 1.5
       
        asteroids.append(small)
        asteroids.append(small2)
        self.alive = False