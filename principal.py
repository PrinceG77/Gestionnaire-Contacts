from contact import Contact
from afficher_contacts import afficher_contacts
from recuperer_contacts import recuperer_contacts
from modifier_contact import modifier_contact
from supprimer_contact import supprimer_contact
from creer_contact import creer_contact
from saisir_option_correct import saisir_option_correct

option_menu_min = 1
option_menu_max = 5
fichier_de_contact = "contacts.txt"

print("Bienvenu dans l'application de Gestion de contact")
print("*************************************************")

# boucle principal de l'application
while(True):
    # boucle menu principal : attend le choix de l'utilisateur, vérifie sa validité et 
    # entrée utilisateur valide : conserve son choix  dans la variable choix_option_int
    # entrée utilisateur invalide : affiche de nouveau le menu à l'utilisateur jusqu'à ce qu'il entre une valeur correcte
    while(True):
        print("Que souhaitez-vous faire ? ")
        print("(1) Ajouter un contact\n(2) Modifier un contact\n(3) Supprimer un contact\n(4) Afficher tous les contacts\n(5) Quitter")
        choix_option_str = input("Entrer le chiffre correspondant à l'action souhaitée : ")
        # première vérification : la chaine de caractère saisie ne contient que des chiffres
        if choix_option_str.strip().isdigit():
            choix_option_int = int(choix_option_str)
        # deuxième vérification : le nombre ainsi obtenu se situe dans l'intervalle souhaité 
        # cas valide : on quitte la boucle
        # cas invalide : on affiche un message d'erreur et on revient au début de la boucle
            if option_menu_min <= choix_option_int <= option_menu_max:
                break
            print(f"ERREUR : Le chiffre saisi doit être compris entre {option_menu_min} et {option_menu_max}. Veuillez réesayer svp...")

        else:
            print("ERREUR : Le caractère saisi n'est pas un chiffre. Veuillez réesayer svp...")
        
        print()



    # option ajout d'un/de nouveau(x) contact(s)
    if choix_option_int == 1:
        # boucle pour ajouter plusieurs contacts successivement
        while (True):
            contact = creer_contact()
            contact.ajouter_contact(contact.nom+contact.numero+".txt")
            print("Le contact a été ajouté avec succès")
            choix_ajout = input("Entrez n'importe quelle valeur si vous souhaitez poursuivre avec l'ajout et (M) Si vous souhaitez retourner au menu principal : ")
            if choix_ajout.strip().upper() == "M":
                break
            print(f"*******************************************************************************")


    #option modifier un/plusieurs contact(s)
    elif choix_option_int == 2:
            # boucle pour modifier plusieurs contacts successivement
            while (True):
                while(True):
                    print(f"*******************************************************************************")
                    print(f"Modification Contact")
                    afficher_contacts()
                    liste_contacts = recuperer_contacts()

                    # boucle pour la saisie d'un chiffre correcte
                    id_contact = saisir_option_correct(1, len(liste_contacts), "Veuillez svp rentrer le numero du contact que vous souhaitez modifier")
                    # fin boucle
                
                    # boucle pour la saisie d'un chiffre correcte
                    numero_info_contact = saisir_option_correct(1, 4, "Quelle info souhaitez vous modifier ?\n(1) Nom (2) Prenom (3) Email (4) Numero => ")
                    # fin boucle
                    a_modifier = ""
                    if numero_info_contact == 1:
                        a_modifier = "Nom"

                    elif numero_info_contact == 2:
                        a_modifier = "Prenom"

                    elif numero_info_contact == 3:
                        a_modifier = "Email"

                    elif numero_info_contact == 4:
                        a_modifier = "Téléphone"

                    #print(f"numero contact à modifier : {choix_contact_int} | info à modifier : {numero_info_a_modifier_int}")
                    #print(f"liste_contacts : {liste_contacts}")


                    valeur = input(f" {a_modifier} : ")

                    #print(f"nouvelle valeur: {valeur}")
                    try:
                        contact_modifie = modifier_contact(id_contact, numero_info_contact, valeur, liste_contacts)
                    except ValueError as message:
                        print(f"{message}")
                    else:
                        break

                print(f"Contact modifié avec succès")
                print(f"Voici ces informations mis à jour")
                print(f"Nom : {contact_modifie.nom}")
                print(f"Prenom : {contact_modifie.prenom}")
                print(f"Email : {contact_modifie.email}")
                print(f"Téléphone : {contact_modifie.numero}")
                print("*******************************************************************")
                poursuivre = input(f"Appuyez n'importe où pour poursuivre et (M) pour revenir au menu principal : ")

                if poursuivre.strip().upper() == "M":
                    break


    #option supprimer un contact
    elif choix_option_int == 3:
        while(True):
            print()
            print(f"******************************************************************************")
            print(f"Suppression d'un contact")
            print()
            liste_contacts = recuperer_contacts()
            afficher_contacts()
            # boucle choix d'identifiant correct
            id_contact = saisir_option_correct(1, len(liste_contacts), "Veuillez rentrer l'identifiant du contact que vous souhaitez supprimer : ")

            decision_finale = input("Êtes vous sûr de vouloir supprimer ce contact\nEntrez n'importe quelle valeur pour poursuivre la suppression"
                                    "ou entrer (A) pour annuler et retourner au menu principal : ")
            
            if decision_finale.strip().upper() == "A":
                break

            supprimer_contact(id_contact, liste_contacts)
            print(f"Que souhaitez-vous faire ?")
            choix = input(f"(N'importe quelle valeur) Poursuivre \t(M) Retourner au menu principal : ")

            if choix.strip().upper() == "M":
                break
            
        print(f"******************************************************************************")
        print()

    #option afficher tous les contacts
    elif choix_option_int == 4:
        afficher_contacts()
        menu_principal = input("Appuyez sur n'importe quelle touche pour revenir au menu principal: ")
        

    # option quitter le programme
    elif choix_option_int == 5:
        break

#fin du programme
print("Merci d'avoir utilisé notre application. En espérant vous revoir bientôt.")
