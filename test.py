import os
import os.path
import unittest
from unittest import TestCase




import pandas as pd
import csv

from erreur.Erreur import ErreurCustomiser


from Model.Question import Question
from Model.Utilisateur import Utilisateurs


class TestUtilisateur(unittest.TestCase):
    """
    Test unitaire de la classe Utilisateurs
    Fait par Ben-Tahri Merwane
    """

    def test_proprety_user_name(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.nom(), 'Pierre')
        self.assertEqual(test_user_2.nom(), "Tom")

    def test_proprety_user_firstname(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.prenom(), 'Patric')
        self.assertEqual(test_user_2.prenom(), "Jedusor")

    def test_proprety_user_pseudo(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.pseudo(), 'Poire789')
        self.assertEqual(test_user_2.pseudo(), "VOSpo")

    def test_sauvegarde_utilisateur(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').sauvegarde_utilisateur)), "_csv.writer")

        PATH = 'utilisateur_sauvegarde/utilisateur.csv'
        user = ['','POPPY','CAT','DUCK']


        with open(PATH, "a", encoding='utf-8') as fichier_Utilisateur:

            sauvegarde = csv.writer(fichier_Utilisateur)
            sauvegarde.writerow(user)

        if os.path.isfile(PATH) and os.access(PATH, os.W_OK):
            print("le fichier existe et peut être lue")

            users = []

            try:

                with open(PATH, 'r') as fichier_utilisateur:
                    lecture_utilisateurs = csv.DictReader(fichier_utilisateur)


                    for row in lecture_utilisateurs:

                       users.append([row['Nom'],row['Prenom'],row['Pseudo']])
                    print(users[-1])


                    if users[-1][0] == user[1] and users[-1][1] == user[2] and users[-1][2] == user[3]:

                        print('Utilisateur test bien ajouté')

                    else:
                        print('Utilisateur Test non ajouté')






            except FileNotFoundError:
                print('Fichier introuvable.')
                erreur_FileNotFoundError = ErreurCustomiser('FileNotFoundError')
                erreur_FileNotFoundError.sauvegarde_erreur()



            except IOError:
                print('Erreur IO.')
                erreur_IOError = ErreurCustomiser('Erreur IO.')
                erreur_IOError.sauvegarde_erreur()


        else:
            print("le fichier est introuvable ou ne peut être lue")

    def test_ajout_id(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').ajout_id)), "_csv.writer" and "_csv.reader")
        PATH = 'utilisateur_sauvegarde/utilisateur.csv'

        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print("le fichier existe et peut être lue")

            df = pd.read_csv(PATH)
            # lecture du fichier utilisateur.csv , ou sont stocker les données utilisateurs

            data = df.head()
            # Retourne les n premières lignes du fichier

            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                # Gestionnaire de contexte pour définir temporairement des options dans le contexte de l'instruction

                df.to_csv("utilisateur_test.csv", sep='\t', encoding='utf-8')
                # écrit le dataframe avec une tabulation comme séparateur (le défaut est une virgule).

            print(data)
            list_of_column_names = list(df.columns)
            # récupère les noms de colonnes
            print(list_of_column_names)
            if list_of_column_names[0] == 'ID':
                print("la colonne ID est bien crée et incrémenté")
            else:
                print("colonne ID non crée")

        else:
            print("le fichier est introuvable ou ne peut être lue")


class TestQuestion(unittest.TestCase):
    """
   Fait par thomas Namurois

    """

    def test_question(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question(),
                         "Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président")
        self.assertEqual(Question("Quelle est la capital de la Belgique ?: (a)Paris, (b)Bruxelles, (c)Amsterdam",
                                  'b').question(), "Quelle est la capital de la Belgique ?: (a)Paris, (b)Bruxelles, "
                                                   "(c)Amsterdam")

    def test_reponse(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').reponse(),
                         "a")
        self.assertEqual(Question("Quelle est la capital de la Belgique ?: (a)Paris, (b)Bruxelles, (c)Amsterdam",
                                  'b').reponse(), "b")
