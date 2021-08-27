import os
import os.path
import unittest
from unittest import TestCase

import csv
import os
import os.path
import unittest
from datetime import datetime

import pandas as pd

from Model.Partie import Partie
from Model.Question import Question
from Model.Utilisateur import Utilisateurs
from Model.Utilisateur import Utilisatrices
from Model.Jeu import Jeu
from erreur.Erreur import ErreurCustomiser


class TestUtilisateur(unittest.TestCase):
    """
    Test unitaire de la classe Utilisateurs
    Fait par Ben-Tahri Merwane
    """

    def test_proprety_user_name(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.nom, 'Pierre')
        self.assertEqual(test_user_2.nom, "Tom")

        self.assertNotEqual(test_user_1.nom, "Tom")
        self.assertNotEqual(test_user_2.nom, 'Pierre')

    def test_proprety_user_firstname(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.prenom, 'Patric')
        self.assertEqual(test_user_2.prenom, "Jedusor")

        self.assertNotEqual(test_user_1.prenom, 'PaPA')
        self.assertNotEqual(test_user_2.prenom, "Juda")

    def test_proprety_user_pseudo(self):
        test_user_1 = Utilisateurs("Pierre", "Patric", "Poire789")

        test_user_2 = Utilisateurs("Tom", "Jedusor", "VOSpo")

        self.assertEqual(test_user_1.pseudo, 'Poire789')
        self.assertEqual(test_user_2.pseudo, "VOSpo")

        self.assertNotEqual(test_user_1.pseudo, 'PoikjQSnjkdne789')
        self.assertNotEqual(test_user_2.pseudo, "VOSkosJDFkosJFKOpo")


