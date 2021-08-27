from Model.Partie import Partie
from Model.Utilisateur import Utilisateurs, Utilisatrices


class Jeu(Partie, Utilisateurs):

    def __init__(self, nom: str, prenom: str, pseudo: str):
        Utilisateurs.__init__(self, nom, prenom, pseudo)
        self.__partie = Partie()

    def affichage(self):
        """
              Cette fonction permet l'affichage d'un message au début de jeu
              PRE: -
              POST: affiche un message au commencement du Jeu
               """
        return "Bon Jeu à vous"

    def utilisateur(self):
        return self.pseudo

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
