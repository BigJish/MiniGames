from pygame import *
from Button import *

class menu:
    def __init__(self):
        self.screen = display.get_surface()
        self.buttons = [
            button("Resume", 24, 500, 150, 1),
            button("Logout", 24, 500, 300, 2),
            button(" Quit ", 24, 500, 450, 3)
        ]
        
    def draw(self):
        for i in self.buttons:
            val = i.update()
            if val != False:
                return val
        