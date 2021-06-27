import arcade
import math
import random
from abc import ABC, abstractmethod
from flyingobject import FlyingObjects
from constant import Constants

#from game.words_list import Words_list
#BULLET_RADIUS = 30
#BULLET_SPEED = 10
#BULLET_LIFE = 60

class Bullets(FlyingObjects):
    def __init__(self, angle, x, y):
        super().__init__("laserGreen.png")
        self.radius = Constants.BULLET_RADIUS
        self.life = Constants.BULLET_LIFE
        self.speed = Constants.BULLET_SPEED
        #self.angle= ship_angle
        #self.center.x= ship_xs
        #self.center.y= ship_y
        self.angle= angle-270
        self.center.x= x
        self.center.y= y
    
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle+270)) * Constants.BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle+270)) * Constants.BULLET_SPEED
    
    def advance(self):
        super().advance()
        self.life = self.life-1
        if (self.life <= 0):
            self.alive = False