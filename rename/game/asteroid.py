from flyingobject import FlyingObjects

class Asteroid(FlyingObjects):
    """ 
    we have three sizes of asteroids this class helps to get the intial type.
    """
    def __init__(self, img):
        super().__init__(img)
        self.radius =0.0