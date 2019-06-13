
from random import shuffle
from random import randrange
from math import cos, sin, sqrt, radians


class Hexagone:
    def __init__(self, x, y, size, coords, color, tags, ressource, number, outline):

        self.x = x           # top left x
        self.y = y           # top left y
        self.size = size     # size of a side
        self.selected = False
        self.tags = tags
        self.coords=coords
        self.color=color
        self.ressource=ressource
        self.number=number
        self.outline=outline


        #initialise les sommets
        start_x = self.x
        start_y = self.y
        angle = 60
        coords = []

        for i in range(6):
            end_x = start_x + self.size * cos(radians(angle * i))
            end_y = start_y + self.size * sin(radians(angle * i))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y

        self.sommet_1=(coords[0][0], coords[0][1])
        self.sommet_2=(coords[1][0], coords[1][1])
        self.sommet_3=(coords[2][0], coords[2][1])
        self.sommet_4=(coords[3][0], coords[3][1])
        self.sommet_5=(coords[4][0], coords[4][1])
        self.sommet_6=(coords[5][0], coords[5][1])
        

class Joueur:
    def __init__(self, couleur):

        self.couleur=couleur
        self.points=0
        self.Bois=0
        self.Blé=0
        self.Mouton=0
        self.Roche=0
        self.Argile=0
        self.Chevaliers=(0,0)
        self.Cartes_1_point=0
        self.Carte_construire_2_routes=0
        self.Carte_monopole=0
        self.Carte_invention=0


class Sommet:
    def __init__(self):
        self.joueur=None
        self.batiment=None

class Route:
    def __init__(self):
        self.joueur=None










        
