import json

from Model.Question import Question


class Partie:

    def __init__(self):
        self.__theme = ""
        self.__tableauQuestion = []

        """
        Cela construit une partie par apport a son thème et ses questions
        PRE: -
        POST:-
        """

    def setTheme(self):

        """
        Cette fonction permet la vérification du thème entrée
        PRE: -
        POST:-

        """
        valide = False
        question = self.accesFichierQuestion()
        while not valide:
            choix_theme = input("Veuillez choisir entre les 3 thèmes suivant: geographie, informatique et histoire:")
            if choix_theme in question.keys():
                self.__theme = choix_theme
                valide = True
            else:
                print("Insertion invalide")

    @property
    def getTheme(self):
        return self.__theme

    def getTableauQuestion(self):
        return self.__tableauQuestion

    def recupQuestions(self):
        question = self.accesFichierQuestion()
        #print(question.keys())

        for numQuestion in question[self.__theme]:
            ajout = Question(
                numQuestion[0],
                numQuestion[1]
            )
            self.insertQuestion(ajout)

    def insertQuestion(self, question:Question):
        self.__tableauQuestion.append(question)

    def accesFichierQuestion(self):
        """
        Cette fonction permet accéder au questions
        PRE: -
        POST:renvoie le dictionnaire de questions

        """

        with open('../questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
        return question
