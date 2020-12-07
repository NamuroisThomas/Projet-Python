# code écrit par Ben-Tahri Merwane et Thomas Namurois
import Gui
import Utilisateur
import Question
import json
import threading


def demarrage_jeu():
    message_bienvenue = "Bienvenue dans notre Quizz Générale "


def renseignement():
    nom = input("Veuillez donner votre Nom :")
    prenom = input("Veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")
    Utilisateur.utilisateur.sauvegarde_utilisateur(nom, prenom, pseudo)

    return (nom, prenom, pseudo)


def recherche_Question():
    with open('./questions/questions.json') as json_question:
        test = json.load(json_question)
        question = dict(test)
        print(question)

    score = 0
    choix_theme = input("Veuillez choisir entre les 3 thème suivant : geographie,informatique et histoire  : ")

    while True:
        for theme in question.keys():
            if theme == choix_theme:
                for questions in question[choix_theme]:  # parcour les thèmes de notre quizz , afin de lancer les questions correspondant au thème choisis

                    questions_demande = input(f"{questions[0]}\n,veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
                    # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
                    if questions_demande == questions[1]:

                        score += 1
                        print(f"votre score est de {score} / {len(question[choix_theme])}")

                    else:

                        print("mauvaise réponse")
                        print(f"la bonne réponse étais : {questions[1]}")

                break

            choix_theme = input("veuillez choisir entre les 3 thème suivant : geographie,informatique et histoire  : ")


            ajout_question = print("Voulez vous ajoutez une question ? oui ou non : ")
            if ajout_question == "oui":
                ajout_Question()

        return score


def ajout_Question():
    theme = input("Dans quelle thème voulez vous ajouter la nouvelle Question/Réponse (geographie,informatique et histoire) : ")
    question = input("Quelle est votre Question , accompagner des proposition ainsi (a) choix 1 (b) choix(2) ... ? : ")
    reponse = input("Donner la lettre de la réponse : ")

    Question.Questions.ajout_question(theme, question, reponse)


if __name__ == "__main__":

    thread = threading.Thread(target=Gui.demarrage_interface())
    thread.start()

    # demarrage_jeu()
    # renseignement()
    # recherche_Question()

    # recherche_Question()

    # quizz_test()
    # Question.Questions.question_de_Base()
    # Question.Questions.ajout_question()
    # Utilisateur.utilisateur.recuperation_utilisateur()

"""
#fonction qui lance le programme principale
def quizz_test():

    with open('./questions/questions.json') as json_question:
        question = json.load(json_question)


    nom = input("veuillez donner votre Nom :")
    prenom = input("veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")
    Utilisateur.utilisateur.sauvegarde_utilisateur(nom,prenom,pseudo)

    print(f"bienvenue {nom} {prenom} alias {pseudo} sur notre Quizz générale Bonne partie :")
    score = 0
    choix_theme = input("veuillez choisir entre les 3 thème suivant : geographie,informatique et histoire  : ")

    for i in question[choix_theme]:#parcour les thèmes de notre quizz , afin de lancer les questions correspondant au thème choisis

        questions = input(f"{i[0]}\n,veuillez choisir la lettre correspondant à la réponses  :  ")#correspond a nos questions
                #cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
        if questions == i[1]:

            score += 1
            print(f"votre score est de {score} / {len(question[choix_theme])}")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {i[1]}")



    return score

"""
