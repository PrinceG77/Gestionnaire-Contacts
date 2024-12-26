
# affiche la liste de tous les contacts
def afficher_contacts(liste_contacts):
    repetition = 90
    print("*"*repetition)
    #print(f"Liste de tous vos constacts\n(Identifiant - Nom - Prenom - Email - Téléphone)")
    print(f"{'Liste de tous vos contacts':^{repetition}}")  # Titre centré
    print("*"*repetition)
    # Entêtes des colonnes
    print(f"{'ID':<5} {'Nom':<20} {'Prénom':<20} {'Email':<30} {'Téléphone':<15}")
    print("-" * repetition)

    for i in range(len(liste_contacts)):
        print(f"{i+1:<5} {liste_contacts[i].nom:<20} {liste_contacts[i].prenom:<20} {liste_contacts[i].email:<30} {liste_contacts[i].numero:<15}")
    print("*"*repetition)

