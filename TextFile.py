from settings import *

class database:
    def __init__(self, user):
        self.user = user
        self.games = ["Game1","Game2","Game3","Game4"]
    
    def read(self):
        f = open("Users.txt","r")
        file = json.load(f)
        f.close()
        return file
    
    def write(self, file):
        f = open("Users.txt","w")
        json.dump(file, f)
        f.close()
    
    def get_game_data(self, type):
        data = []
        file = self.read()
        for i in self.games:
            data.append(file[self.user][2]["Games"][i][type])
        return data

    def get_stars(self):
        file = self.read()
        stars = (file[self.user][1]["Total Stars"])
        return stars