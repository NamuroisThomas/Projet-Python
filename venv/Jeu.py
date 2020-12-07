class Jeu:



    def __init__(self,utilisateur,partie,score):

        self.__utilisateur = utilisateur
        self.__partie = partie
        self.__score = 0


    @property
    def user(self):
        return self.__utilisateur

    @property
    def partie(self):
        return self.__partie

    @property
    def score(self):
        return self.__score



