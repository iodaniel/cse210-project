class lever:
    """
    Class used to control the movement of the spaceship.
    """    
    def __init__(self, x, y):
        
        self._x = x
        self._y = y

    def add(self, other):
        
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return lever(x, y)

    def equals(self, other):
        
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        
        return self._x

    def get_y(self):
        
        return self._y

    def reverse(self):
        
        x = self._x * -1
        y = self._y * -1
        return lever(x, y)