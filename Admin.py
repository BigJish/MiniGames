from settings import *
from Button import *

class admin:
    def __init__(self):
        self.win = display.get_surface()
        self.open = False
        self.keyTime = 0
        self.keyHeld = 1
        self.activate = False
        self.admin = False
        self.showHitboxes = False
        self.fireMenu = False
        self.speedMenu = False
        self.fireMod = 1
        self.speedMod = 1
        self.setup()
    
    def setup(self):
        self.button1 = button("Admin", 24, 100, 50, "open")
        self.buttons = [
            button("Close", 24, 100, 250, "close"),
            button("Hitbx", 24, 100, 200, "hitboxes"),
            button("Shoot", 24, 100, 150, "shoot"),
            button("Speed", 24, 100, 100, "speed"),
        ]
        self.shotButtons = [
            button("1x",24, 220, 150,"1f"),
            button("2x",24, 300, 150,"2f"),
            button("4x",24, 380, 150,"4f"),
            button("infinite",24, 535, 150,"infinite"),
            button("Close",24, 740, 150,"closeShot")
        ]

        self.speedButtons = [
            button("1x",24, 220, 100,"1s"),
            button("2x",24, 300, 100,"2s"),
            button("4x",24, 380, 100,"4s"),
            button("8x",24, 460, 100,"8s"),
            button("Close",24, 580, 100,"closeSpeed")
        ]
        self.closeHitbox = button("Hide", 24, 250, 200, "closeHitbox")
        

    def draw(self):
        if self.open == False:
            if self.button1.update() == "open":
                self.open = True
        if self.open == True:
            for i in self.buttons:
                val = i.update()
                if val == "close":
                    self.open = False
                if val == "hitboxes":
                    self.showHitboxes = True
                if val == "shoot":
                    self.fireMenu = True
                if val == "speed":
                    self.speedMenu = True

        if self.showHitboxes == True:
            if self.closeHitbox.update() == "closeHitbox":
                self.showHitboxes = False


        if self.fireMenu == True:
            for i in self.shotButtons:
                val = i.update()
                if val == "closeShot":
                    self.fireMenu = False
                if val == "infinite":
                    self.fireMod = 0
                if val == "1f":
                    self.fireMod = 1
                if val == "2f":
                    self.fireMod = 0.5
                if val == "4f":
                    self.fireMod = 0.25

        if self.speedMenu == True:
            for i in self.speedButtons:
                val = i.update()
                if val == "closeSpeed":
                    self.speedMenu = False
                if val == "1s":
                    self.speedMod = 1
                if val == "2s":
                    self.speedMod = 2
                if val == "4s":
                    self.speedMod = 4
                if val == "8s":
                    self.speedMod = 8
    
    def run(self):
        self.draw()
    
    def checkAdmin(self):
        k  = key.get_pressed()
        if self.admin == False:
            if k[K_LCTRL] and k[K_LSHIFT] and k[K_p]:
                self.activate = True
            else:
                self.activate = False
                self.keyTime = t()
                
            if self.activate == True:
                if k[K_RETURN]:
                    if t() - self.keyTime >= self.keyHeld:
                        self.admin = True

                else:
                    self.keyTime = t()
        
        else:
            if k[K_LCTRL] and k[K_LSHIFT] and k[K_q]:
                self.admin = False
                self.showHitboxes = False
                self.fireMod = 1
                self.speedMod = 1

        
        return [self.admin, self.showHitboxes, self.fireMod, self.speedMod]