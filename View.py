
from random import shuffle
from random import randrange
from math import cos, sin, sqrt, radians
from tkinter import *
from Fonctions import *





class Plateau(Tk):

    def __init__(self, model):

        Tk.__init__(self)
        self.can = Canvas(self, width=1500, height=1000)
        self.can.pack(side=LEFT)
        self.model=model
        self.debug=True

        
        #Moment galère #######

        if self.model.Premier_Tour:
            
            label1=Label(self, text='Bienvenue au fantastique jeu du CATAN').place(x=1050,y=100)
            label2=Label(self, text="Combien de joueurs?").place(x=1050,y=200)
            self.can.Btn=Button(self, text='OK', command=get_Nbjoueur(NbJoueur)).place(x=1050,y=400)
            self.can.entry=Entry(self, textvariable=NbJoueur).place(x=1050,y=250)
            NbJoueur=
            
        #Fin du Moment galère #######

        if self.model.Premier_Tour:
            self.entry = tk.Entry(self).place(x=1050,y=250)
            self.button = tk.Button(self, text="Get", command=self.on_button)
            self.button.pack()
            self.entry.pack()

    def on_button(self):
        print(self.entry.get())

 






        self.draw_hex()


    def draw_hex(self):

        for hex in self.model.Cases_du_plateau.values():

            self.can.create_polygon(hex.sommet_1[0],
            							hex.sommet_1[1],
            							hex.sommet_2[0],
            							hex.sommet_2[1],
            							hex.sommet_3[0],
            							hex.sommet_3[1],
            							hex.sommet_4[0],
            							hex.sommet_4[1],
            							hex.sommet_5[0],
            							hex.sommet_5[1],
            							hex.sommet_6[0],
            							hex.sommet_6[1],
                                        fill=hex.color,
                                        outline=hex.outline,
                                        tags=hex.tags)
     
            if hex.number!=None and hex.number!=7:
                taille_carre=21
                x0=hex.x+taille_carre
                y0=hex.y+(sqrt(3)/2)*hex.size+taille_carre
                x1=hex.x+hex.size-taille_carre
                y1=hex.y+(sqrt(3)/2)*hex.size-taille_carre
                self.can.create_oval(x0,y0,x1,y1,fill='White')
                self.can.create_text((x0+x1)/2, (y0+y1)/2, text=hex.number)

            if self.debug :
                
                coords = "{}, {}".format(hex.coords[0], hex.coords[1])
                self.can.create_text((hex.size/2) + hex.sommet_1[0],
                                    (hex.size/2) + hex.sommet_1[1], 
                                   	 text=coords)



    def rafraichir(self, model):
        self.model=model
        return


    













 


   




    
#----------------------------------------------------------------------------------------

    
    




































