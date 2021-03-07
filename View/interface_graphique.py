#! / usr / bin / env python
# - * - codage: utf-8 - * -


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from Model import Partie
from Model import Question
from Model import Utilisateur


class Acceuil(Screen):
    pass


class SauvegardeJoueur(Screen):

    def voir_info(self):
        nom = self.ids.nom.text
        prenom = self.ids.prenom.text
        pseudo = self.ids.pseudo.text

        sauvegarde = Utilisateur.Utilisateurs.sauvegarde_utilisateur(self, nom, prenom, pseudo)

        return sauvegarde


class Theme(Screen):
    pass


class Histoire(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_histoire
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.acces_fichier_question(self)
        # accede au fichier de questions

        self.theme = "histoire"
        # le thème choisis

        self.nombre_Questions = []
        # ce tableau me permetteras de rajouter les questions qui permettras de definir la taille du score

        self.verifications = []
        # ce tableau me permetteras de rajouter les réponses de mes inputs

        self.score = 0

        for mes_questions in self.fichier_question[self.theme]:
            self.demande_question_label = Label(text=mes_questions[0])
            # un label qui affiche la question

            self.demande_reponse_textinput = TextInput(multiline=False)
            # un textinput qui recois les questions

            self.nombre_Questions.append(self.demande_question_label)

            self.bouton_validation = Button(text="Validation")
            self.bouton_validation.bind(on_press=self.verification)

            zone_questions_reponses.add_widget(self.demande_question_label)
            # Ajout de label avec les questions
            zone_questions_reponses.add_widget(self.demande_reponse_textinput)
            # Ajout des textinput pour les réponses

        zone_questions_reponses.add_widget(self.bouton_validation)
        # Ajout du boutton de validation

        return zone_questions_reponses

    def verification(self, text):

        for child in reversed(self.ids.zone_questions_histoire.children):  # Parcours les enfants du Boxlayout

            if len(child.text) == 1 or child.text == '':  # Seul les réponses sont prises

                self.verifications.append(child.text)

            else:
                print("Ce sont les questions ou le boutton")
            print(self.verifications)

        for index, reponse in enumerate(self.fichier_question[self.theme]):
            print(reponse[1])

            if self.verifications[index] == reponse[1]:
                print("ok")
                self.score += 1
            else:
                print("Mauvaise réponse")

        print(self.score)

        le_score = Label(
            text=f"Votre score pour le thème : {self.theme} est de {self.score} / {len(self.nombre_Questions)}")

        self.ids.zone_questions_histoire.clear_widgets()
        self.ids.zone_questions_histoire.add_widget(le_score)

        bouton_ajout_question = Button(text='Ajouter une question ? : ', on_release=self.ajout_question,

                                       background_color=(0.1, 0.5, 0.6, 1),
                                       color=(50, 50, 50, 50),
                                       size=(15, 15),
                                       size_hint=(.2, .2),
                                       pos=(400, 250))

        self.ids.zone_questions_histoire.add_widget(bouton_ajout_question)

    def ajout_question(self, item):

        self.manager.transition.direction = 'up'
        self.manager.transition.duration = 3  # 3 seconds
        self.manager.current = 'AjoutQuestion'


class Geographie(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_geographie
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.acces_fichier_question(self)
        # accede au fichier de questions

        self.theme = "geographie"
        # le thème choisis

        self.nombre_Questions = []
        # ce tableau me permetteras de rajouter les questions qui permettras de definir la taille du score

        self.verifications = []
        # ce tableau me permetteras de rajouter les réponses de mes inputs

        self.score = 0

        for mes_questions in self.fichier_question[self.theme]:
            self.demande_question_label = Label(text=mes_questions[0])
            # un label qui affiche la question

            self.demande_reponse_textinput = TextInput(multiline=False)
            # un textinput qui recois les questions

            self.nombre_Questions.append(self.demande_question_label)

            self.bouton_validation = Button(text="Validation")
            self.bouton_validation.bind(on_press=self.verification)

            zone_questions_reponses.add_widget(self.demande_question_label)
            # Ajout de label avec les questions
            zone_questions_reponses.add_widget(self.demande_reponse_textinput)
            # Ajout des textinput pour les réponses

        zone_questions_reponses.add_widget(self.bouton_validation)
        # Ajout du boutton de validation

        return zone_questions_reponses

    def verification(self, text):

        for child in reversed(self.ids.zone_questions_geographie.children):  # Parcours les enfants du Boxlayout

            if len(child.text) == 1 or child.text == '':  # Seul les réponses sont prises

                self.verifications.append(child.text)

            else:
                print("Ce sont les questions ou le boutton")
            print(self.verifications)

        for index, reponse in enumerate(self.fichier_question[self.theme]):
            print(reponse[1])

            if self.verifications[index] == reponse[1]:
                print("ok")
                self.score += 1
            else:
                print("Mauvaise réponse")

        print(self.score)

        le_score = Label(
            text=f"Votre score pour le thème : {self.theme} est de {self.score} / {len(self.nombre_Questions)}")

        self.ids.zone_questions_geographie.clear_widgets()
        self.ids.zone_questions_geographie.add_widget(le_score)

        bouton_ajout_question = Button(text='Ajouter une question ? : ', on_release=self.ajout_question,

                                       background_color=(0.1, 0.5, 0.6, 1),
                                       color=(50, 50, 50, 50),
                                       size=(15, 15),
                                       size_hint=(.2, .2),
                                       pos=(400, 250))

        self.ids.zone_questions_geographie.add_widget(bouton_ajout_question)

    def ajout_question(self, item):

        self.manager.transition.direction = 'up'
        self.manager.transition.duration = 3  # 3 seconds
        self.manager.current = 'AjoutQuestion'


class Informatique(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_informatique
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.acces_fichier_question(self)
        # accede au fichier de questions

        self.theme = "informatique"
        # le thème choisis

        self.nombre_Questions = []
        # ce tableau me permetteras de rajouter les questions qui permettras de definir la taille du score

        self.verifications = []
        # ce tableau me permetteras de rajouter les réponses de mes inputs

        self.score = 0

        for mes_questions in self.fichier_question[self.theme]:
            self.demande_question_label = Label(text=mes_questions[0])
            # un label qui affiche la question

            self.demande_reponse_textinput = TextInput(multiline=False)
            # un textinput qui recois les questions

            self.nombre_Questions.append(self.demande_question_label)

            self.bouton_validation = Button(text="Validation")
            self.bouton_validation.bind(on_press=self.verification)

            zone_questions_reponses.add_widget(self.demande_question_label)
            # Ajout de label avec les questions
            zone_questions_reponses.add_widget(self.demande_reponse_textinput)
            # Ajout des textinput pour les réponses

        zone_questions_reponses.add_widget(self.bouton_validation)
        # Ajout du boutton de validation

        return zone_questions_reponses

    def verification(self, text):

        for child in reversed(self.ids.zone_questions_informatique.children):  # Parcours les enfants du Boxlayout

            if len(child.text) == 1 or child.text == '':  # Seul les réponses sont prises

                self.verifications.append(child.text)

            else:
                print("Ce sont les questions ou le boutton")
            print(self.verifications)

        for index, reponse in enumerate(self.fichier_question[self.theme]):
            print(reponse[1])

            if self.verifications[index] == reponse[1]:
                print("ok")
                self.score += 1
            else:
                print("Mauvaise réponse")

        print(self.score)

        le_score = Label(
            text=f"Votre score pour le thème : {self.theme} est de {self.score} / {len(self.nombre_Questions)}",
            pos=[0, 0],
            size_hint=[1, 1])

        self.ids.zone_questions_informatique.clear_widgets()
        self.ids.zone_questions_informatique.add_widget(le_score)

        bouton_ajout_question = Button(text='Ajouter une question ? : ',
                                       on_release=self.ajout_question,
                                       pos_hint={'x': .3, 'y': .6},
                                       size_hint=(.5, .2)

                                       )

        self.ids.zone_questions_informatique.add_widget(bouton_ajout_question)

    def ajout_question(self, item):

        self.manager.transition.direction = 'up'
        self.manager.transition.duration = 3  # 3 seconds
        self.manager.current = 'AjoutQuestion'


class AjoutQuestion(Screen):

    def ajout_question(self):
        theme = self.ids.theme.text
        print(theme)
        question = self.ids.Question.text
        print(question)
        reponse = self.ids.Reponse.text
        print(reponse)

        return Question.Question.ajout_question(theme, question, reponse)


class WindowManager(ScreenManager):
    pass


class MyMainApp(App):

    def build(self):
        return Builder.load_file(
            'C:\\Users\\Gros\\Documents\\Développement informatique II\\Projet-Python\\View\\interface_graphique_kivy.kv',
            encoding='utf8')


def start_gui():
    MyMainApp().run()


if __name__ == "__main__":
    start_gui()
