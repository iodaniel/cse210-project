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
    """
    In this class we created the super class that controls the aim and shotting of the spaceship

    """
    def __init__(self, angle, x, y):
        """
        Using the constants we manage the bullet radius, life, speed, shape and color of the laser, importing
        the corresponding image to it
        
        """
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
        """
        this function manage the aim and the speed's rotation of the ship
        """
        self.velocity.dx -= math.sin(math.radians(self.angle+270)) * Constants.BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle+270)) * Constants.BULLET_SPEED
    
    def advance(self):
        """
        this function helps to count the losses lifes in the game
        """
        super().advance()
        self.life = self.life-1
        if (self.life <= 0):
            self.alive = False