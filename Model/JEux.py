from Model.Utilisateurs import Utilisateurs
from Model.Partie import Partie


class JEux:

    def __init__(self, nom: str, prenom: str, pseudo: str):
        self.__utilisateur = Utilisateurs(nom, prenom, pseudo)
        self.__partie = Partie()
        self.__score = 0

    @property
    def getUtilisateur(self):
        return self.__utilisateur.getPseudo

    @property
    def getPartie(self):
        info = self.__partie.getTableauQuestion()
        return info



    def setPartie(self):
        self.__partie.setTheme()
        self.__partie.recupQuestions()