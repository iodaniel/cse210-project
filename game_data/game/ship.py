
import math
from constant import Constants
from flyingobject import FlyingObjects


class Ships(FlyingObjects):
    def __init__(self):
        super().__init__("alienShip.png")
        self.angle = 1
        self.center.x = (Constants.SCREEN_WIDTH/2)
        self.center.y = (Constants.SCREEN_HEIGHT/2)
        self.radius = Constants.SHIP_RADIUS
    
    def left(self):
        self.angle += Constants.SHIP_TURN_AMOUNT
    
    def right(self):
        self.angle -= Constants.SHIP_TURN_AMOUNT
    
    def thrust(self, isUp):
        if (not isUp):
            self.velocity.dx += math.sin(math.radians(self.angle)) * Constants.SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.cos(math.radians(self.angle)) * Constants.SHIP_THRUST_AMOUNT
        else:
            self.velocity.dx -= math.sin(math.radians(self.angle)) * Constants.SHIP_THRUST_AMOUNT
            self.velocity.dy += math.cos(math.radians(self.angle)) * Constants.SHIP_THRUST_AMOUNT