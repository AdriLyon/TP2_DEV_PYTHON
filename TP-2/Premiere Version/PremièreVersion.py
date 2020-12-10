#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:13:55 2020

On codera ici le programme principal de la première version de notre jeu du 
pendu : on veut choisir un mot au hasard, afficher sa première lettre, puis 
laissé 8 chances au joueur pour trouver le mot.

@author: adrien.covarel
"""
# GIT : https://github.com/AdriLyon/TP2_DEV_PYTHON
import Lib_Fonctions

tentatives = 8
mot = Lib_Fonctions.ChoisirUnMot() # mot pris au hasard dans notre fichier texte
LettresTrouvees = [mot[0]] # on definit la premiere lettre du mot
Affichage = Lib_Fonctions.RemplissageMot(LettresTrouvees,mot)   # on affiche cette premiere lettre


while ('_' in Affichage) and (tentatives > 0) :
    
    print ("Tentatives Restantes : " + str(tentatives) )
    
    print("Mot a deviner : ", Affichage)
    
    lettre = input("Saisies une lettre : ")[0].upper() # L'utilisateur saisie la lettre qu'il veut
    
    if Lib_Fonctions.TestLetrre(mot,lettre,LettresTrouvees): # Si la lettre fait partie du mot , alors on l'affiche dans le mot a remplir
        
        Affichage = Lib_Fonctions.RemplissageMot(LettresTrouvees,mot)  
        
    if lettre not in mot: # si la lettre n'en fait pas partie alors l'utilisateur possède une tentative en moins
        
        tentatives -= 1
    
    

if tentatives == 0 : # l'utilisateur a utiliser toutes ses tentatives

    print("Perdu :( la solution etait : " + mot)
    Rejouer = Lib_Fonctions.Rejouer()

else: # toute les lettres ont ete trouvees , victoire !

    print("BRAVO tu as trouve :  " + mot)
      




