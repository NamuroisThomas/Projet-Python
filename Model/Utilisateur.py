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

    def pseudo(self):


    def prenom(self):
        return self.__prenom

    def nom(self):
        return self.__nom


    def sauvegarde_utilisateur(self):

        """
        Cette fonction me permet de sauvegarder un utilisateur dans un fichier csv
        PRE: -
        POST: le fichier utilisateur.csv a été modifié et contient un nouvel utilisateur
        """

        #crée l'execption et ka metttre dna lhéritage

        try:
            with open("../utilisateur_sauvegarde/utilisateur.csv", "a", encoding='utf-8') as fichier_Utilisateur:
                # entete = ['ID',"Nom", "Prenom", "Pseudo"]
                donne = ['', self.__nom, self.__prenom, self.__pseudo]


       
                # csv_fichier = csv.DictWriter(fichier_Utilisateur, fieldnames=entete)
                # csv_fichier.writeheader()

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)

                Utilisateurs.ajout_id(self)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')


    def ajout_id(self):

        """
        Cette fonction me permet la création d'ID pour chaque utilisateur contenue dans le fichier csv
        PRE:-
        POST:le fichier utilisateur.csv à été modifier en ajoutant un ID à chaque utilisateurs
        """

        fichier_id = []

        with open('../utilisateur_sauvegarde/utilisateur.csv', 'r') as fichier_utilisateur:
            lecture_utilisateurs = csv.DictReader(fichier_utilisateur)
            id = 0

            for row in lecture_utilisateurs:
                id += 1
                row["ID"] = str(id)
                fichier_id.append(row)

        with open('../utilisateur_sauvegarde/utilisateur.csv', 'w') as fichier_utilisateur_ecriture:
            sauvegarde = csv.DictWriter(fichier_utilisateur_ecriture,
                                        fieldnames=["ID", "Nom", "Prenom", "Pseudo"])
            sauvegarde.writeheader()
            sauvegarde.writerows(fichier_id)


"""
if __name__ == "__main__":
    Utilisateurs("A", "A", "A").ajout_id()
"""

