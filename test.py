import unittest

from Model.Question import Question
from Model.Utilisateur import Utilisateurs


class TestUtilisateur(unittest.TestCase):
    """
    Test unitaire de la classe Utilisateurs
    Fait par Ben-Tahri Merwane
    """

    def test_init(self):
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").get_pseudo, "Poire789")
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").getnom, "Pierre")
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").getprenom, "Patric")

        self.assertEqual(Utilisateurs("Tom", "Jedusor", "VOSpo").get_pseudo, "VOSpo")

    def test_sauvegarde_utilisateur(self):
        self.assertTrue(str(type(Utilisateurs.sauvegarde_utilisateur('tom', 'tim', 'TOTO145'))), "_csv.writer")


class TestQuestion(unittest.TestCase):
    """
   Test unitaire de la classe Question
   Fait par Ben-Tahri Merwane

    """

    def test_init(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').get_question(),
                         "Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président")
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'b').get_reponse(),
                         'b')

        self.assertEqual(
            Question("Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles", "c").get_question(),
            "Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles")
        self.assertEqual(
            Question("Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles", "c").get_reponse(),
            'c')

    def test_ajout_question(self):
        self.assertEqual(Question.ajout_question('geographie',
                                                 "Quelle est la capitale de l'Albanie ?: (a)Berlin, (b)Sofia, (c)Tirana",
                                                 'c'), {"geographie": [
            ["Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles", "c"],
            ["Quel est le continent qui a la plus grande superficie ?:   (a)Europe, (b)Asie, (c)Afrique", "b"],
            ["Quelle est la capitale de l'Allemagne ? :  (a) Marseille, (b)Berlin, (c) rabat", "b"],
            ["Quelle est la capitale du N\u00e9pal ? (a) Moscou (b) Pattaya (c) Katmandou", "c"],
            ["Dans quelle continent se trouve la Belgique ? : (a) Europe (b) Afrique (c) Asie", "a"]], "histoire": [[
            "Quelle est l'ann\u00e9e de la d\u00e9claration d'ind\u00e9pendance de la Belgique ? :  (a)1830, (b)1940, (c)1257",
            "a"],
            [
                "Quelle est l'ann\u00e9e de la 1er R\u00e9volution Fran\u00e7aise ? :  (a)2018, (b)1789, (c)1919",
                "b"],
            [
                "Qui \u00e0 d\u00e9couvert l'am\u00e9rique (a) Tintin (b) J\u00e9sus (c)  Christophe colomb",
                "c"],
            [
                "En quelle ann\u00e9e Napolenon a t'il perdu face au Prusse et anglais ? : (a) 2015 (b) 1715 (c) 1815",
                "c"]],
                             "informatique": [[
                                 "Que signifie DHCP ? :  (a)Dynamic Host CPU Pipe, (b)Dynamic Host Configuration Protocol, (c)Domain Name System",
                                 "b"], [
                                 "Un Spyware est un :   (a)Un virus, (b)Un programme optimisant votre ordinateur, (c)Un espio-logiciel",
                                 "c"], [
                                 "Qui \u00e0 cr\u00e9e Microsoft :  (a) Elon Musk, (b) Claude Fran\u00e7ois, (c) Bill Gates",
                                 "c"], [
                                 "Que signifie HTML ? : (a)Hyper text Markeup language (b)Hyper text Markup language (c)Hyper text Markeup langue",
                                 "a"]]})
