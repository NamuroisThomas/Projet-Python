from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from Model import Partie
from Model import Utilisateur


class Acceuil(Screen):
    pass


class SauvegardeJoueur(Screen):

    def voir_info(self):

        nom = self.ids.nom.text
        prenom = self.ids.prenom.text
        pseudo = self.ids.pseudo.text


        Utilisateur.Utilisateurs.sauvegarde_utilisateur(nom,prenom,pseudo)




class Theme(Screen):
    pass


class Histoire(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_histoire
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.accesFichierQuestion(self)
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


class Geographie(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_geographie
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.accesFichierQuestion(self)
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


class Informatique(Screen):

    def lancement_question(self):

        zone_questions_reponses = self.ids.zone_questions_informatique
        # Cette variable me permet d'accéder au Boxlayout ou seront afficher

        zone_questions_reponses.clear_widgets()
        # Nettoie tout les widget de mon Boxlayout

        self.fichier_question = Partie.Partie.accesFichierQuestion(self)
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
            text=f"Votre score pour le thème : {self.theme} est de {self.score} / {len(self.nombre_Questions)}")

        self.ids.zone_questions_informatique.clear_widgets()
        self.ids.zone_questions_informatique.add_widget(le_score)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('interface_graphique.kv')


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
