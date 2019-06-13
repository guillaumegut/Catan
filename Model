
from random import shuffle
from random import randrange
from Objets import *
from Fonctions import *
from math import cos, sin, sqrt, radians


class Plateau:

    def __init__(self, Nbjoueur):

        self.Premier_Tour=True
        self.Jeu_en_cours=True
        self.hexagons = {}
        self.Cases_du_plateau={}
        self.sommets = {}
        self.routes = {}
        self.Joueurs= []
        self.Joueur_en_cours=None

        #Initialise les joueurs
        Joueur_1=Joueur('Bleu')
        Joueur_2=Joueur('Rouge')
        Joueur_3=Joueur('Vert')
        Joueur_4=Joueur('Blanc')
        tab_joueurs=[Joueur_1, Joueur_2, Joueur_3, Joueur_4]

        self.Nbjoueur=Nbjoueur

        for i in range(self.Nbjoueur):
            self.Joueurs+=[tab_joueurs[i]]

        #Joueur en cours   
        self.tour=0
        self.Joueur_en_cours=self.Joueurs[self.tour%self.Nbjoueur]

        
        self.initGrid(7, 7, 85)


    def initGrid(self, cols, rows, size):

        decalage_haut=120
        décalage_gauche=40

        Ressources = ['Bois','Bois','Bois','Bois', 'Blé', 'Blé', 'Blé', 'Blé', 'Mouton','Mouton',
                    'Mouton','Mouton', 'Roche','Roche','Roche','Argile','Argile','Argile']
        Numbers=[2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        colors={'Bois': 'forest green','Blé': 'gold','Mouton': 'lawn green','Argile': 'tomato3','Roche': 'gray76','Desert': 'khaki1'}
        shuffle(Ressources)
        shuffle(Numbers)
        

        Cases_du_plateau =((1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4),(2,5),
        (3,1),(3,2),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4),(4,5),(5,3))

        cpt=0
        color='Skyblue1'
        outline='Skyblue1'
        number=None
        ressource=None
        hex_desert=randrange(19)


        for c in range(cols):
            if c % 2 == 0:
                offset = size * sqrt(3) / 2
            else:
                offset = 0
            for r in range(rows):

                if (r,c) in Cases_du_plateau:
                    
                    if cpt==hex_desert:
                        number=7
                        ressource='Desert'
                        color=colors[ressource]
                        outline='gray'
                        hex_desert=None

                    else:
                        number=Numbers[cpt]
                        ressource=Ressources[cpt]
                        color=colors[ressource]
                        outline='gray'
                        cpt+=1
                
                h = Hexagone(c * (size * 1.5) - décalage_gauche,
                            (r * (size * sqrt(3))) + offset - decalage_haut,
                            size,
                            (r,c),
                            color,
                            "{}.{}".format(r, c),
                            ressource,
                            number,
                            outline)

                self.Cases_du_plateau[(r,c)]=h

                color='Skyblue1'
                outline='Skyblue1'
                number=None
                ressource=None

                if (r,c) in Cases_du_plateau:
                    self.hexagons[(r,c)]=h

                if h.coords in Cases_du_plateau:

                    if not_in_keys_sommet(h.sommet_1, self.sommets):
                        self.sommets[h.sommet_1]=Sommet()
                    if not_in_keys_sommet(h.sommet_2, self.sommets):
                        self.sommets[h.sommet_2]=Sommet()
                    if not_in_keys_sommet(h.sommet_3, self.sommets):
                        self.sommets[h.sommet_3]=Sommet()
                    if not_in_keys_sommet(h.sommet_4, self.sommets):
                        self.sommets[h.sommet_4]=Sommet()
                    if not_in_keys_sommet(h.sommet_5, self.sommets):
                        self.sommets[h.sommet_5]=Sommet()
                    if not_in_keys_sommet(h.sommet_6, self.sommets):
                        self.sommets[h.sommet_6]=Sommet()

                    if not_in_keys_route((h.sommet_1, h.sommet_2), self.routes):
                        self.routes[(h.sommet_1, h.sommet_2)]=Route()
                    if not_in_keys_route((h.sommet_2, h.sommet_3), self.routes):
                        self.routes[(h.sommet_2, h.sommet_3)]=Route()
                    if not_in_keys_route((h.sommet_3, h.sommet_4), self.routes):
                        self.routes[(h.sommet_3, h.sommet_4)]=Route()
                    if not_in_keys_route((h.sommet_4, h.sommet_5), self.routes):
                        self.routes[(h.sommet_4, h.sommet_5)]=Route()
                    if not_in_keys_route((h.sommet_5, h.sommet_6), self.routes):
                        self.routes[(h.sommet_5, h.sommet_6)]=Route()
                    if not_in_keys_route((h.sommet_6, h.sommet_1), self.routes):
                        self.routes[(h.sommet_6, h.sommet_1)]=Route()


    def jouer(self):
        a=int(input())
        return
   
'''
    for joueur in ordre:
        Plateau.Joueur_en_cours=joueur
        print ('où placer votre colonie?')
        coord=make_coord_sommet()
        placer_colonie(Plateau, coord)
        print('où placer votre route?')
        coord=make_coord_route()
        placer_route(Plateau, coord)
        print(Plateau.Routes[coord].Joueur)

    Plateau.Premier_Tour=False
'''

#while True:
    #Board=Plateau()
    #if Board.Premier_Tour==True:
        #Premier_Tour(Board)

    
#----------------------------------------------------------------------------------------





































