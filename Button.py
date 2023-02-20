from settings import *

class button:
    def __init__(self, txt, fontSize, x, y):
        self.screen = display.get_surface()
        self.buttonText = text(txt, fontSize, x, y, 1)
        self.rect = Rect(x, y, self.buttonText.get_text_width()+fontSize, self.buttonText.get_text_height()+fontSize)

    def draw(self):
        draw.rect(self.screen, self.bg_colour, self.rect)
        self.buttonText.draw()
    
    def collide(self):
        mpos = mouse.get_pos()
        if self.rect.collidepoint(mpos[0],mpos[1]):
            self.text_colour = (120,120,120)
            self.bg_colour = (0,0,0)
            if mouse.get_pressed()[0]:
                return True
        else :
            self.text_colour = (0,0,0)
            self.bg_colour = (120,120,120)
    
    def update(self):
        if self.collide() == True:
            return True
        self.draw()
        