from settings import *
from TextFile import *

class game1_title:
    def __init__(self, user):
        self.screen = display.get_surface()
        self.bg_img = image.load('Game1_bg.jpg').convert_alpha()
        self.textFile = database(user)
        self.text = [
            text("Sky Raiders!", 64, 500, 180, 1),
            text("Your highscore is "+str(self.textFile.get_game_data("Highscore")), 64, 500, 300, 1),
            text("Press enter to start", 36, 500, 420, 1)
        ]
        
    def run(self):
        self.screen.blit(self.bg_img,(0,0))
        for i in self.text:
            i.draw()
        k = key.get_pressed()
        if k[K_RETURN]:
            return True