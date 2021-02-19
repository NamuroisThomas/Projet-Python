from Utilisateur import Utilisateurs
from Partie import Partie


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
    def getUtilisateur(self):
        return self.__utilisateur.getPseudo

    @property
    def getPartie(self):
        return self.__partie.getTableauQuestion()

    def setPartie(self):
        self.__partie.setTheme()
        self.__partie.recupQuestions()

        """
        Une fonction qui récupère des questions par rapport à son thème
        PRE: -
        POST:-

        """


