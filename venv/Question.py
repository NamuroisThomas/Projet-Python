import json
import os


class Questions:

    def __init__(self,question,reponse):

        self.__question =question
        self.__reponse = reponse


    @property
    def question(self):
        return self.__question

    @property
    def reponse(self):
        return self.__reponse


    def question_de_Base():

        theme_quizz = {

    "geographie" : [["Quelle est la capitale de la Belgique ?: \n(a)Berlin\n(b)Sofia\n(c)Bruxelles\n\n",'c'],
                   ["Quel est le continent qui a la plus grande superficie ?:  \n(a)Europe\n(b)Asie\n(c)Afrique\n\n",'b'],
                   ],

    "informatique" :[["Que signifie DHCP ? : \n(a)Dynamic Host CPU Pipe\n(b)Dynamic Host Configuration Protocol\n(c)Domain Name System\n\n",'b'],
                   ["Un Spyware est un :  \n(a)Un virus\n(b)Un programme optimisant votre ordinateur\n(c)Un espio-logiciel\n\n",'c']],

    "histoire" :[["Quelle est l'année de la déclaration d'indépendance de la Belgique ? : \n(a)1830\n(b)1940\n(c)1257\n\n",'a'],
                   ["Quelle est l'année de la 1er Révolution Française ? : \n(a)2018\n(b)1789\n(c)1919\n\n",'b']]
        }



        try:
            with open('./questions/questions.json',"w") as fichier_questions :
                question_base = json.dump(theme_quizz,fichier_questions,indent=4,sort_keys=True)


        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

            return question_base


    def ajout_question(choix_theme,ma_question,ma_reponse):

        try:
            with open('./questions/questions.json') as fichier_question:
                question = json.load(fichier_question)
                #choix_theme = input("veuillez choisir entre les 3 thème suivant : geographie,informatique et histoire  : ")
                #ma_question = input("posez votre question : ")
                #ma_reponse = input("posez votre réponse : ")


                question[choix_theme].extend([[ma_question,ma_reponse]])



            with open('./questions/questions.json','w') as question_push:
                json.dump(question,question_push)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

        return question















