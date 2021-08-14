import subprocess
from datetime import datetime


class ErreurCustomiser:

    def __init__(self, erreurs):
        self.__erreurs = erreurs

    def erreurs(self):
        return self.__erreurs

    def sauvegarde_erreur(self):

        """
               Cette fonction permet la sauvegarde d'erreur
               PRE: -
               POST: le fichier sauvegarde_erreurs.txt à été modifier en ajoutant une nouvelle erreur
               """

        try:
            with open('../erreur/sauvegarde_erreurs.txt', 'a', encoding='utf-8') as fichier_des_erreurs:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                message_detection_erreur = f"=" * 40 + f" A {current_time} , Erreur trouvée " + "=" * 40
                message_erreur = f"\nUne erreur à été détecté et la voici : {self.__erreurs}"

                fichier_des_erreurs.write("\n")
                fichier_des_erreurs.write(message_detection_erreur)
                fichier_des_erreurs.write(message_erreur)

                ErreurCustomiser(self.__erreurs).gestion_erreur()

            # fichier_des_erreurs.write(f"=" * 40 + " Bienvenue dans votre fichier d'erreurs" + "=" * 40)
            # ichier_des_erreurs.write(message_de_debut)

        except IOError:
            print('Erreur IO.')

    def gestion_erreur(self):

        """
        Cette fonction permet la gestion d'erreur
        PRE: -
        POST:Une page web est ouverte pour communiquer avec le créateur du Quizz et le fichier sauvegarde_erreurs.txt à été modifier en ajoutant une nouvelle erreur
        """
        # message_de_debut = f"\nBienvenue utilisateur , vous voici dans le fichier contenant les erreurs du Quizz. "

        print("Bienvenue sur la fonction permettant la gestion erreur")
        demande = input(f"Je suis face à une erreur {self.__erreurs} et je ne sais pas quoi faire ? "
                        "\nPas de soucis vous êtes au bonne endroit."
                        "\nVous pouvez contactez une des créateur de l'application via ces réseaux ,"
                        " en insérant : contact"
                        "\nou arréter le quizz : stop"
                        "\n Votre erreur est sauvegarder dans le fichier sauvegarde_erreur.txt"
                        "\n Veuillez insérer votre demande ? :  ")

        if demande == "contact":
            subprocess.run(['start', 'https://www.linkedin.com/in/merwane-ben-tahri/'], shell=True,
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
            print(
                "Ben-Tahri Merwane est l'un des créateurs de ce quizz , "
                " son email : he201794@students.ephec.be ")
        elif demande == "stop":
            quit()
        else:
            print("Nous vous conseillons vivement de contacter le codeur du Quizz")


'''
if __name__ == "__main__":
    error = ErreurCustomiser("BANANA").sauvegarde_erreur()
'''
