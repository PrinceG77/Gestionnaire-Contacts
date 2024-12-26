from recuperer_contact import recuperer_contact
import os

def supprimer_contact(identifiant_contact_a_supprimer, liste_contacts):
    # récupération du contact (objet de la class contact) à supprimer
    contact_a_supprimer = recuperer_contact(identifiant_contact_a_supprimer, liste_contacts)

    fichier_contact_a_supprimer = contact_a_supprimer.nom + contact_a_supprimer.numero + ".txt"

    if os.path.exists(fichier_contact_a_supprimer):
        os.remove(fichier_contact_a_supprimer)
        print(f"Le contact {contact_a_supprimer.nom} a été supprimé avec succès.")

    else:
        print(f"Impossible de supprimer ce contact car il n'est pas dans la liste de vos contacts")