import csv




def ajout_utilisateur(nom,prenom,pseudo):

    try:
        with open("utilisateur_test.csv", "a", encoding='utf-8') as fichier_Utilisateur:
             #entete = ['ID',"Nom", "Prenom", "Pseudo"]
             donne = ['', nom,prenom,pseudo]

             #csv_fichier = csv.DictWriter(fichier_Utilisateur, fieldnames=entete)
             #csv_fichier.writeheader()

             sauvegarde = csv.writer(fichier_Utilisateur)
             sauvegarde.writerow(donne)


    except FileNotFoundError:
        print('Fichier introuvable.')

    except IOError:
        print('Erreur IO.')


def verification_ajout_utilisateur():

    try:
        with open('utilisateur_test.csv', 'r') as fichier_utilisateur:
            lecture_utilisateurs = csv.reader(fichier_utilisateur)

            for i in lecture_utilisateurs:
                print(i)




    except FileNotFoundError:
        print('Fichier introuvable.')

    except IOError:
        print('Erreur IO.')




if __name__ == "__main__":
    #ajout_utilisateur('jean12','pierre12','blabla2')
    verification_ajout_utilisateur()