class test_utilisatrices(unittest.TestCase):
    def test_creation_utilisatrice(self):
        self.assertEqual(type(Utilisatrices("Bentahri","Merwane","Tata").nom), type(""))
        self.assertNotEqual(type(Utilisatrices("Bentahri", "Merwane", "Tata").nom), type(42))
        self.assertEqual(type(Utilisatrices("Bentahri","Merwane","Tata").prenom), type(""))
        self.assertNotEqual(type(Utilisatrices("Bentahri", "Merwane", "Tata").prenom), type(42))
        self.assertEqual(type(Utilisatrices("Bentahri", "Merwane", "Tata").pseudo), type(""))
        self.assertNotEqual(type(Utilisatrices("Bentahri", "Merwane", "Tata").pseudo), type(42))

        self.assertEqual(Utilisatrices("Bentahri", "Merwane", "Tata").nom, "Bentahri")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").nom, "Bentahr")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").nom, 42)
        self.assertEqual(Utilisatrices("Bentahri", "Merwane", "Tata").prenom, "Merwane")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").prenom, "Merwan")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").prenom, 42)
        self.assertEqual(Utilisatrices("Bentahri", "Merwane", "Tata").pseudo, "Tata")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").pseudo, "Tat")
        self.assertNotEqual(Utilisatrices("Bentahri", "Merwane", "Tata").pseudo, 42)

    def test_sauvegarde_utilisateur(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').sauvegarde_utilisateur)), "_csv.writer")

        path = 'utilisateur_sauvegarde/utilisateur.csv'
        user = ['', 'POPPY', 'CAT', 'DUCK']

        with open(path, "a", encoding='utf-8') as fichier_Utilisateur:

            sauvegarde = csv.writer(fichier_Utilisateur)
            sauvegarde.writerow(user)

        if os.path.isfile(path) and os.access(path, os.W_OK):
            print("le fichier existe et peut être lue")

            users = []

            try:

                with open(path, 'r') as fichier_utilisateur:
                    lecture_utilisateurs = csv.DictReader(fichier_utilisateur)

                    for row in lecture_utilisateurs:
                        users.append([row['Nom'], row['Prenom'], row['Pseudo']])
                    print(users[-1])

                    if users[-1][0] == user[1] and users[-1][1] == user[2] and users[-1][2] == user[3]:

                        print('Utilisateur test bien ajouté')

                    else:
                        print('Utilisateur Test non ajouté')

            except FileNotFoundError:

                print('Fichier introuvable.')
                erreur_filenotfounderror = ErreurCustomiser('FileNotFoundError')
                erreur_filenotfounderror.sauvegarde_erreur()

            except IOError:

                print('Erreur IO.')
                erreur_ioerror = ErreurCustomiser('Erreur IO.')
                erreur_ioerror.sauvegarde_erreur()

        else:
            print("le fichier est introuvable ou ne peut être lue")

    def test_ajout_id(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').ajout_id)), "_csv.writer" and "_csv.reader")
        path = 'utilisateur_sauvegarde/utilisateur.csv'

        if os.path.isfile(path) and os.access(path, os.R_OK):
            print("le fichier existe et peut être lue")

            df = pd.read_csv(path)
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


class TestErreurCustomiser(unittest.TestCase):
    """
    Test unitaire de la classe ErreurCustomiser
    Fait par Ben-Tahri Merwane
    """

    def test_Erreurs(self):

        self.assertEqual(ErreurCustomiser("FileNotFoundError").erreurs(), "FileNotFoundError")
        self.assertEqual(ErreurCustomiser("IOError").erreurs(), "IOError")

        self.assertNotEqual(ErreurCustomiser("FileNotFoundError").erreurs(), "error")
        self.assertNotEqual(ErreurCustomiser("IOError").erreurs(), "error")

    def test_sauvegarde_erreur(self):

        path = 'erreur/sauvegarde_erreurs.txt'
        erreur = "TEST FONCTIONELLE"
        try:
            with open(path, 'a', encoding='utf-8') as fichier_des_erreurs:

                if os.path.isfile(path) and os.access(path, os.W_OK):
                    print("le fichier existe et peut être lue ou écrire dedans")
                    now = datetime.now()

                    message_detection_erreur = f"=" * 40 + f" A {now} , Erreur trouvée " + "=" * 40
                    message_erreur = f"\nUne erreur à été détecté et la voici : {erreur}"

                    fichier_des_erreurs.write("\n")
                    fichier_des_erreurs.write(message_detection_erreur)
                    fichier_des_erreurs.write(message_erreur)

                    # fichier_des_erreurs.write(f"=" * 40 + " Bienvenue dans votre fichier d'erreurs" + "=" * 40)
                    # ichier_des_erreurs.write(message_de_debut)
                    with open(path, "r", encoding='utf-8') as f:
                        message_erreur_sauvergarde = f"Une erreur à été détecté et la voici : {erreur}"
                        # juste les 5 dernières lignes, mais Python a en effet lu tout le fichier
                        for ligne in f.readlines()[-1:]:
                            print(ligne)

                        if ligne == message_erreur_sauvergarde:
                            print("erreur bien sauvegarder")

                        else:
                            print("erreur non sauvegardé")

                else:
                    print("le fichier est introuvable ou ne peut être lue")

        except IOError:
            print('Erreur IO.')


class TestPartie(unittest.TestCase):
    """
      Test unitaire de la classe Partie
      Fait par Ben-Tahri Merwane
       """

    def test_affiche(self):
        partie1 = Partie()

        self.assertEqual(partie1.affichage(), "Bonne Partie à vous")
        self.assertNotEqual(partie1.affichage(), "Bonne Partie à toi")

        partie2 = Partie()

        self.assertEqual(partie2.affichage(), "Bonne Partie à vous")
        self.assertNotEqual(partie2.affichage(), "Bonne Partie à vou")

    def test_theme(self):
        partie1 = Partie()

        self.assertEqual(partie1.le_theme(), '')
        self.assertNotEqual(partie1.le_theme(), 'POMME')

        partie2 = Partie()

        self.assertEqual(partie2.le_theme(), '')
        self.assertNotEqual(partie2.le_theme(), 'thème')

    def test_tableauQuestion(self):
        partie1 = Partie()

        self.assertEqual(partie1.tableauquestion(), [])
        self.assertNotEqual(partie1.tableauquestion(), 'tableauQuestion')

        partie2 = Partie()

        self.assertEqual(partie2.tableauquestion(), [])
        self.assertNotEqual(partie2.tableauquestion(), {})


class TestQuestion(unittest.TestCase):
    """
   Fait par thomas Namurois

    """

    def test_type_question(self):
        self.assertEqual(type(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question()),
                         type(""))
        self.assertNotEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question(),
                            type(42))

    def test_value_question(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question(),
                         "Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président")
        self.assertNotEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question(), 42)

    def test_type_reponse(self):
        self.assertEqual(type(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').reponse()),
                         type("a"))
        self.assertNotEqual(type(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').reponse()),
                            type(42))

    def test_value_reponse(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').reponse(), "a")
        self.assertNotEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').reponse(), 42)


class testJeu(unittest.TestCase):
    """
   Fait par thomas Namurois

    """

    def test_creation_Jeu(self):
        jeu = Jeu("Namurois", "Thomas", "toto")

        self.assertEqual(type(jeu.nom), type(""))
        self.assertNotEqual(type(jeu.nom), type(42))
        self.assertEqual(type(jeu.prenom), type(""))
        self.assertNotEqual(type(jeu.prenom), type(42))
        self.assertEqual(type(jeu.pseudo), type(""))
        self.assertNotEqual(type(jeu.pseudo), type(42))

        self.assertEqual(jeu.nom, "Namurois")
        self.assertNotEqual(jeu.nom, "Namuroi")
        self.assertNotEqual(jeu.nom, 42)
        self.assertEqual(jeu.prenom, "Thomas")
        self.assertNotEqual(jeu.prenom, "Thoma")
        self.assertNotEqual(jeu.prenom, 42)
        self.assertEqual(jeu.pseudo, "toto")
        self.assertNotEqual(jeu.pseudo, "tot")
        self.assertNotEqual(jeu.pseudo, 42)

    def test_type_affichage(self):
        self.assertEqual(type(Jeu("Namurois", "Thomas", "toto").affichage()), type(""))
        self.assertNotEqual(type(Jeu("Namurois", "Thomas", "toto").affichage()), type(42))

    def test_valeur_affichage(self):
        self.assertEqual(Jeu("Namurois", "Thomas", "toto").affichage(), "Bon Jeu à vous")
        self.assertNotEqual(Jeu("Namurois", "Thomas", "toto").affichage(), "Bon Jeu à vou")

    def test__type_utilisateur(self):
        self.assertEqual(type(Jeu("Namurois", "Thomas", "toto").utilisateur()), type(""))
        self.assertNotEqual(type(Jeu("Namurois", "Thomas", "toto").utilisateur()), type(42))

    def test_valeur_utilisateur(self):
        self.assertEqual(Jeu("Namurois", "Thomas", "toto").utilisateur(), "toto")
        self.assertNotEqual(Jeu("Namurois", "Thomas", "toto").utilisateur(), "tata")
        self.assertNotEqual(Jeu("Namurois", "Thomas", "toto").utilisateur(), 42)

    def test_type_tableau_question_partie(self):
        self.assertEqual(type(Jeu("Namurois", "Thomas", "toto").tableau_question_partie()), type([]))
        self.assertNotEqual(type(Jeu("Namurois", "Thomas", "toto").tableau_question_partie()), type(42))
        self.assertNotEqual(type(Jeu("Namurois", "Thomas", "toto").tableau_question_partie()), type(""))
