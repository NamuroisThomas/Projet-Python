#! / usr / bin / env python
# - * - codage: utf-8 - * -

from Model.Partie import Partie
from Model.Utilisateur import Utilisateurs


class Jeu:

    def __init__(self, nom: str, prenom: str, pseudo: str):
        self.__utilisateur = Utilisateurs(nom, prenom, pseudo)
        self.__partie = Partie()
        self.__score = 0

        """
        Cela construit une partie basée sur un utilisateur , sa partie,son score
        PRE: utilisateur est une appelle une autre classe , la partie est aussi un appelle,et le score est un entier
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

        """
        Une fonction qui récupère des questions par rapport à son thème
        PRE: -
        POST:-

        """
