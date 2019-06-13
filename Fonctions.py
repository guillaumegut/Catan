from random import randrange
from math import sqrt

#valeur absolue
def abs (x):
    if x<0:
        return -x
    else: 
        return x

#Retourne faux s'il existe dans sommets un sommets quasiment identique à sommet
def not_in_keys_sommet(sommet, sommets):
    for i in sommets.keys():
        if abs(sommet[0]-i[0]) < 10 and abs(sommet[1]-i[1]) < 10:
            return False
    return True

def not_in_keys_route(route, routes):
	for i in routes.keys():
		if (abs(route[0][0]-i[0][0]) < 10 and abs(route[0][1]-i[0][1]) < 10 and abs(route[1][0]-i[1][0]) < 10 and abs(route[1][1]-i[1][1]) < 10) or (abs(route[1][0]-i[0][0]) < 10 and abs(route[1][1]-i[0][1]) < 10 and abs(route[0][0]-i[1][0]) < 10 and abs(route[0][1]-i[1][1]) < 10):
			return False
	return True


def Roll_dices():
    dice1=randrange(1,7)
    dice2=randrange(1,7)
    return dice1+dice2


def placer_colonie(Plateau, coord):
    Plateau.Sommets[coord].batiment='Colonie'
    Plateau.Sommets[coord].Joueur=Plateau.Joueur_en_cours
    if Plateau.Premier_Tour==False:
        Plateau.Joueur_en_cours.Bois-=1
        Plateau.Joueur_en_cours.Blé-=1
        Plateau.Joueur_en_cours.Argile-=1
        Plateau.Joueur_en_cours.Monton-=1


def placer_ville(Plateau, coord):
    Plateau.Sommets[coord].batiment='Ville'
    Plateau.Sommets[coord].Joueur=Plateau.Joueur_en_cours
    if Plateau.Premier_Tour==False:
        Plateau.Joueur_en_cours.Blé-=2
        Plateau.Joueur_en_cours.Roche-=3
        
def placer_route(Plateau, coord):
    Plateau.Routes[coord].Joueur=Plateau.Joueur_en_cours
    if Plateau.Premier_Tour==False:
        Plateau.Joueur_en_cours.Bois-=1
        Plateau.Joueur_en_cours.Argile-=1


def fct_Premier_Tour(Plateau):
    dices_results={}
    for i in range(Plateau.Nbrjoueur):
        #attendre lancer de dé joueur 
        lancer=Roll_dices()
        while lancer in dices_results.keys():
            lancer=Roll_dices()
        dices_results[lancer]=Plateau.Joueurs[i]

    print (dices_results)
    sorted_results=sorted(dices_results,reverse=True)+sorted(dices_results)
    print (sorted_results)

    ordre=[]
    for result in sorted_results:
        cpt=0
        for cle in dices_results.keys():
            if cle==result:
                if cpt==0:
                    ordre+=[dices_results[cle]]
                    cpt=1
    print (ordre)
    #Plateau.can.create_text(200,200,text='salut')

    
    for player in ordre:
        Plateau.can.bind("<Button>", lambda event : trouver_sommet(event, Plateau))

        




def get_Nbjoueur(NbJoueur):
    Nb_Joueur=NbJoueur.get()
    print (Nb_Joueur)
    return







def trouver_case (self, event):
    x, y = event.x, event.y
    for hex in self.hexagons:
        if hex.sommet_1[0]<x<hex.sommet_2[0] and hex.sommet_1[1]<y<hex.sommet_5[1]:
            print(hex.coords)
            return hex.coords




def trouver_sommet (event,Plateau):
    x, y = event.x, event.y
    size = (1/2) * 85 * sqrt(3) / 2
    for sommet in Plateau.sommets:
        if sommet[0]-size < x < sommet[0]+size and sommet[1]-size < y < sommet[1]+size:
            print (sommet)
            return sommet



        
