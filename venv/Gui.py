
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner

import Model.Utilisateurs
import json
import Model.Question
import Model.Partie
import Presenter.Controle
from Model.JEux import JEux


class Quizz(App):
    def build(self):


        self.title = "Quizz Générale"
        self.quizz = BoxLayout(orientation='vertical')
        message_bienvenue = Label(text='Bienvenue à tous')
        self.quizz.add_widget(message_bienvenue)



        lancer = Button(text="commencer Partie",background_color=(155,0,51,53))
        lancer.bind(on_press=self.commencer)
        self.quizz.add_widget(lancer)



        ajout_question = Button(text="Ajouter Question",background_color=(128,0, 128, 255))
        ajout_question.bind(on_press=self.ajout_Question)
        self.quizz.add_widget(ajout_question)


        return self.quizz


    def ajout_Question(self,instance):

        with open('../questions/questions.json') as json_question:
            test = json.load(json_question)
            question = dict(test)
            print(question)

        self.quizz.add_widget(Label(text='Choisissez un Thème : '))
        self.theme = TextInput(text="")
        self.quizz.add_widget(self.theme)

        self.quizz.add_widget(Label(text = "Question :  "))
        self.question = TextInput(text="")
        self.quizz.add_widget(self.question)


        self.quizz.add_widget(Label(text = "Première proposition :  "))
        self.proposition1 = TextInput(text="")
        self.quizz.add_widget(self.proposition1)

        self.quizz.add_widget(Label(text = "Deuxième proposition :  "))
        self.proposition2 = TextInput(text="")
        self.quizz.add_widget(self.proposition2)

        self.quizz.add_widget(Label(text = "Troisième proposition  "))
        self.proposition3 = TextInput(text="")
        self.quizz.add_widget(self.proposition3)

        self.quizz.add_widget(Label(text = "Réponse"))
        self.reponse = TextInput(text="")
        self.quizz.add_widget(self.reponse)

        self.ajout = Button(text="ajouter",font_size=40)#un bouton avec un text et une taille
        self.ajout.bind(on_press=self.ajout_nouvelle_question)#à l'evenement presse , j'apelle une méthode valider
        self.quizz.add_widget(self.ajout)#rajouter le bouton

    def ajout_nouvelle_question(self,instance):

        Question.Question.ajout_question(self.theme.text,self.question.text,self.proposition1.text,self.proposition2.text,self.proposition3.text,self.reponse.text)








    def commencer(self,instance):

        self.quizz.add_widget(Label(text = "Nom : "))#simplement une case qui affiche un message
        self.nom = TextInput(text="")#un input dans lequel je peut insérer mes données
        self.quizz.add_widget(self.nom)#rajoute le Textinput dans la 2ème colonne

        self.quizz.add_widget(Label(text = "Prénom : "))
        self.prenom = TextInput(text="")
        self.quizz.add_widget(self.prenom)

        self.quizz.add_widget(Label(text = "Pseudo : "))
        self.pseudo = TextInput(text="")
        self.quizz.add_widget(self.pseudo)

        self.envoy = Button(text="envoie",font_size=40)#un boutonde avec un nom et une taille
        self.envoy.bind(on_press=self.valider)#à l'evenement presse , j'apelle une méthode valider

        self.quizz.add_widget(self.envoy)#rajouter le bouton


    def valider(self,instance):


        nom = self.nom.text#texte me permet de récuper la valeur d'un input
        prenom = self.prenom.text
        pseudo = self.pseudo.text

        print(f"votre nom : {nom} et Prénom : {prenom} , pseudo {pseudo}")

        if nom and prenom and pseudo == "" :
            print("champs vides")

        else:
            Model.Utilisateurs.Utilisateurs.sauvegarde_utilisateur(nom,prenom,pseudo)
            return self.jouer() #Presenter.Controle.jouer(nom,prenom,pseudo),


    def jouer(self):
        self.score = 0


        self.quizz.add_widget(Label(text='Choisissez un Thème : '))
        spinner = Spinner(text="Les thèmes ",
        values = ('geographie','histoire','informatique'))
        self.quizz.add_widget(spinner)

        self.spinnerSelectionner = Label(text=f"le thème sélectioné est {spinner}")

        spinner.bind(text=self.spinner_selectionner_valeur)

        return self.quizz

    def spinner_selectionner_valeur(self,spinner,text):
        fichier_question = Model.Partie.Partie.accesFichierQuestion(self)

        self.taille_question = []

        for theme in fichier_question.keys():
            if text == theme:

                for ma_question in fichier_question[text]:
                    demande_question = Spinner(text=f"{ma_question[0]}{ma_question[1]},{ma_question[2]},{ma_question[3]},veuillez choisir la lettres correspondante.",

                                                    font_size ="15sp",
                                                    values=('a','b','c')
                                                    )
                    self.reponse = ma_question[-1]
                    self.taille_question.append(ma_question[0])

                    self.quizz.add_widget(demande_question)
                    demande_question.bind(text=self.validation)



    def validation(self,demande_question,text):


        if text == self.reponse:
            self.score += 1
            print(self.score)

        else:
            print("Mauvaise réponse")


        return self.quizz.add_widget(Label(text=f"{self.score} / {len(self.taille_question)}"))





def demarrage_interface():

    Quizz().run()
    #Ajout_Question()


