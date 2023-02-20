from settings import *
from Button import *

class admin:
    def __init__(self):
        self.win = display.get_surface()
        self.open = False
        self.setup()
    
    def setup(self):
        self.menu = button((375,150), 250, 50, (120,120,120), "Admin Menu", (0,0,0), 24)
        self.close = button((375,150), 250, 50, (120,120,120), "Close Menu", (0,0,0), 24)

    def draw(self):
        if self.open == False:
            if self.menu:
                self.open = True
        if self.open == True:
            if self.close:
                self.open = True
    
    def run(self):
        self.draw()