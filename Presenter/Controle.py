import threading
from Model.JEux import JEux
import Gui



def commencer_jeu():
    message_bienvenu = "Bienvenue dans notre Quizz Générale "
    print(message_bienvenu)

    nom = input("Veuillez donner votre Nom :")
    prenom = input("Veuillez donner votre Prénom :")
    pseudo = input("veuillez donner votre Pseudo :")

    return jouer(nom,prenom,pseudo)


def jouer(nom, prenom, pseudo):
    jeu = JEux(nom, prenom, pseudo)
    jeu.setPartie()
    #print(jeu.getPartie[0].getQuestion())

    score = 0
    for i in jeu.getPartie:
        questions_demande = input(f"{i.getQuestion()}{i.getReponseA()}{i.getReponseB()}{i.getReponseC()}\n,veuillez choisir la lettre correspondant à la réponses  :  ")  # correspond a nos questions
        # cette condition nous permet de vérifier si la réponse a cette question égale a nos reponses définis avant
        if questions_demande == i.getReponse():

            score += 1
            print("bonne réponse")

        else:

            print("mauvaise réponse")
            print(f"la bonne réponse étais : {i.getReponse()}")

    print(f"votre score est de {score} / {len(jeu.getPartie)}")


if __name__ == "__main__":
    thread = threading.Thread(target=Gui.demarrage_interface())
    thread.start()
    #commencer_jeu()
    #jouer()
