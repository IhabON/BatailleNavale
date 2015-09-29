from src import Boat

class Grid():
    def __init__(self):
        self.grid = [["0"]*10 for _ in range(10)]

    #Fonction permettant de verifier et de placer un bateau si place dispo
    def setBoat(self, boat, direction):
        empty = True
        x=boat.getCoordonnees()[0]
        y=boat.getCoordonnees()[1]
        #Verification de la disponibilité des cases
        for i in range(0,boat.getTaille()):
            if direction == "N":
                empty = self.checkEmpty(x, y-i)
            elif direction == "S":
                empty = self.checkEmpty(x, y+i)
            elif direction == "E":
                empty = self.checkEmpty(x+i, y)
            elif direction == "W":
                empty = self.checkEmpty(x-i, y)
        #Si case dispo -> remplissage
        if empty == True:
            for i in range(0,boat.getTaille()):
                if direction == "N":
                    self.grid[x][y-i] = boat.id
                elif direction == "S":
                    self.grid[x][y+i] = boat.id
                elif direction == "E":
                    self.grid[x+i][y] = boat.id
                elif direction == "W":
                    self.grid[x-i][y-i] = boat.id
            return True
        #Si case non dispo -> return False
        else:
            return False

    #Verifie la disponibilité d'une case et son existence
    def checkEmpty(self, x, y):
        if 0<=x<=10 & 0<=y<=10:
            if self.grid[x][y] == 0:
                return True
            else:
                return False
    #Fonction d'affichage
    def display(self):
        print("|---------------|")
        for j in range(0,10):
            ligne="|-"
            for i in range(0,10):
                ligne += str(self.grid[i][j])+"-"
            print(ligne+"|")
        print("|---------------|")