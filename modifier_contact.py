from recuperer_contact import recuperer_contact
from supprimer_contact import supprimer_contact


def modifier_contact(numero_contact_a_modifier, numero_info_a_modifier, nouvelle_valeur, liste_contacts):
    """
        fonction pour modifier une information concernant le contact

    """

    # récupération du contact (objet) dont on modifiera une information
    contact_a_modifier = recuperer_contact(numero_contact_a_modifier, liste_contacts)

    # suppression fichier contact préexistant : pour ne pas créer un nouveau fichier de contact dans le cas d'une modification
    # du nom ou du numero de téléphone
    supprimer_contact(numero_contact_a_modifier, liste_contacts)

    # on modifie l'attribut correspondant au numéro fourni par l'utilisateur
    if numero_info_a_modifier == 1:
        contact_a_modifier.nom = nouvelle_valeur

    elif numero_info_a_modifier == 2:
        contact_a_modifier.prenom = nouvelle_valeur

    elif numero_info_a_modifier == 3:
        contact_a_modifier.email = nouvelle_valeur

    elif numero_info_a_modifier == 4:
        contact_a_modifier.numero = nouvelle_valeur

    nom = contact_a_modifier.nom
    prenom = contact_a_modifier.prenom
    email = contact_a_modifier.email
    numero = contact_a_modifier.numero
    nom_fichier = nom + numero + ".txt"
    
    # on met à jour le fichier du contact avec de nouvelles informations
    contact_a_modifier.ajouter_contact(nom_fichier)


    # retourne le contact modifier
    return contact_a_modifier