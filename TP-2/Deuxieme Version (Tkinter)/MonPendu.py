# -*- coding: utf-8 -*-
"""

@author: Adrien COVAREL
Le but de ce code sera de faire une interface graphique pour notre jeu du pendu, je me suis donc 
inspiré de mon code terminé de la dernière séance, je l'ai adapté en créant des fentres, boutons...

Etat, pour l'instant seule la saisie des lettre et le visuel graphique marche je n'ai pas reussi 
a trouver pourquoi lorsque j'appuie sur la validation de la lettre ca ne prend pas en compte

"""

from Lib_Fonctions import ChoisirUnMot,RemplissageMot,TestLetrre, RejouerEncore
from tkinter import END, Button, ALL, Tk, PhotoImage, Canvas, Label, Frame, FLAT, Entry
# GIT : https://github.com/AdriLyon/TP2_DEV_PYTHON

#Saisie de la lettre adapter car l'utilisateur ne saisit pas sa lettre dans le terminal mais directement dans l'interface

def SaisieLettre(event):
    global Tentatives
    global LettresDejaTrouvees
    global mot
    global lettre
    global meilleurScore
    lettre = maSaisie.get()[0].upper() #passe la lettre en majuscule 
    maSaisie.delete(0,END);
    if lettre in lettre :
        return;        
    lettre += lettre
    if TestLetrre(lettre, mot, LettresDejaTrouvees): 
        lProposition=RemplissageMot(LettresDejaTrouvees, mot)
        labelProposition["text"] = "".join(lProposition)
        if not('_' in lProposition):
            Score = 8 - Tentatives
            if meilleurScore > Score:
                meilleurScore = Score
            labelTentatives["text"] = "".join("Ton meilleur score est de %d Score." % (meilleurScore))
            monBouton.configure(text = "RejouerEncore")
            monBouton.bind("<Button-1>", RejouerEncore)
    else :
        Tentatives -= Tentatives  
        monCanvas.delete(ALL)
        monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=ImagesBonhommes[8-Tentatives])
        if Tentatives == 0 : #si on est sorti du while est qu'on a plus de tentative ça signifie qu'on a perdu            
            labelTentatives["text"] = "".join("Tu as perdu :(")
            labelProposition["text"] = "".join(mot) 
            monBouton.configure(text="RejouerEncore")
            monBouton.bind("<Button-1>", RejouerEncore)               
        else:
            labelTentatives["text"] = "".join("Il vous reste %s tentatives" % Tentatives)
            return

#Declaration Initialles , comme dans la version "classique"
Tentatives = 8 
mot = ChoisirUnMot()
lettre = [mot[0]] 
LettresDejaTrouvees = [mot[0]] 
proposition = RemplissageMot(LettresDejaTrouvees, mot)
meilleurScore = 8

# fenêtre graphique 
MaFentrePendu = Tk()
MaFentrePendu.title("Jeu du pendu")


    
# images
ImagesBonhommes = [PhotoImage(file="ImagesBonhommes/bonhomme%s.gif" % j) for j in range(1,Tentatives+1)]

# Création de la zone pour afficher les images
largeurImage = ImagesBonhommes[0].width()
hauteurImage = ImagesBonhommes[0].height()
monCanvas = Canvas(MaFentrePendu, width=largeurImage, height=hauteurImage, highlightthickness=0)
monCanvas.grid(row=0, column=0, padx=20, pady=20)

#Chargement d'une image
monCanvas.delete(ALL)
monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=ImagesBonhommes[0])

#Création d'une frame pour pouvoir mettre le label proposition et tentative 
monCadreLabel = Frame(MaFentrePendu, bg='#444644')
monCadreLabel.grid(row=0, column=1)

# Afficher le mot et les tentatives qu'il reste
labelProposition = Label(monCadreLabel, font=('Deja Vu Sans Mono', 45, 'bold'), width=26, fg="white")
labelProposition.grid(row=0, column=0)
labelProposition.configure(bg='#444644')

labelTentatives = Label(monCadreLabel, font=('Deja Vu Sans Mono', 14, 'bold'), width=60, fg="white")
labelTentatives.grid(row=1, column=0)
labelTentatives.configure(bg='#444644')


#Zone de saisie de la lettre
ZoneSaisie = Frame(MaFentrePendu, bg='grey')
ZoneSaisie.grid(row=1,column=1)

maSaisie = Entry(ZoneSaisie, font=('Deja Vu Sans Mono', 20, 'bold'), width=5, bg="white")
maSaisie.grid(row=0, column=0)

# Bouton pour valider la saisie de la lettre
monBouton = Button(ZoneSaisie, text="Proposer", relief=FLAT, font=('Deja Vu Sans Mono', 14, 'bold'))
monBouton.grid(row=0, column=1, padx=20)
monBouton.bind("<Button-1>", SaisieLettre)
    
labelProposition["text"] = "".join(proposition)
labelTentatives["text"] = "".join("Il vous reste %s tentatives" % Tentatives)


MaFentrePendu.mainloop()