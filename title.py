from pygame import *
from Text import *
from sprite_sheet import*



class Title_Screen:
    def __init__(self, user):
        self.visible_sprites = sprite.Group()
        self.screen = display.get_surface()
        self.next_page = False

        bg = image.load("Title_bg.jpg").convert_alpha()
        bg = SpriteSheet(bg)
        self.bg = bg.get_image(0, 1000, 600, 1, (0, 0, 0))

        self.text = [
            text("Welcome!", 72, 500, 180, 1),
            text(user, 56, 500, 300, 1),
            text("Press Enter To Start", 32, 500, 400, 1)
        ]
        
    def run(self):
        if self.next_page == True:
            return True
        else:
            self.display()
        
    def display(self):
        k = key.get_pressed()
        if k[K_RETURN]:
            self.next_page = True
        self.screen.fill((100,150,255))
        self.screen.blit(self.bg, (0,0))

        for i in self.text:
            i.draw()     