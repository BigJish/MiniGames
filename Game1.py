from settings import *

from Game1_Title import *
from Game1_Game_Over import *

from PlayerPlane import *
from rocket import *

from EnemyPlane import *
from Enemy_Rocket import *
from Game1_Spawning_Algorithm import *

from Boom import *

class Aerial:
    def __init__(self, user):
        self.screen = display.get_surface()
        
        self.visible_sprites = sprite.Group()
        self.enemy_sprites = sprite.Group()
        self.rocket_sprites = sprite.Group()
        self.obstcale_sprites = sprite.Group()
        self.enemy_rocket_sprites = sprite.Group()
        
        self.bg_img = image.load('Game1_bg.jpg').convert_alpha()
        self.user = user
        
        self.collisions = []
        self.explosions = []

        self.title = game1_title(user)
        
        self.score = 0
        self.rocket_cooldown = 99999
        self.enemy_cooldown = 0
        self.difficulty_factor = 0.95
        self.cooldown = 2
        self.dead = False
        self.key_held = False
        self.scrn_num = 1
        
        self.text = text(str(self.score), 64, 500, 100, 1)

        self.setup()
        
    def setup(self):
        self.player = Player((200,300),self.visible_sprites)
        self.spawn = EnemySpawning()
    
    def run(self):
        if self.scrn_num == 1:
            if self.title.run() == True:
                self.scrn_num = 2
            
        if self.scrn_num == 2:
            if self.dead == False:
                self.screen.blit(self.bg_img,(0,0))
                self.text.text_update(""+str(self.score))

                val = self.spawn.spawn()
                if val == "spawn":
                    Enemy([self.visible_sprites, self.enemy_sprites, self.obstcale_sprites], self.rocket_sprites)


                if self.player.shoot() == True:
                    if self.key_held == False:
                        if t() - self.rocket_cooldown >= 0.5:
                            self.rocket_cooldown = t()
                            self.key_held = True
                            Rocket(self.player.rect.center, [self.visible_sprites, self.rocket_sprites, self.obstcale_sprites], self.enemy_sprites)
               
                for i in self.enemy_sprites:
                    if i.shoot() == True:
                        enemy_rocket((i.rect.x, i.rect.y+25), [self.visible_sprites, self.enemy_rocket_sprites])
                    
                # if t() - self.enemy_cooldown >= self.cooldown:
                #     self.enemy_cooldown = t()
                #     self.cooldown *= self.difficulty_factor
                #     Enemy([self.visible_sprites, self.enemy_sprites, self.obstcale_sprites], self.rocket_sprites)
                    
                
                for i in self.obstcale_sprites:
                    if i.hit() == True:
                        self.visible_sprites.remove(i)
                        self.obstcale_sprites.remove(i)
                        self.collisions.append(i)
                        
                        
                for i in self.collisions:
                    for j in self.enemy_sprites:
                        if j == i:
                            self.enemy_sprites.remove(i)
                            self.score += 1
                            self.explosions.append(Pow(i.rect.center, self.visible_sprites))
                    for j in self.rocket_sprites:
                        if j == i:
                            self.rocket_sprites.remove(i)
                            
                            
                for i in self.rocket_sprites:
                    if i.off_screen() == True:
                        self.visible_sprites.remove(i)
                        self.obstcale_sprites.remove(i)
                        self.rocket_sprites.remove(i)
                
                for i in self.explosions:
                    if i.timer() == True:
                        self.visible_sprites.remove(i)
                        
                for i in self.enemy_rocket_sprites:
                    if i.collide(self.player) == True:
                        self.visible_sprites.remove(self.player)
                        self.explosions.append(Pow(self.player.rect.center, self.visible_sprites))
                        self.GameOver = game_over(self.score)
                        self.dead = True
                        
                for i in self.visible_sprites:
                    i.update()

                if self.player.shoot() == False:
                    self.key_held = False
                    
            if self.dead == True:
                val = self.GameOver.display(self.user)

                if val == "retry":
                    return "reset"
                    
                if val == "leave":
                    return "exit"