import subprocess


class ErreurCustomiser:
    """
    Cette classe me permet l'execption erreur
    """

    def gestion_erreur(self, erreur):
        if isinstance(erreur, (FileNotFoundError, IOError)):

            print("Bienvenue sur la fonction permettant la gestion erreur")
            demande = input("Je suis face à une erreur et je ne sais pas quoi faire ? "
                            "\nPas de soucis vous êtes au bonne endroit."
                            "\nVous pouvez contactez une des créateur de l'application via ces réseaux ,"
                            " en insérant : contact"
                            "\nou arréter le quizz : stop"
                            "\n"
                            "Veuillez insérer votre demande ? :  ")

            if demande == "contact":
                subprocess.run(['start', 'https://www.facebook.com/Eddy.maloub/'], shell=True,
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
                print(
                    "Ben-Tahri Merwane est l'un des créateurs de ce quizz , "
                    " son email : he201794@students.ephec.be ")
            elif demande == "stop":
                quit()
            else:
                print("Nous vous conseillons vivement de contacter le codeur du Quizz")
