def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" les problèmes sinon
    """
    alerte = False
    message = ""

    if isinstance(temp, int) or isinstance(temp, float):
        if temp < 18:
            message += "Température trop basse \n"
            alerte = True
        elif temp > 27:
            message += "Température trop élevée \n"
            alerte = True
    else:
        message += "La température est exprimé en chiffre!"
        alerte = True

    if isinstance(poussiere, str):
        if poussiere != "faible" and poussiere != "Faible":
            message += "Trop de poussière\n"
            alerte = True
    else:
        message += "La poussière est exprimé en string, par faible, moyen et élevé!\n"
        alerte = True

    if isinstance(humidite, int) or isinstance(humidite, float):
        if humidite <= 30 :
            message += "Il fait pas assez humide\n"
            alerte = True
        elif humidite >= 50:
            message += "Il fait trop humide\n"
            alerte = True
    else:
        message += "L'humidité est exprimé en chiffre!"
        alerte = True

    if message != "":
        print(message)

    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"

if __name__ == "__main__":
    i = 0
    ls_temp = [20, 21, 40, 100, 0]
    ls_dust = ["faible", "faible", "faible", "élevé", "moyen"]
    ls_wet = [40, 30, 45, 99, 0]
    nb_ordi = int(input("Combien d'ordinateur à tester?"))

    for i in range(nb_ordi):
        temp = float(input("Entrer la température"))
        dust = input("entrer le niveau de poussière")
        wet = float(input("Entrer le taux d'humidité"))
        ls_temp.append(temp)
        ls_dust.append(dust)
        ls_wet.append(wet)


    for i in range(len(ls_temp)):
        print(environnement_optimal(ls_temp[i], ls_dust[i], ls_wet[i]))

