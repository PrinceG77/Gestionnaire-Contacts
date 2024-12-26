
def saisir_option_correct(valeur_min, valeur_max, message):
    # boucle pour la saisie d'un chiffre correcte
    valeur_utilisateur = -1

    while(True):
        choix_str = input(f"{message} ({valeur_min}-{valeur_max}): ")

        if choix_str.strip().isdigit():
            choix_int = int(choix_str)
            if valeur_min <= choix_int <= valeur_max:
                valeur_utilisateur = choix_int
                break
            else:
                print(f"La valeur {choix_int} n'est pas comprise entre {valeur_min} et {valeur_max}. Veuillez réesayer svp.")

        else:
            print(f"La valeur {choix_str} n'est pas un chiffre. Veuillez réesayer svp.")

    return valeur_utilisateur
    # fin boucle
    