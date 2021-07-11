from asteroid import Asteroids
from constant import Constants



class SmallAsteroids(Asteroids):
    def __init__(self):
        super().__init__("meteor_small1.png")
        self.speed = Constants.BIG_ROCK_SPEED 
        self.radius = Constants.SMALL_ROCK_RADIUS
    
    def advance(self):
        super().advance()
        self.angle += Constants.SMALL_ROCK_SPIN

    def break_apart(self, asteroids):
        self.alive = False