#! / usr / bin / env python
# - * - codage: utf-8 - * -

import csv

from erreur.Erreur import ErreurCustomiser


class Utilisateurs:

    def __init__(self, nom: str, prenom: str, pseudo: str):

        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.sexe = 'M'

    def pseudo(self):
        return self.pseudo

    def prenom(self):
        return self.prenom

    def nom(self):
        return self.nom

    def sexe(self):
        return self.sexe

    def sauvegarde_utilisateur(self):

        """
        Cette fonction me permet de sauvegarder un utilisateur dans un fichier csv
        PRE: -
        POST: le fichier utilisateur.csv a été modifié et contient un nouvel utilisateur
        """

        try:
            with open("../utilisateur_sauvegarde/utilisateur.csv", "a", encoding='utf-8') as fichier_Utilisateur:
                # entete = ['ID', "Nom", "Prenom", "Pseudo", "Sexe"]
                donne = ['', self.nom, self.prenom, self.pseudo, self.sexe]

                # csv_fichier = csv.DictWriter(fichier_Utilisateur, fieldnames=entete)
                # csv_fichier.writeheader()

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)
                print("Utilisateur bien ajouté")

                Utilisateurs.ajout_id(self)

        except FileNotFoundError:
            print('Fichier introuvable.')
            erreur_FileNotFoundError = ErreurCustomiser('FileNotFoundError')
            erreur_FileNotFoundError.sauvegarde_erreur()



        except IOError:
            print('Erreur IO.')
            erreur_IOError = ErreurCustomiser('Erreur IO.')
            erreur_IOError.sauvegarde_erreur()

    def ajout_id(self):

        """
        Cette fonction me permet la création d'ID pour chaque utilisateur contenue dans le fichier csv
        PRE:-
        POST:le fichier utilisateur.csv à été modifier en ajoutant un ID à chaque utilisateurs
        """

        fichier_id = []

        try:

            with open('../utilisateur_sauvegarde/utilisateur.csv', 'r') as fichier_utilisateur:
                lecture_utilisateurs = csv.DictReader(fichier_utilisateur)
                id = 0

                for row in lecture_utilisateurs:
                    id += 1
                    row["ID"] = str(id)
                    fichier_id.append(row)

            with open('../utilisateur_sauvegarde/utilisateur.csv', 'w') as fichier_utilisateur_ecriture:
                sauvegarde = csv.DictWriter(fichier_utilisateur_ecriture,
                                            fieldnames=["ID", "Nom", "Prenom", "Pseudo", "Sexe"])
                sauvegarde.writeheader()
                sauvegarde.writerows(fichier_id)

        except FileNotFoundError:
            print('Fichier introuvable.')
            erreur_FileNotFoundError = ErreurCustomiser('FileNotFoundError')
            erreur_FileNotFoundError.sauvegarde_erreur()



        except IOError:
            print('Erreur IO.')
            erreur_IOError = ErreurCustomiser('Erreur IO.')
            erreur_IOError.sauvegarde_erreur()

    def verification_ajout_utilisateur(self):

        dernier_utilisateur = []

        try:
            with open('../utilisateur_sauvegarde/utilisateur.csv', 'r') as fichier_utilisateur:
                lecture_utilisateurs = csv.reader(fichier_utilisateur)

                for utilisateur in lecture_utilisateurs:
                    dernier_utilisateur.append(utilisateur)
                print(dernier_utilisateur[-2][1])
                print(dernier_utilisateur[-2][2])
                print(dernier_utilisateur[-2][3])




        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')


class Utilisatrices(Utilisateurs):
    def __init__(self, nom: str, prenom: str, pseudo: str):

        self.__nom = nom
        self.__prenom = prenom
        self.__pseudo = pseudo
        # Appelez au constructeur de la classe mère (Utilisateur)
        # pour attribuer la valeur au attribut 'name' de la classe mère.
        super().__init__(nom, prenom, pseudo)
        self.__sexe = 'F'

    def sexe(self):
        return self.__sexe

    def sauvegarde_utilisateur(self):

        """
        Cette fonction me permet de sauvegarder un utilisateur dans un fichier csv
        PRE: -
        POST: le fichier utilisateur.csv a été modifié et contient un nouvel utilisateur
        """

        try:
            with open("../utilisateur_sauvegarde/utilisateur.csv", "a", encoding='utf-8') as fichier_Utilisateur:
                # entete = ['ID', "Nom", "Prenom", "Pseudo", "Sexe"]
                donne = ['', self.__nom, self.__prenom, self.__pseudo, self.__sexe]

                # csv_fichier = csv.DictWriter(fichier_Utilisateur, fieldnames=entete)
                # csv_fichier.writeheader()

                sauvegarde = csv.writer(fichier_Utilisateur)
                sauvegarde.writerow(donne)
                print("Utilisateur bien ajouté")

                Utilisateurs.ajout_id(self)

        except FileNotFoundError:
            print('Fichier introuvable.')
            erreur_FileNotFoundError = ErreurCustomiser('FileNotFoundError')
            erreur_FileNotFoundError.sauvegarde_erreur()



        except IOError:
            print('Erreur IO.')
            erreur_IOError = ErreurCustomiser('Erreur IO.')
            erreur_IOError.sauvegarde_erreur()

    def ajout_id(self):

        """
        Cette fonction me permet la création d'ID pour chaque utilisateur contenue dans le fichier csv
        PRE:-
        POST:le fichier utilisateur.csv à été modifier en ajoutant un ID à chaque utilisateurs
        """

        fichier_id = []

        try:

            with open('../utilisateur_sauvegarde/utilisateur.csv', 'r') as fichier_utilisateur:
                lecture_utilisateurs = csv.DictReader(fichier_utilisateur)
                id = 0

                for row in lecture_utilisateurs:
                    id += 1
                    row["ID"] = str(id)
                    fichier_id.append(row)

            with open('../utilisateur_sauvegarde/utilisateur.csv', 'w') as fichier_utilisateur_ecriture:
                sauvegarde = csv.DictWriter(fichier_utilisateur_ecriture,
                                            fieldnames=["ID", "Nom", "Prenom", "Pseudo", "Sexe"])
                sauvegarde.writeheader()
                sauvegarde.writerows(fichier_id)

        except FileNotFoundError:
            print('Fichier introuvable.')
            erreur_FileNotFoundError = ErreurCustomiser('FileNotFoundError')
            erreur_FileNotFoundError.sauvegarde_erreur()



        except IOError:
            print('Erreur IO.')
            erreur_IOError = ErreurCustomiser('Erreur IO.')
            erreur_IOError.sauvegarde_erreur()


if __name__ == "__main__":
    Utilisatrices("TEST", "UTILISATRICE", "UUUU").sauvegarde_utilisateur()

# Utilisateurs("TEST1", "TEST1", "TEST2").sauvegarde_utilisateur()
