from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner

import Utilisateur
import json
import Question


class Quizz(App):
    def build(self):

        self.title = "Quizz Générale"
        self.quizz = BoxLayout(orientation='vertical')
        message_bienvenue = Label(text='Bienvenue à tous')
        self.quizz.add_widget(message_bienvenue)



        lancer = Button(text="commencer Partie",background_color=(155,0,51,53))
        lancer.bind(on_press=self.commencer)
        self.quizz.add_widget(lancer)

        renseignement = Button(text="Enregistrer vos données",background_color=(128,0, 128, 255))
        renseignement.bind(on_press=self.renseignement)
        self.quizz.add_widget(renseignement)

        ajout_question = Button(text="Ajouter Question",background_color=(128,0, 128, 255))
        ajout_question.bind(on_press=self.ajout_Question)
        self.quizz.add_widget(ajout_question)


        return self.quizz


    def ajout_Question(self,instance):

        with open('./questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
            print(question)

        self.quizz.add_widget(Label(text='Choisissez un Thème : '))
        self.theme = TextInput(text="")
        self.quizz.add_widget(self.theme)


        self.quizz.add_widget(Label(text = "Question :  "))
        self.question = TextInput(text="")
        self.quizz.add_widget(self.question)

        self.quizz.add_widget(Label(text = "Réponse"))
        self.reponse = TextInput(text="")
        self.quizz.add_widget(self.reponse)

        self.ajout = Button(text="ajouter",font_size=40)#un bouton avec un text et une taille
        self.ajout.bind(on_press=self.ajout_nouvelle_question)#à l'evenement presse , j'apelle une méthode valider
        self.quizz.add_widget(self.ajout)#rajouter le bouton

    def ajout_nouvelle_question(self,instance):

        Question.Questions.ajout_question(self.theme.text,self.question.text,self.reponse.text)








    def renseignement(self,instance):

        self.quizz.add_widget(Label(text = "Nom : "))#simplement une case qui affiche un message
        self.nom = TextInput(text="")#un input dans lequel je peut insérer mes données
        self.quizz.add_widget(self.nom)#rajoute le Textinput dans la 2ème colonne

        self.quizz.add_widget(Label(text = "Prénom : "))
        self.prenom = TextInput(text="")
        self.quizz.add_widget(self.prenom)

        self.quizz.add_widget(Label(text = "Pseudo : "))
        self.utilisateur = TextInput(text="")
        self.quizz.add_widget(self.utilisateur)

        self.envoy = Button(text="envoie",font_size=40)#un boutonde avec un nom et une taille
        self.envoy.bind(on_press=self.valider)#à l'evenement presse , j'apelle une méthode valider

        self.quizz.add_widget(self.envoy)#rajouter le bouton


    def valider(self,instance):


        nom = self.nom.text#texte me permet de récuper la valeur d'un input
        prenom = self.prenom.text
        utilisateur = self.utilisateur.text

        print(f"votre nom : {nom} et Prénom : {prenom} , pseudo {utilisateur}")

        Utilisateur.utilisateur.sauvegarde_utilisateur(nom,prenom,utilisateur)


    def commencer(self,instance):

        self.quizz.add_widget(Label(text='Choisissez un Thème : '))
        spinner = Spinner(text="Les thèmes ",
        values = ('geographie','histoire','informatique'))
        self.quizz.add_widget(spinner)

        self.spinnerSelectionner = Label(text=f"le thème sélectioné est {spinner}")

        spinner.bind(text=self.spinner_selectionner_valeur)

        return self.quizz

    def spinner_selectionner_valeur(self,spinner,text):

        with open('./questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)

            self.question = question
            self.score = 0
            self.mauvaise = []

            for theme in question.keys():#je parcours les thèmes
                if text == theme:
                    self.theme = text

                    for mes_questions in question[text]:
                        self.nombre_question = mes_questions

                        self.mes_question = mes_questions[0]#je crée cette méthode pour l'utiliser dans une autre fonction
                        self.reponse = mes_questions[1]



                        self.demande_question = Spinner(text = mes_questions[0],values=('a','b','c'))#permet de crée une liste avec les réponses à la question
                        self.quizz.add_widget(self.demande_question)#j'ajoute ma liste déroulante

                        self.validation_reponse = Button(text="Valider mes réponses")
                        self.validation_reponse.bind(on_press=self.validation)
                        self.quizz.add_widget(self.validation_reponse)

                    self.voir_score = Button(text="Score")
                    self.voir_score.bind(on_press=self.voir_mon_score)
                    self.quizz.add_widget(self.voir_score)

            return self.quizz

    def validation(self,instance):

        if self.demande_question.text == self.reponse:

            print("yo")
            self.score +=1
            print(self.score)


        else:

            print("mauvais")


        return f"{self.score} /  {len(self.nombre_question)}"

    def voir_mon_score(self,instance):
        self.quizz.add_widget(Label(text=f"{self.score} /  {len(self.nombre_question)}"))


def demarrage_interface():

    Quizz().run()
    #Ajout_Question()



















"""
class Renseignement(GridLayout):
    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)
        self.cols = 2 #ma page est divisé en deux colonne

        self.add_widget(Label(text = "Nom : "))#simplement une case qui affiche un message
        self.nom = TextInput(text="")#un input dans lequel je peut insérer mes données
        self.add_widget(self.nom)#rajoute le Textinput dans la 2ème colonne

        self.add_widget(Label(text = "Prénom : "))
        self.prenom = TextInput(text="")
        self.add_widget(self.prenom)

        self.add_widget(Label(text = "Pseudo : "))
        self.pseudo = TextInput(text="")
        self.add_widget(self.pseudo)

        self.envoy = Button(text="envoie",font_size=40)#un boutonde avec un nom et une taille
        self.envoy.bind(on_press=self.valider)#à l'evenement presse , j'apelle une méthode valider

        self.add_widget(self.envoy)#rajouter le bouton


    def valider(self,instance):


        nom = self.nom.text#texte me permet de récuper la valeur d'un input
        prenom = self.prenom.text
        pseudo = self.pseudo.text

        print(f"votre nom : {nom} et Prénom : {prenom} , pseudo {pseudo}")

        Utilisateur.utilisateur.sauvegarde_utilisateur(nom,prenom,pseudo)














class Ajout_Question(GridLayout):

    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)
        self.cols = 2 #ma page est divisé en deux colonne

        with open('./questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
            print(question)

        self.add_widget(Label(text = "Dans Quelle thème ? : "))#simplement une case qui affiche un message
        self.theme = TextInput(text="")#un input dans lequel je peut insérer mes données
        self.add_widget(self.theme)#rajoute le Textinput dans la 2ème colonne


        self.add_widget(Label(text = "Question :  "))
        self.question = TextInput(text="")
        self.add_widget(self.question)

        self.add_widget(Label(text = "Réponse"))
        self.reponse = TextInput(text="")
        self.add_widget(self.reponse)

        self.ajout = Button(text="ajouter",font_size=40)#un boutonde avec un nom et une taille
        self.ajout.bind(on_press=self.ajout_nouvelle_question)#à l'evenement presse , j'apelle une méthode valider
        self.add_widget(self.ajout)#rajouter le bouton

    def ajout_nouvelle_question(self,instance):

        theme = self.theme.text
        question = self.question.text
        reponse = self.reponse.text

        print(f"Pour ce thème {theme} , vous avez ajouter cette question : {question} et sa réponse : {reponse}")

        Question.Questions.ajout_question(theme,question,reponse)


"""










