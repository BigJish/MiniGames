from settings import *

class EnemySpawning:
    def  __init__(self):
        self.level = 1
        self.spawnDelay = 4
        self.spawned = 0

        self.spawnTime = t()
        self.levelSpawn = 4
        self.textTime = t()
        self.textDelay = 4

        self.text = text("Level "+str(self.level), 48, 500, 300, 1)
    
    def run(self):
        if t() - self.textTime <= self.textDelay:
            self.levelUpDisplay()

        else:
            return self.spawn()

    def levelUp(self):
        self.level += 1
        self.spawned = 0
        self.levelSpawn += 2
        self.spawnDelay = 16/self.levelSpawn
        self.textTime = t()
        self.spawnTime = t()

    def spawn(self):
        if t() - self.spawnTime >= self.spawnDelay:
            if self.levelSpawn > self.spawned:
                    self.spawned += 1
                    self.spawnTime = t()
                    return "spawn"
            else:
                self.levelUp()
            
    def levelUpDisplay(self):
        self.text.text_update("Level "+str(self.level))