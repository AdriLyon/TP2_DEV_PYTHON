#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:13:57 2020
Librairie consacrés aux fonctions nécessaires à la première et à la deuxième 
version du mode console de notre jeu du pendu.

@author: adrien.covarel
"""

import random
 
def ChoisirUnMot():
    """ cette focntion sert à ouvir le fichier remplit de mots, lire chaque mot 
    puis en choisir un au hasard avec la commande random.choice(mots) """
    
    fich = open('mots.txt','r')
    mots = fich.readlines()
    fich.close()
    return random.choice(mots).strip('\n')

    

def TestLetrre(mot,lettre,LettresTrouvees):
    """ cette fonction nous permet de tester si la lettre taper par l'utilisateur se trouve dans 
    le mot a touver, si c'est le cas la lettre est rajouter aux autres lettres deja trouvees"""
    if lettre in mot:
        LettresTrouvees += lettre
        print ("\ Bravo ! la lettre est presente")
        return True
    return False


def RemplissageMot(LettresTrouvees,MotATrouver):
    """ cette fonction sert d'abord a remplir le mot au fur et a mesure des lettres proposees
    par l'utilisateur, a son premier appel, il n'y aura donc que la premiere lettre suivie des _
    correspondants aux lettres restantes, puis a chaque lettre trouve on cherche l'emplacement correspondant
    dans le mot a trouver et donc on remplace le _ par la lettre correspondante"""
    MotARemplir = ""

    for x in MotATrouver:

        if x in LettresTrouvees :

            MotARemplir += x + ' '

        else :

            MotARemplir += '_ ' 

    return MotARemplir

def Rejouer():
    """ cette fonction va demander a l'utilisateur de rentrer au clavier si il souhaite rejouer ou non
    la fonction retourne alors sa réponse et si il ne retourne pas 1 ou 2 on lui demande de retaper sa réponse"""
    erreur = 1
    while erreur == 1:
        decision = input("Si tu veux rejouer, appuies sur o , sinon appuies sur n : ")[0].upper()
        if decision == "O" :
            erreur = 0
            return True
        if decision == "N" :
            erreur = 0
            print("D'accord , a bientot ! ")
            return False
        else:
            print ("Vous n'avez pas taper la bonne lettre")

    
def LettreDejaProposee(lettre,LettresProposees):
    if lettre in LettresProposees:              # Test  pour voir si la lettre a deja ete tapee par l'utilisateur
        print("Cette lettre a deja ete proposee")
        return True         #Si oui , on lui dit
    else:
        LettresProposees += lettre # si non, on ajoute sa lettre a la liste des lettres deja proposees
        return False           
        

#Fonction RejouerEncore adapter a notre interface
def RejouerEncore(event):
    global mot
    global lettre
    global LettresDejaTrouvees
    global proposition
    Tentatives=8
    mot=fChoisirUnMot(mot)
    lettre=[mot[0]] 
    LettresDejaTrouvees=[mot[0]] 
    proposition=fRemplirProposition(LettresDejaTrouvees, mot)
    monCanvas.delete(ALL)
    monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=ImagesBonhommes[0])
    monBouton.configure(text="Proposer")
    monBouton.bind("<Button-1>", SaisieLettre)
    labelProposition["text"] = "".join(proposition)
    labelTentatives["text"] = "".join("Il vous reste %s tentatives" % Tentatives)

#Saisie de la lettre adapter car l'utilisateur ne saisit pas sa lettre dans le terminal mais directement dans l'interface

