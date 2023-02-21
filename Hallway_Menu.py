from pygame import *
from Button import *

class menu:
    def __init__(self):
        self.screen = display.get_surface()
        self.b1 = button("Resume", 24, 500, 150)
        self.b2 = button("Logout", 24, 500, 300)
        self.b3 = button(" Quit ", 24, 500, 450)
        
    def draw(self):
        if  self.b1.update() == True:
            return 1
        elif  self.b2.update() == True:
            return 2
        elif  self.b3.update() == True:
            return 3
        