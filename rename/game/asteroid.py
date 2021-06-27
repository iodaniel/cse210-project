
from flyingobject import FlyingObjects


class Asteroid(FlyingObjects):
    def __init__(self, img):
        super().__init__(img)
        self.radius =0.0