

class Contact:
    
    def __init__(self, nom, prenom, email, numero) -> None:
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.numero = numero

    # getter pour nom
    @property
    def nom(self):
        return self.__nom
    
    #setter pour nom 
    @nom.setter
    def nom(self, nom):
        if not nom.strip():
            raise ValueError("Impossible de créer un contact avec un nom vide. Veuillez réesayez svp...")
        self.__nom = nom


    # getter pour prenom
    @property
    def prenom(self):
        return self.__prenom
    
    #setter pour prenom 
    @prenom.setter
    def prenom(self, prenom):
        if not prenom.strip():
            raise ValueError("Impossible de créer un contact avec un prenom vide. Veuillez réesayez svp...")
        self.__prenom = prenom


    # getter pour email
    @property
    def email(self):
        return self.__email
    
    #setter pour email 
    @email.setter
    def email(self, email):
        if "@" not in email or not email.strip():
            #print(f"numero : {email.strip()}")
            raise ValueError("Impossible de créer un contact avec un email vide et/ou invalide. Veuillez réesayez svp...")
        self.__email = email


    # getter pour numero
    @property
    def numero(self):
        return self.__numero
    
    #setter pour numero
    @numero.setter
    def numero(self, numero):
        if not (len(numero.strip()) == 10) or not numero.strip().isdigit():
            #print(f"longueur numero : {len(numero.strip())}")
            #print(f"numero : {numero.strip()}")
            raise ValueError("Impossible de créer un contact avec un numéro de téléphone invalide. Veuillez réesayez svp...")
        self.__numero = numero


    def ajouter_contact(self, nom_fichier):
       
        with open(nom_fichier, "w") as mon_fichier:
            mon_fichier.write(f"{self.nom}\n")
            mon_fichier.write(f"{self.prenom}\n")
            mon_fichier.write(f"{self.email}\n")
            mon_fichier.write(f"{self.numero}\n")
