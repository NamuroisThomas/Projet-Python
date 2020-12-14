import json
class Question:


    def __init__(self, question:str, reponseA:str, reponseB:str, reponseC:str, reponse:str):
        self.__question = question
        self.__reponseA = reponseA
        self.__reponseB = reponseB
        self.__reponseC = reponseC
        self.__reponse = reponse

        """
        Cela construit les questions sous formes d'un tableau
        PRE: question:, reponseA, reponseB, reponseC, reponse sont des strings
        POST:-
        """

    def getQuestion(self):
        return self.__question
    def getReponseA(self):
        return self.__reponseA
    def getReponseB(self):
        return self.__reponseB
    def getReponseC(self):
        return self.__reponseC
    def getReponse(self):
        return self.__reponse

    def ajout_question( choix_theme : str   ,ma_question : str, proposition1 : str, proposition2 : str , proposition3 : str ,ma_reponse : str   ):
        """
        Cette fonction permet ajouter une question
        PRE: choix_theme,ma_question,proposition et ma_reponse sont des strings
        POST:renvoie un dictionnaire avec la nouvelle question
        """

        try:
            with open('../questions/questions.json',encoding="utf-8") as fichier_question:
                question = json.load(fichier_question)

                question[choix_theme].extend([[ma_question,proposition1,proposition2,proposition3,ma_reponse]])



            with open('../questions/questions.json','w') as question_push:
                json.dump(question,question_push)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

        return question
