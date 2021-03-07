#! / usr / bin / env python
# - * - codage: utf-8 - * -

import csv


class Utilisateurs:

    def __init__(self, nom: str, prenom: str, pseudo: str):
        """
        Cela construit un utilisateur basée sur son nom,prénom et pseudo
        PRE: nom , prenom et pseudo sont des strings
        POST: -
        """

        self.__nom = nom
        self.__prenom = prenom
        self.__pseudo = pseudo

    @property
    def get_pseudo(self):
        return self.__pseudo

    @property
    def getprenom(self):
        return self.__prenom

    @property
    def getnom(self):
        return self.__nom

    def sauvegarde_utilisateur(self, nom: str, prenom: str, pseudo: str):

        """
        Cette fonction me permet de sauvegarder mes utilisateurs dans un fichier csv
        PRE: nom,prenom et pseudo sont des strings
        POST: -
        """

        try:

            with open("../utilisateur_sauvegarde/utilisateur.csv", "a", newline='') as fichier_Utilisateur:

                # entete = ["Nom", "Prénom", "pseudo"]
                donne = [nom, prenom, pseudo]

                # csv_fichier = csv.DictWriter(fichier_Utilisateur, fieldnames=entete)
                # csv_fichier.writeheader()

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')
