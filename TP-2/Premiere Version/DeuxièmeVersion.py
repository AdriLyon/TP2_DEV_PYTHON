#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:13:59 2020

On codera ici la deuxième version de notre jeu du pendu qui consistera à optimiser
la première en ajoutant plusieurs améliorations: prévenir si le joueur a déja donné
une lettre, proposer de rejouer en fin de partie et retenir le meilleur score.

@author: adrien.covarel
"""
# GIT : https://github.com/AdriLyon/TP2_DEV_PYTHON

import Lib_Fonctions

Rejouer = True

while (Rejouer == True):
    tentatives = 8
    mot = Lib_Fonctions.ChoisirUnMot()
    LettresTrouvees = [mot[0]]
    LettresProposees = [mot[0]]
    Affichage = Lib_Fonctions.RemplissageMot(LettresTrouvees,mot) 
    MeilleurScore = 0
    
    while ('_' in Affichage) and (tentatives > 0) and Rejouer==True:
        
        print ("Tentatives Restantes : " + str(tentatives) )
        
        print("Mot a deviner : ", Affichage)
        
        lettre = input("Saisies une lettre : ")[0].upper()

        if Lib_Fonctions.LettreDejaProposee(lettre,LettresProposees): 
            while Lib_Fonctions.LettreDejaProposee(lettre,LettresProposees) == True: # si la lettre a deja ete propose , l'utlisateur rentre une nouvelle lettre
                lettre = input("Saisies une lettre : ")[0].upper()                      
        
        if Lib_Fonctions.TestLetrre(mot,lettre,LettresTrouvees):
            
            Affichage = Lib_Fonctions.RemplissageMot(LettresTrouvees,mot)  
            
        if lettre not in mot:
            tentatives -= 1
        
        if tentatives == 0 : 
            print("Perdu :( la solution etait : " + mot)        
            Rejouer = Lib_Fonctions.Rejouer()
         
        if '_' not in Affichage :
            print("BRAVO tu as trouve :  " + mot)
            
            Score = 8 - tentatives
            if Score > MeilleurScore and Score >0 :
                MeilleurScore = Score
                print("Nouveau record , tu as fais seulement " + str(MeilleurScore) + " erreurs")
            Rejouer = Lib_Fonctions.Rejouer()
    
    

