from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import Utilisateur
import json
import Question




class Demarrage(App):
    def build(self):
        """
         self.title = 'Quizz'

        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="Bienvenue Au quizz générale"))

        self.commencer = Button(text="Commencer",font_size=40)
        self.commencer.bind(on_press=self.renseignement)
        box.add_widget(self.commencer)

        return box,Renseignement()

        :return:
        """
        return Renseignement()

    def renseignement(self,instance):
        print("Ne marche pas")
        return Renseignement()






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



def demarrage_interface():
    Demarrage().run()

    #Renseignement().run()
    #Ajout_Question().run()



