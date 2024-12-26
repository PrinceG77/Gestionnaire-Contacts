from contact import Contact

def creer_contact():
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
    return contact