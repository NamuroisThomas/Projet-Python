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
        Cette fonction permet la vérification du thème entré
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
                numQuestion[1],
                numQuestion[2],
                numQuestion[3],
                numQuestion[4]
            )
            self.insertQuestion(ajout)

    def insertQuestion(self, question:Question):
        self.__tableauQuestion.append(question)

    def accesFichierQuestion(self):
        with open('../questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
        return question
"""""
    def lanceQuestion(self):
        score = 0
        question = self.accesFichierQuestion()
        for questions in question[self.__theme]:

            questions_demande = input(
                f"{questions[0]}{questions[1]}{questions[2]}{questions[3]}\n"
                f",veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
            # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
            if questions_demande == questions[4]:

                score += 1
                print(f"votre score est de {score} / {len(question[self.__theme])}")

            else:

                print("mauvaise réponse")
                print(f"la bonne réponse étais : {questions[4]}")
"""""
