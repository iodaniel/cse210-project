




'''

import sys
from game.lever import lever
from asciimatics.event import KeyboardEvent

class InputService:
    # this is the player's lever

    def __init__(self, screen):
        #The keys that we will use

        self._screen = screen
        self._keys = {}
        self._keys[119] = lever(0, -1) # go up
        self._keys[115] = lever(0, 1) # go down
        self._keys[97] = lever(-1, 0) # move left
        self._keys[100] = lever(1, 0) # move right
        self._current = lever(1, 0)
        
    def get_direction(self):

        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            self._current = self._keys.get(event.key_code, self._current)
        return self._current
'''