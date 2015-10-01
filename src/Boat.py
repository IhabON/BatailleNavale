class Boat():
    def __init__(self, nom, size, id):
       self.nom=nom
       self.size=size
       self.x=-1
       self.y=-1
       self.id=id
       self.touch=0
       self.down=False

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom=nom

    def getSize(self):
        return int(self.size)

    def setSize(self, size):
        self.size=size

    def setCoordonees(self, x, y):
        self.x=x
        self.y=y

    def getCoordonnees(self):
        return [self.x, self.y]
    
    def checkBoat(self,id):
    #Si le bateau est touché, on rend l'id négatif sur la grille
        self.id =id
        self.touch += 1
        if self.touch == self.size:
            self.down=True
            self.id = -id
            return True
        else:
            return False
