import sys
from game import constant
from asciimatics.widgets import Frame

class OutputService:
    # This is what the game shall show, we are using asciimatics because we don't have images yet.

    def __init__(self, screen):
        
        self._screen = screen
        
    def clear_screen(self): #
         
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constant.limit_left_right_movemment, 0, 0, 7)
        self._screen.print_at("-" * constant.limit_left_right_movemment, 0, constant.limit_left_right_movemment, 7)
        
    def draw_player(self, player):

        text = player.get_text()
        position = player.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7)

    def draw_actors(self, player):
        
        for i in player:
            self.draw_actor(player)
    
    def flush_buffer(self):
        
        self._screen.refresh()    
