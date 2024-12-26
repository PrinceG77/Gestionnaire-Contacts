from contact import Contact
from afficher_contacts import afficher_contacts
from recuperer_contacts import recuperer_contacts
from modifier_contact import modifier_contact
from supprimer_contact import supprimer_contact

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
            print(f"*******************************************************************************")
            print(f"Ajout Contact")
            # boucle pour tester que l'objet a été créé sans aucun problème
            while (True):
                print(f"Veuillez svp saisir les informations ci-dessous pour ajouter un nouveau contact")
                nom = input("Nom : ")
                prenom = input("Prenom : ")
                email = input("Email : ")
                numero = input("Téléphone : ")
                try:
                    contact = Contact(nom, prenom, email, numero)
                except ValueError as messageErreur:
                    print(f"{messageErreur}\n")
                else:
                    break

            contact.ajouter_contact(nom+numero+".txt")
            print("Le contact a été ajouté avec succès")
            choix_ajout = input("Entrez n'importe quelle valeur si vous souhaitez poursuivre avec l'ajout et (M) Si vous souhaitez retourner au menu principal : ")
            if choix_ajout.strip().upper() == "M":
                break
            print(f"*******************************************************************************")


    #option modifier un/plusieurs contact(s)
    elif choix_option_int == 2:
            # boucle pour modifier plusieurs contacts successivement
            while (True):
                print(f"*******************************************************************************")
                print(f"Modification Contact")
                liste_contacts = recuperer_contacts()
                afficher_contacts(liste_contacts)

                # boucle pour la saisie d'un chiffre correcte
                while(True):
                    choix_contact_str = input(f"Veuillez svp rentrer le numero du contact que vous souhaitez modifier ({1}-{len(liste_contacts)}): ")

                    if choix_contact_str.strip().isdigit():
                        choix_contact_int = int(choix_contact_str)
                        if 1 <= choix_contact_int <= len(liste_contacts):
                            break
                        else:
                            print(f"La valeur {choix_contact_int} n'est pas comprise entre 1 et {len(liste_contacts)}. Veuillez réesayer svp.")

                    else:
                        print(f"La valeur {choix_contact_str} n'est pas un chiffre. Veuillez réesayer svp.")

                # fin boucle
            
                # boucle pour la saisie d'un chiffre correcte
                while(True):
                    print(f"Quelle info souhaitez vous modifier ?")
                    numero_info_a_modifier_str = input("(1) Nom (2) Prenom (3) Email (4) Numero => ")

                    if numero_info_a_modifier_str.strip().isdigit():
                        numero_info_a_modifier_int = int(numero_info_a_modifier_str)
                        if 1 <= numero_info_a_modifier_int <= 4:
                            break
                        else:
                            print(f"La valeur {numero_info_a_modifier_int} n'est pas comprise entre 1 et 4. Veuillez réesayer svp.")

                    else:
                        print(f"La valeur {numero_info_a_modifier_int} n'est pas un chiffre. Veuillez réesayer svp.")

                # fin boucle
                a_modifier = ""
                if numero_info_a_modifier_int == 1:
                    a_modifier = "Nom"

                elif numero_info_a_modifier_int == 2:
                    a_modifier = "Prenom"

                elif numero_info_a_modifier_int == 3:
                    a_modifier = "Email"

                elif numero_info_a_modifier_int == 4:
                    a_modifier = "Téléphone"

                #print(f"numero contact à modifier : {choix_contact_int} | info à modifier : {numero_info_a_modifier_int}")
                #print(f"liste_contacts : {liste_contacts}")


                valeur = input(f" {a_modifier} : ")

                #print(f"nouvelle valeur: {valeur}")

                contact_modifie = modifier_contact(choix_contact_int, numero_info_a_modifier_int, valeur, liste_contacts)
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
            afficher_contacts(liste_contacts)
            # boucle choix d'identifiant correct
            while(True):
                identifiant_contact_str = input("Veuillez rentrer l'identifiant du contact que vous souhaitez supprimer : ")

                if identifiant_contact_str.strip().isdigit():
                    identifiant_contact_int = int(identifiant_contact_str)
                    if 1 <= identifiant_contact_int <= len(liste_contacts):
                        break
                    else:
                        print(f"La valeur {identifiant_contact_int} n'est pas comprise entre 1 et {len(liste_contacts)}. Veuillez réesayer svp.")

                else:
                    print(f"La valeur {identifiant_contact_str} n'est pas un chiffre. Veuillez réesayer svp.")

            decision_finale = input("Êtes vous sûr de vouloir supprimer ce contact\nEntrez n'importe quelle valeur pour poursuivre la suppression"
                                    "ou entrer (A) pour annuler et retourner au menu principal : ")
            
            if decision_finale.strip().upper() == "A":
                break

            supprimer_contact(identifiant_contact_int, liste_contacts)
            print(f"Que souhaitez-vous faire ?")
            choix = input(f"(n'importe qu'elle valeur) Poursuivre \t(M) Retourner au menu principal : ")

            if choix.strip().upper() == "M":
                break
            
        print(f"******************************************************************************")
        print()

    #option afficher tous les contacts
    elif choix_option_int == 4:
        liste_contacts = recuperer_contacts()
        afficher_contacts(liste_contacts)
        menu_principal = input("Appuyez sur n'importe quelle touche pour revenir au menu principal: ")
        

    # option quitter le programme
    elif choix_option_int == 5:
        break

#fin du programme
print("Merci d'avoir utilisé notre application. En espérant vous revoir bientôt.")
