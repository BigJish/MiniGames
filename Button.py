from settings import *

class button:
    def __init__(self, displayText, fontSize, x, y, buttonVal):
        self.win = display.get_surface()
        self.buttonText = text(displayText, fontSize, x, y, 1)
        w = self.buttonText.get_text_width()+fontSize
        h = self.buttonText.get_text_height()+fontSize
        self.rect = Rect(x-(w//2), y-(h//2), w, h)
        self.buttonVal = buttonVal

    def draw(self):
        draw.rect(self.win, self.bg_colour, self.rect)
        self.buttonText.draw()
    
    def collide(self):
        mpos = mouse.get_pos()
        if self.rect.collidepoint(mpos[0],mpos[1]):
            self.bg_colour = (80,80,80)
            if mouse.get_pressed()[0]:
                return True
        else :
            self.bg_colour = (180,180,180)
    
    def update(self):
        val = self.collide()
        self.draw()
        if val == True:
            return self.buttonVal
        else:
            return False
        
        