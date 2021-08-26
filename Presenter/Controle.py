#! / usr / bin / env python
# - * - codage: utf-8 - * -


import View.interface_graphique as gui
from Model.Jeu import Jeu
from Model.Partie import Partie
from Model.Question import Question
from Model.Utilisateur import *


def choix_interface():
    """
    Cette fonction permet de choisir entre la Console ou Gui
    """
    demande_choix = input("Choisissez votre interface (Console ou GUI) : ")

    if demande_choix == "Console":
        return commencer_jeu()

    elif demande_choix == "GUI":
        return gui.start_gui()


def commencer_jeu():
    """
    Cette fonction permet de récupérer les données du joueur

    :return: La fonction qui lance le Quizz
    """

    message_bienvenu = "Bienvenue dans notre Quizz Générale "
    print(message_bienvenu)

    nom = input("Veuillez donner votre Nom :")
    prenom = input("Veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")

    sexe = input("Vous êtes un homme ou une femme ? -> un homme taper = H et -> une femme = F : ")

    if sexe == 'H':

        # utilisateur = Utilisateurs(nom, prenom, pseudo)
        # utilisateur.sauvegarde_utilisateur()
        # utilisateur.ajout_id()

        lancement = Jeu(nom, prenom, pseudo)
        lancement.sauvegarde_utilisateur()
        print(lancement.pseudo)
        lancement.ajout_id()

        return jouer(lancement.nom, lancement.prenom, lancement.pseudo)

    elif sexe == 'F':

        utilisatrices = Utilisatrices(nom, prenom, pseudo)
        utilisatrices.sauvegarde_utilisateur()
        utilisatrices.ajout_id()

        return jouer(utilisatrices.nom, utilisatrices.prenom, utilisatrices.pseudo)


def jouer(nom, prenom, pseudo):
    # print(f" {pseudo},Bonne partie ")

    jeu = Jeu(nom, prenom, pseudo)
    jeu.affichage()

    """
    Cette fonction est le Quizz et la sauvegarde du Joueur

    :param nom: Nom du joueur
    :param prenom: Prénom du joueur
    :param pseudo: Pseudo du joueur
    :return: - 
    """

    # me permet instance la classe Jeu les renseignement au jeu , qui ensuite seront utile à la partie
    jeu.partie()
    # cette méthode de jeu me permet de d'appleler 1)setTheme() qui demande le thème et 2)recupQuestions()
    score = 0

    Partie().affichage()
    for questions in jeu.tableau_question_partie():  # parcours le tableau de questions

        questions_demande = input(
            f"{questions.question()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")
        # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant

        if questions_demande == questions.reponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse ")
            print(f"la bonne réponse étais : {questions.question()}")

    print(f"votre score est de {score} / {len(jeu.tableau_question_partie())}")

    ajouter_question = input("voulez vous ajoutez une question ? oui ou non :")
    if ajouter_question == "oui":
        ajout_question()

    else:
        quit()


def ajout_question():
    """
    Cette fonction permet l'ajout d'une question et de sa répondre dans un thème
    """
    theme = input("Dans quelle thème voulez-vous l'ajouter ? : ")
    question = input("Quelle question voulez-vous ajouter ainsi que ses propositions ? : ")
    reponse = input("Quelle est la lettre correspondants à la question ? : ")

    Question(question, reponse).ajout_question(theme, question, reponse)


if __name__ == "__main__":
    # gestion_erreur()
    choix_interface()
    # commencer_jeu()
    # jouer()
