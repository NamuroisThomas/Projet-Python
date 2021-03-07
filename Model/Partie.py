#! / usr / bin / env python
# - * - codage: utf-8 - * -

import json

from Model.Question import Question


class Partie:

    def __init__(self):
        self.__theme = ""
        self.__tableauQuestion = []

        """
        Cela construit une partie 
        PRE: -
        POST:-
        """

    def set_theme(self):

        """
        Cette fonction permet la vérification du thème entrée
        PRE: -
        POST:-

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

    @property
    def get_theme(self):
        return self.__theme

    def get_tableau_question(self):
        return self.__tableauQuestion


    def recup_questions(self):
        """
        Cette fonction permet la récupération des questions dans un fichier JSON
        """
        question = self.acces_fichier_question()
        # print(question.keys())

        try:

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
