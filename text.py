from pygame import *
init()

class text:
    def __init__(self, displayText, textSize, x, y, displayType):
        self.win = display.get_surface()

        textFont = font.Font("PressStart2P-Regular.ttf",textSize)
        self.text = textFont.render(displayText, True, (0,0,0))
        self.x = x
        self.y = y
        self.type = displayType

        self.pos_config()
    
    def draw(self):
        self.win.blit(self.text,(self.x, self.y))

    def pos_config(self):
        if self.type == 1:
            self.x = self.x - self.text.get_width() // 2
            self.y = self.y - self.text.get_height() // 2

    def get_text_width(self):
        return self.text.get_width()
        
    def get_text_height(self):
        return self.text.get_height()