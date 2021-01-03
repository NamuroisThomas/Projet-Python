import threading
from Model.jeu import Jeu
import Gui
import Model.Utilisateurs


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

    return jouer(nom, prenom, pseudo)


def jouer(nom, prenom, pseudo):
    Model.Utilisateurs.Utilisateurs.sauvegarde_utilisateur(nom, prenom, pseudo)

    """
    cette fonction permet de jouer et enregistrer les données d'un joueur

    :param nom: nom du joueur
    :param prenom: prénom du joueur
    :param pseudo: pseudo du joueur
    :return:*
    """

    jeu = Jeu(nom, prenom, pseudo)
    # me permet instance la classe jEux les renseignement au jeu , qui ensuite seront utile à la partie
    jeu.setpartie()
    # cette méthode de jeu me permet de d'appleler 1)setTheme() qui demande le thème et 2)recupQuestions()

    score = 0
    for questions in jeu.getpartie:  # parcours le tableau de questions
        questions_demande = input(
            f"{questions.getQuestion()}{questions.getReponseA()}{questions.getReponseB()}{questions.getReponseC()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
        if questions_demande == questions.getReponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {questions.getReponse()}")

    print(f"votre score est de {score} / {len(jeu.getpartie)}")


if __name__ == "__main__":
    Gui.demarrage_interface()

    #commencer_jeu()
    # jouer()
