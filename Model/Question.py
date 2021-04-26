import json


class Question:

    def __init__(self, question: str, reponse: str):
        self.__question = question
        self.__reponse = reponse

    def question(self):
        return self.__question

    def reponse(self):
        return self.__reponse

    def ajout_question(choix_theme: str, ma_question: str, ma_reponse: str):
        """
        Cette fonction permet ajouter une question dans le fichier questions.json
        PRE: choix_theme,ma_question,proposition et ma_reponse sont des strings
        POST:Le fichier de questions questions.json est modifiée et contient la nouvelle question et sa réponse
        """

        try:
            with open('../questions/questions.json', encoding="utf-8") as fichier_question:
                question = json.load(fichier_question)

                question[choix_theme].extend([[ma_question, ma_reponse]])

            with open('../questions/questions.json', 'w') as question_push:
                json.dump(question, question_push)

        except FileNotFoundError:
            print('Fichier introuvable.')

        except IOError:
            print('Erreur IO.')

        return question
