#! / usr / bin / env python
# - * - codage: utf-8 - * -


import Model.Question
import Model.Utilisateur
import View.interface_graphique as gui
from Model.Jeu import Jeu


def choix_interface():
    """
    Cette fonction permet de choisir entre la Console ou Gui
    """
    demande_choix = input("Choisissez votre interface (Console ou Gui) : ")

    try:
        if demande_choix == "Console":
            commencer_jeu()

        elif demande_choix == "GUI":
            gui.start_gui()
        else:
            print("Choix invalide recommencer")
            return choix_interface()
    except Exception as e:
        print("Erreur au dans le choix interfaces")
        return e


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

    return jouer(nom, prenom, pseudo)


def jouer(nom, prenom, pseudo):
    print(f" {pseudo},Bonne partie ")

    """
    Cette fonction est le Quizz et la sauvegarde du Joueur

    :param nom: Nom du joueur
    :param prenom: Prénom du joueur
    :param pseudo: Pseudo du joueur
    :return: - 
    """

    jeu = Jeu(nom, prenom, pseudo)
    # me permet instance la classe jEux les renseignement au jeu , qui ensuite seront utile à la partie
    jeu.set_partie()
    # cette méthode de jeu me permet de d'appleler 1)setTheme() qui demande le thème et 2)recupQuestions()

    score = 0
    for questions in jeu.get_partie:  # parcours le tableau de questions

        questions_demande = input(
            f"{questions.get_question()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")
        # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant

        if questions_demande == questions.get_reponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {questions.get_question()}")

    print(f"votre score est de {score} / {len(jeu.get_partie)}")

    ajouter_question = input("voulez vous ajoutez une question ? oui ou non :")
    if ajouter_question == "oui":
        ajout_question()

    else:
        quit()


def ajout_question():
    """
    Cette fonction permet l'ajout d'une question à un thème précis
    """
    theme = input("Dans quelle thème voulez-vous l'ajouter ? : ")
    question = input("Quelle question voulez-vous ajouter ainsi que ses propositions ? : ")
    reponse = input("Quelle est la lettre correspondants à la question ? : ")

    Model.Question.Question.ajout_question(theme, question, reponse)


if __name__ == "__main__":
    choix_interface()
    # commencer_jeu()
    # jouer()
