import arcade
import math
import random
from abc import ABC, abstractmethod

from point import Point
from velocity import Velocity
#from constant import Constants
#from rename.game.constant import Constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
SHIP_RADIUS = 30

class FlyingObjects(ABC):
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = SHIP_RADIUS
        self.angle = 0
        self.speed = 0
        self.direction = 1
        #self.alpha = 255
        
    def advance(self):
        self.wrap()
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx

    def wrap(self):
        if self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
        if self.center.x < 0:
            self.center.x += SCREEN_WIDTH
        if self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
        if self.center.y < 0:
            self.center.y += SCREEN_HEIGHT

    
    def is_alive(self):
        return self.alive
    
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture,
                                      self.angle, 255)