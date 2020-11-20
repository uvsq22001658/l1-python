# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné"""
    """comme jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond
    au nombre de seconde passé en argument"""
    jour = seconde // 86400
    j = seconde % 86400
    heure = j // 3600
    h = j % 3600
    minute = h // 60
    seconde = h % 60
    return(jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes",
                temps[3], "secondes")

def affichePluriel(mot, nombre)
    if nombre > 0 :
        print(nombre, mot, end="")
    if nombre > 1 :
        print("s", end="")


def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    
afficheTemps((1,0,14,23))    


def demandeTemps():
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

while (jours < 0) :
    jours = int(input("Entrer un nombre de jours"))

while (heures < 0 or heures >= 24) :
    heures = int(input("Entrer un nombre d'heures"))

while (minutes < 0 or minutes >= 60) :
    minutes = int(input("Entrer un nombre de minutes"))

while (secondes < 0 or secondes > 60) :
    secondes = int(input("Entrer un nombre de secondes"))

return (jours, heures, minutes, secondes)

afficheTemps(demandeTemps())


def sommeTemps(temps1 : tuple, temps2 : tuple) -> tuple :
    seconde1 = tempsEnSeconde(temps1)
    seconde2 = tempsEnSeconde(temps2)
    seconde3 = seconde1 + seconde2
    return seconde3
    

sommeTemps((2,3,4,25),(5,22,57,1))


def proportionTemps(temps : tuple, proportion : float) -> tuple :
    secondes = tempsEnSeconde(temps)
    seconde2 = int(secondes * proportion)
    tempsFinal = secondeEnTemps(seconde2)
    return tempsFinal
afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments


def tempsEnDate(temps : tuple) -> tuple :
    annees = temps[0] // 365
    jours = temps[0] % 365
    return (1970 + annees, 1 + jours, temps[1], temps[2], temps[3])


def afficheDate(date : tuple) :
    print("Annee", date[0], "Jour", date[1], str(date[2] + "i" + str(date[3]))
                            + "i" + str(date[4]))
    
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()


def nombreBisextile(jour):
    pass

def tempsEnDateBisextile(temps):
    pass
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))