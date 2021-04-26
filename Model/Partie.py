import json

from Model.Question import Question


class Partie:

    def __init__(self):
        self.__theme = ""
        self.__tableauQuestion = []

    def affichage(self):
        """
       Cette fonction permet l'affichage d'un message au début de partie
       PRE: -
       POST: affiche une message au commencement de partie.
        """

        print("Bonne Partie à vous")

    def theme(self):

        """
        Cette fonction  permet la vérification du thème entrée
        PRE: -
        POST: Le thème à valider et le quizz peut continuer
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

    def le_theme(self):
        return self.__theme

    def tableauquestion(self):
        return self.__tableauQuestion

    def recupQuestions(self):

        """
        Cette fonction permet la récupération des questions
        PRE: -
        POST: Le fichier de questions questions.json est parcouru et les questions
        liée au thème sont stocker dans un tableau
        """
        question = self.accesFichierQuestion()
        # print(question.keys())

        for numQuestion in question[self.__theme]:
            ajout = Question(
                numQuestion[0],
                numQuestion[1]
            )
            self.insertQuestion(ajout)

    def insertQuestion(self, question: Question):

        """
        Cette fonction permet de stocker les questions d'un thème
        PRE: Les questions sont des tableaux
        POST: les questions et leurs réponse sont stocker dans un tableau centrale au thème
       """

        self.__tableauQuestion.append(question)

    def accesFichierQuestion(self):
        """
        Cette fonction permet accéder au questions
        PRE: -
        POST:renvoie le contenue du fichier questions.json qui est un dictionnaire
        """

        with open('../questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
        return question
