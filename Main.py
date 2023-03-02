from login_tk import *
from pygame import *
from settings import *
from Title import *
from Game1 import *
from Game3 import *
from Game2 import *
from Game4 import *
from hallway import *
from Admin import *


class Game:
    def __init__(self):
        # self.user = TkRun()
        self.user = "Josh"
        self.end = True
        if self.user != "":
            init()
            self.screen  = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            # self.win  = display.set_mode((0, 0), RESIZABLE)
            self.clock = time.Clock()

            self.end = False
            self.logout = False
            self.screen = 3

            self.title = Title_Screen(self.user)
            self.hallway = Hallway(self.user)
            self.game1 = Aerial(self.user)
            self.game2 = Platformer()
            self.game3 = Maze()
            self.game4 = game4()
            self.admin = admin()

            self.run()

    def run(self):
        while self.end == False:   
            for e in event.get():
                if e.type == QUIT:
                    self.end = True
            
            admin = self.admin.checkAdmin()
            
            if self.screen == 1:
                if self.title.run() == True:
                    self.screen = 2
            
            elif self.screen == 2:
                val = self.hallway.run()

                if val == "logout":
                    self.end = True
                    self.logout = True

                if self.hallway.minigame() == 1:
                    self.screen = 3
                    
                if self.hallway.minigame() == 2:
                    self.screen = 4
                    
                if self.hallway.minigame() == 3:
                    self.screen = 5
                    
                if self.hallway.minigame() == 4:
                    self.screen = 6
            
            elif self.screen == 3:
                val = self.game1.run(admin)

                if val == "exit":
                    self.game1 = Aerial(self.user)
                    self.screen = 2


                if val== "reset":
                     self.game1 = Aerial(self.user)
                     
            elif self.screen == 4:
                val = self.game2.run(self.user)
                
                if  val == "exit":
                    self.game2 = Platformer()
                    self.screen = 2

                if val == "reset":
                    self.game2 = Platformer()
                    
            elif self.screen == 5:
                if self.game3.run() == True:
                    self.screen = 2
                    
            elif self.screen == 6:
                if self.game4.run() == True:
                    self.screen = 2
            
            if admin[0] == True:
                self.admin.run()
                
            self.clock.tick(FPS)
            display.flip()
        
        quit()
        if self.logout == True:
            game = Game()
            game.run()

if __name__ == '__main__':
    game = Game()