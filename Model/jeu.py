from Model.Utilisateurs import Utilisateurs
from Model.Partie import Partie


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
    def getutilisateur(self):
        return self.__utilisateur.getpseudo

    @property
    def getpartie(self):
        return self.__partie.getableauquestion()

    def setpartie(self):
        self.__partie.settheme()
        self.__partie.recupquestions()

        """
        Une fonction qui récupère des questions par rapport à son thème
        PRE: -
        POST:-
        
        """
