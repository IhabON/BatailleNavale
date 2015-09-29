class Boat():
    def __init__(self, nom, taille):
       self.nom=nom
       self.taille=taille
       self.x=-1
       self.y=-1

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom=nom

    def getTaille(self):
        return self.taille

    def setTaille(self, taille):
        self.taille=taille

    def setCoordonees(self, x, y):
        self.x=x
        self.y=y

    def getCoordonnees(self):
        return [self.x, self.y]