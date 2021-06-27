import arcade
import math
import random

from abc import ABC, abstractmethod
from ship import Ships
from bullet import Bullets

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        #arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.example_image = arcade.load_texture("space_background.png")
        self.held_keys = set()
        
        self.asteroids = []

        #for i in range(INITIAL_ROCK_COUNT):
            #bigAst = LargeRock()
            #self.asteroids.append(bigAst)
            
        self.ship= Ships()
        
        self.bullets=[]
            
        # TODO: declare anything here you need the game class to track
   
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        # clear the screen to begin drawing
        arcade.start_render()

    
        for asteroid in self.asteroids:
            asteroid.draw()

        for bullet in self.bullets:
            bullet.draw()
         # TODO: draw each object    
        self.ship.draw()    
        #self.bullet.draw()
    def remove_notAliveObjects(self):
        for bullet in self.bullets:
            if not bullet.is_alive():
                self.bullets.remove(bullet)   

        for asteroid in self.asteroids:
            if not asteroid.is_alive():
                self.asteroids.remove(asteroid) 

    def check_collisions(self):
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if((bullet.alive) and (asteroid.alive)):
                    distance_x = abs(asteroid.center.x - bullet.center.x)
                    distance_y = abs(asteroid.center.y - bullet.center.y)
                    max_dist = asteroid.radius + bullet.radius
                    if((distance_x < max_dist) and (distance_y < max_dist)):
                        asteroid.break_apart(self.asteroids)
                        bullet.alive = False
                        asteroid.alive = False
                else:
                    self.destroy = True
                    print("METEOR DESTROY")
    
        for asteroid in self.asteroids:
            if((self.ship.alive) and (asteroid.alive)):
                distance_x = abs(asteroid.center.x - self.ship.center.x)
                distance_y = abs(asteroid.center.y - self.ship.center.y)
                max_dist = asteroid.radius + self.ship.radius
                if((distance_x < max_dist) and (distance_y < max_dist)):
                    self.ship.alive= False
                    asteroid.alive = False
            
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        for asteroid in self.asteroids:
            asteroid.advance()
       
        for bullet in self.bullets:
            bullet.advance()
            #bullet.alive()

        self.remove_notAliveObjects()
        self.check_collisions()

        
        self.ship.advance()
        #self.bullet.advance()
        
      

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()
            
        if arcade.key.UP in self.held_keys:
            self.ship.thrust(True)

        if arcade.key.DOWN in self.held_keys:
            self.ship.thrust(False)

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullets(self.ship.angle, self.ship.center.x, self.ship.center.y)
                self.bullets.append(bullet)
                bullet.fire()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()