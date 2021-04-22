#! / usr / bin / env python
# - * - codage: utf-8 - * -

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
        POST: Le thème valider le quizz peut continuer
        """
        valide = False
        question = self.acces_fichier_question()
        while not valide:

            try:
                choix_theme = input(
                    "Veuillez choisir entre les 3 thèmes suivant: geographie, informatique et histoire:")
                if choix_theme in question.keys():
                    self.__theme = choix_theme
                    valide = True
                else:
                    print("Insertion invalide")

            except TypeError:
                print("Le type du input est mauvais , seulement des strings")
                continue  # This causes it to continue
            except EOFError:
                print("Il n'y a pas de données ")
                continue  # This causes it to continue


    def le_theme(self):
        return self.__theme

    def tableauquestion(self):
        return self.__tableauQuestion

    def recupQuestions(self):

        """
        Cette fonction permet la récupération des questions
       PRE: -
       POST:Permet de récupérer les questions d'un thème précis
        """
        question = self.accesFichierQuestion()


    def recup_questions(self):
        """
        Cette fonction permet la récupération des questions dans un fichier JSON
        """
        question = self.acces_fichier_question()

        # print(question.keys())

        try:


    def insertQuestion(self, question: Question):

        """
        Cette fonction permet de stocker les questions d'un thème

      PRE: les questions sont des tableaux .
      POST: les questions et leur réponse sont stocker dans un tableau
       """


            for numQuestion in question[self.__theme]:
                ajout = Question(
                    numQuestion[0],
                    numQuestion[1]
                )
                self.insert_question(ajout)

        except KeyError:
            print("La clés qui représente le thème est n'existe pas")

    def insert_question(self, question: Question):
        """
        Cette fonction permet de rajouter les questions dans un tableau
        :param question: les questions à ajouter dans le tableau tableauQuestion
        :return: -
        """

        self.__tableauQuestion.append(question)

    def acces_fichier_question(self):
        """
        Cette fonction permet accéder au questions
        PRE: -
        POST:renvoie le dictionnaire de questions
        """

        with open('../questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
        return question
