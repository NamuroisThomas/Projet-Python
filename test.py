import unittest

from Model.Question import Question
from Model.Utilisateur import Utilisateurs


class TestUtilisateur(unittest.TestCase):
    """
    Test unitaire de la classe Utilisateurs
    Fait par Ben-Tahri Merwane
    """

    def test_init(self):
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").pseudo(), 'Poire789')
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").nom(), 'Pierre')
        self.assertEqual(Utilisateurs("Pierre", "Patric", "Poire789").prenom(), 'Patric')

        self.assertEqual(Utilisateurs("Tom", "Jedusor", "VOSpo").pseudo(), "VOSpo")
        self.assertEqual(Utilisateurs("Tom", "Jedusor", "VOSpo").nom(), "Tom")
        self.assertEqual(Utilisateurs("Tom", "Jedusor", "VOSpo").prenom(), "Jedusor")

    def test_sauvegarde_utilisateur(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').sauvegarde_utilisateur)), "_csv.writer")

    def test_ajout_id(self):
        self.assertTrue(str(type(Utilisateurs('tom', 'tim', 'TOTO145').ajout_id)), "_csv.writer" and "_csv.reader")


class TestQuestion(unittest.TestCase):
    """
   Test unitaire de la classe Question
   Fait par thomas Namurois

    """

    def test_init(self):
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'a').question(),
                         "Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président")
        self.assertEqual(Question("Qui est TK78 ? : (a) Héro (b) Youtubeur (c) Président", 'b').reponse(),
                         'b')

        self.assertEqual(
            Question("Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles", "c").question(),
            "Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles")
        self.assertEqual(
            Question("Quelle est la capitale de la Belgique ?: (a)Berlin, (b)Sofia, (c)Bruxelles", "c").reponse(),
            'c')
