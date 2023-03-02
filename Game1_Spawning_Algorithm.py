from settings import *

class EnemySpawning:
    def  __init__(self):
        self.level = 1
        self.spawnDelay = 4
        self.spawned = 0

        self.spawnTime = t()
        self.levelSpawn = 5
        self.textTime = t()
        self.textDelay = 4

        self.text = text("", 48, 500, 300, 1)
    
    def run(self):
        if t() - self.textTime >= self.textDelay:
            self.levelUpDisplay()

        return self.spawn()

    def levelUp(self):
        self.level += 1
        self.spawned = 0
        self.levelSpawn = self.level*5
        self.spawnTime = self.levelSpawn/20

    def spawn(self):
        if self.levelSpawn >= self.spawned:
            if t() - self.spawnTime >= self.spawnDelay:
                self.spawned += 1
                self.spawnTime = t()
                return "spawn"
            
    def levelUpDisplay(self):
        self.text.text_update("Level "+str(self.level))