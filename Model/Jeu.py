
#! / usr / bin / env python
# - * - codage: utf-8 - * -


from Model.Partie import Partie
from Model.Utilisateur import Utilisateurs

class Jeu:

    def __init__(self, nom: str, prenom: str, pseudo: str):

        self.__utilisateur = Utilisateurs(nom, prenom, pseudo)
        self.__partie = Partie()
        self.__score = 0

    def affichage(self):
        """

              Cette fonction permet l'affichage d'un message au début de jeu
              PRE: -
              POST: affiche un message au commencement du Jeu
               """
        print("Bonne Jeu à vous")

    def utilisateur(self):
        return self.__utilisateur.pseudo

    def tableau_question_partie(self):
        return self.__partie.tableauquestion()

    def partie(self):
        """
        Une fonction qui récupère des questions par rapport à son thème
        PRE: -
        POST: Appel de la méthode theme et de recupQuestions qui composent une partie

        """
        self.__partie.theme()
        self.__partie.recupQuestions()

        Cela construit une une partie basée sur l utilisateur .
        PRE: Le nom , prenom , pseudo soient des strings
        POST:-

        """

    @property
    def get_utilisateur(self):
        return self.__utilisateur.get_pseudo

    @property
    def get_partie(self):
        return self.__partie.get_tableau_question()

    def set_partie(self):
        self.__partie.set_theme()
        self.__partie.recup_questions()


