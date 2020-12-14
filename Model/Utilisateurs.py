import csv

class Utilisateurs:

    def __init__(self, nom: str, prenom: str, pseudo:str):
        self.__nom = nom
        self.__prenom = prenom
        self.__pseudo = pseudo


    @property
    def getPseudo(self):
        return self.__pseudo

    @property
    def getprenom(self):
        return self.__prenom

    @property
    def getnom(self):
        return self.__nom

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

            with open("../utilisateur_sauvegarde/utilisateur.csv","a",newline='') as fichier_Utilisateur:

                entete = ["Nom","Prénom","Utilisateur"]
                donne = [nom,prenom,utilisateur]

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')


