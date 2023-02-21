from settings import *
from player import Player
from Background import bg
from portal import Portal
from Player_Name import player_name
from Hallway_Menu import *
from TextFile import *

class Hallway:
    def __init__(self,user):
        self.visible_sprites = Camera()
        self.obsticle_sprites = sprite.Group()
        self.screen = display.get_surface()
        self.user = user
        self.screen_num = 1
        self.menu = menu()
        self.textFile = database(user)
        self.star_img = image.load('Star.png').convert_alpha()
        self.setup(user)
    
    def setup(self, user):
        self.bg = bg((0,-200), [self.visible_sprites])
        self.portals = [Portal((930,0), [self.visible_sprites,self.obsticle_sprites], user,"Game1"),
                        Portal((1130,0), [self.visible_sprites, self.obsticle_sprites], user,"Game2"),
                        Portal((1330,0), [self.visible_sprites, self.obsticle_sprites], user,"Game3"),
                        Portal((1530,0), [self.visible_sprites, self.obsticle_sprites], user,"Game4"),
        ]
        self.player = Player((200,200), self.visible_sprites, self.obsticle_sprites, user)
        self.playername = player_name((500,220), self.visible_sprites, user)
        self.text = text("= "+str(self.textFile.get_stars()), 24, 120, 20, 0)
                
    def run(self):
        if self.screen_num == 1:
            k = key.get_pressed()
            if k[K_ESCAPE]:
                self.screen_num = 2
            
            self.screen.fill((60,0,120))
            
            self.visible_sprites.custom_draw(self.player)
            self.x = 0
            x = 0
            for i in self.portals:
                x+=1
                if i.enter(self.player) == True:
                    self.x = x
                    
            self.visible_sprites.update()
            self.playername.update()
            
            self.screen.blit(self.star_img, (50,15))
            self.text.text_update("= "+str(self.textFile.get_stars()))
            
        elif self.screen_num == 2:
            if self.menu.draw() == 1:
                self.screen_num = 1
            if self.menu.draw() == 2:
                return "logout"
            if self.menu.draw() == 3:
                quit()
            
    def minigame(self):
        if self.x == 1:
            return 1
        if self.x == 2:
            return 2
        if self.x == 3:
            return 3
        if self.x == 4:
            return 4
        

class Camera(sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = display.get_surface()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)