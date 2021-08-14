# code écrit par Ben-Tahri Merwane et Thomas Namurois
import Gui
import Utilisateur
import Question
import json
import threading
import Jeu



def ajout_Question():

    theme = input("Dans quelle thème voulez vous ajouter la nouvelle Question/Réponse (geographie,informatique et histoire) : ")
    question = input("Quelle est votre Question , accompagner des proposition ainsi (a) choix 1 (b) choix(2) ... ? : ")
    reponse = input("Donner la lettre de la réponse : ")

    Question.Questions.ajout_question(str(theme), question, reponse)







def commencer_jeu():
    message_bienvenu = "Bienvenue dans notre Quizz Générale "
    print(message_bienvenu)

    nom = input("Veuillez donner votre Nom :")
    prenom = input("Veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")

    jeu = JEux(nom, prenom, pseudo)
    jeu.partie()
    #print(jeu.getPartie[0].getQuestion())

    score = 0
    for i in jeu.tableau_question_partie:
        questions_demande = input(f"{i.getQuestion()}{i.getReponseA()}{i.getReponseB()}{i.getReponseC()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
        if questions_demande == i.getReponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {i.getReponse()}")

    print(f"votre score est de {score} / {len(jeu.tableau_question_partie)}")


if __name__ == "__main__":
    commencer_jeu()
    enregistrerPartie()


if __name__ == "__main__":


    thread = threading.Thread(target=Gui.demarrage_interface())
    thread.start()

    #demarrage_jeu()
    #renseignement()
    #recherche_question()



    # Question.Questions.question_de_Base()
    # Question.Questions.ajout_question()
    # Utilisateur.utilisateur.recuperation_utilisateur()
