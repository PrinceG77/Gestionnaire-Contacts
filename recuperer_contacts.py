import glob
import os
from contact import Contact
#from afficher_contacts import afficher_contacts

def recuperer_contacts():
    liste_contacts = []
    
    noms_fichiers_contact = [os.path.basename(f) for f in glob.glob("./*.txt")]
    #print(noms_fichiers_contact)

    for i in range(len(noms_fichiers_contact)):
        with open(noms_fichiers_contact[i], "r") as contact:
            liste_infos_contact = [ligne.strip() for ligne in contact]
            nom = liste_infos_contact[0]
            prenom = liste_infos_contact[1]
            email = liste_infos_contact[2]
            numero = liste_infos_contact[3]
            #print(f"liste infos contact => {liste_infos_contact}")
            liste_contacts.append(Contact(nom, prenom, email, numero))
    return liste_contacts


#afficher_contacts(recuperer_contacts())