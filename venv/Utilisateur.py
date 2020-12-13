import os

import csv
import datetime

class utilisateur:

    def __init__(self,nom:str , prenom : str, utilisateur:str):

        self.__iduser = 0
        self.__utilisateur = utilisateur
        self.__nom = nom
        self.__prenom = prenom


    @property
    def iduser(self):
        return self.__iduser

    @property
    def utilisateur(self):
        return self.__utilisateur

    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom


    def sauvegarde_utilisateur( nom :str,prenom : str,utilisateur : str  ):

        """
        Cette fonction me permet de sauvegarder mes utilisateurs dans un fichier csv

        :param nom: nom du joueur
        :param prenom:prenom du joueur
        :param utilisateur:pseudo de utilisateur

        :return:-
        """

        try:
            """
            la librairie csv me permet l'échange de données avec un fichier csv
            
            
            csv_fichier = csv.DictWriter(fichier_Utilisateur,fieldnames=entete)
            csv_fichier.writeheader()
            """

            with open("./utilisateur_sauvegarde/utilisateur.csv","a",newline='') as fichier_Utilisateur:

                entete = ["Nom","Prénom","Utilisateur"]
                donne = [nom,prenom,utilisateur]

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')

    def recuperation_utilisateur():


        try:

            with open("./utilisateur_sauvegarde/utilisateur.csv","r",newline='') as fichier_sauvegarde_utilisateur:
                utilisateur_sauvegarde = csv.reader(fichier_sauvegarde_utilisateur)
                for r in utilisateur_sauvegarde:
                    print(r)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')




















