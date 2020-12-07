

class Questions:
    def __init__(self,question,reponse):

        self.__question =question
        self.__reponse = reponse



class Theme:

    def __init__(self,theme :str, questions ):

        self.__theme = theme
        self.__questions = questions

    @property
    def theme(self):
        return self.__theme

    @property
    def questions(self):
        return self.__questions


class User:

    def __init__(self, iduser:int, user:str, score:int):

        self.__iduser = iduser
        self.__user = user
        self.__score = score

    @property
    def iduser(self):
        return self.__iduser

    @property
    def user(self):
        return self.__user

    @property
    def score(self):
        return self.__score


class Partie:

    def __init__(self,idpartie : str,theme :str):

        self.__idpartie = idpartie
        self.__theme = theme


    @property
    def idpartie(self):
        return self.__idpartie

    @property
    def theme(self):
        return self.__theme


class Jeux:

    def __init__(self,user,partie):

        self.__user = user
        self.__partie = partie

    @property

    def user(self):
        return self.__user

    @property
    def partie(self):
        return self.__partie
