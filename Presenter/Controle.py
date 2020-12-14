import threading
from Model.JEux import JEux
import Gui
import Model.Utilisateurs
import Model.Question


def commencer_jeu():

    """
    cette fonction me permet de recevoir les renseignements et ensuite de jouer

    :return: une fonction qui lance le jeu
    """

    message_bienvenu = "Bienvenue dans notre Quizz Générale "
    print(message_bienvenu)

    nom = input("Veuillez donner votre Nom :")
    prenom = input("Veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")


    return jouer(nom,prenom,pseudo)


def jouer(nom, prenom, pseudo):
    print(f" {pseudo},Bonne partie ")



    """
    cette fonction permet de jouer et enregistrer les données d'un joueur

    :param nom: nom du joueur
    :param prenom: prénom du joueur
    :param pseudo: pseudo du joueur
    :return:
    """

    jeu = JEux(nom, prenom, pseudo)
    #me permet instance la classe jEux les renseignement au jeu , qui ensuite seront utile à la partie
    jeu.setPartie()
    #cette méthode de jeu me permet de d'appleler 1)setTheme() qui demande le thème et 2)recupQuestions()

    score = 0
    for questions in jeu.getPartie: #parcours le tableau de questions
        questions_demande = input(f"{questions.getQuestion()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
        if questions_demande == questions.getReponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {questions.getReponse()}")

    print(f"votre score est de {score} / {len(jeu.getPartie)}")

    ajouter_question = input("voulez vous ajoutez une question ? oui ou non :")
    if ajouter_question == "oui":
        ajout_question()

    else:
        quit()


def ajout_question():

    theme = input("Dans quelle thème voulez-vous l'ajouter ? : ")
    question = input("Quelle question voulez-vous ajouter ainsi que ses propositions ? : ")
    reponse = input("Quelle est la lettre correspondants à la question ? : ")

    Model.Question.Question.ajout_question(theme,question,reponse)


if __name__ == "__main__":

    #thread = threading.Thread(target=Gui.demarrage_interface())
    #thread.start()

    commencer_jeu()
    #jouer()
