import random
import math
from asteroid import Asteroids
from constant import Constants
from mediumAsteroid import MediumAsteroids
from smallAsteroid import SmallAsteroids

class BigAsteroids(Asteroids):
    def __init__(self):
        super().__init__("meteor_big1.png")
        #"images/meteorGrey_big1.png"
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.speed= Constants.BIG_ROCK_SPEED
        self.velocity.dx= math.cos(math.radians(self.direction))* self.speed
        self.velocity.dy= math.sin(math.radians(self.direction))* self.speed
        self.radius = Constants.BIG_ROCK_RADIUS

    def advance(self):
        super().advance()
        self.angle += Constants.BIG_ROCK_SPIN

    def break_apart(self, asteroids):
        med1 = MediumAsteroids()
        med1.center.x = self.center.x
        med1.center.y = self.center.y 
        med1.velocity.dy = self.velocity.dy + 2
         
        med2 = MediumAsteroids()
        med2.center.x = self.center.x
        med2.center.y = self.center.y 
        med2.velocity.dy = self.velocity.dy - 2
        
        small = SmallAsteroids()
        small.center.x = self.center.x
        small.center.y = self.center.y 
        small.velocity.dy = self.velocity.dy + 5

        asteroids.append(med1)
        asteroids.append(med2)
        asteroids.append(small)
        self.alive= False