# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
# Liens utiles : https://www.epochconverter.com/ ; https://www.calendar-365.com/day-numbers/2020.html

import time


def tempsEnSeconde(temps: tuple) -> int:
    """ Renvoie la valeur en seconde de temps donné
    comme jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]


# temps = (3, 23, 1, 34)
# print(type(temps))
# print(tempsEnSeconde(temps))


def secondeEnTemps(seconde: int) -> tuple:
    """Renvoie le temps (jour, heure, minute, seconde) qui
    correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    return (jours, heures, minutes, reste)


# temps = secondeEnTemps(100000)
# print(temps[0], "jours", temps[1], "heures", temps[2], "minutes",
#                 temps[3], "secondes")


def affichePluriel(mot: str, nombre: int):
    """ Affiche (ou non) un mot en fonction du paramètre nombre. \
        Met le mot au pluriel si nécessaire."""
    if nombre > 0:
        print(" ", nombre, mot, end="")

    if nombre > 1:
        print("s", end="")


def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print()


# afficheTemps((1, 0, 14, 23))

def demandeTemps():
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jours < 0):
        jours = int(input("Entrez un nombre de jour"))

    while (heures < 0 or heures >= 24):
        heures = int(input("Entrez un nombre d'heures"))

    while (minutes < 0 or minutes >= 60):
        minutes = int(input("Entrez un nombre de minutes"))

    while (secondes < 0 or secondes >= 60):
        secondes = int(input("Entrez un nombre de secondes"))

    return (jours, heures, minutes, secondes)


# afficheTemps(demandeTemps())

def sommeTemps(temps1: tuple, temps2: tuple) -> tuple:
    """Retourne la somme des deux temps passés en paramètres."""
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


# afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps: tuple, proportion: float) -> tuple:
    """Retourne un temps egal au temps passé en paramètre après
    application de la proportion."""
    return secondeEnTemps(int(tempsEnSeconde(temps) * proportion))


# afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))
# afficheTemps(proportionTemps(proportion=0.2, temps=(2, 0, 36, 0)))

def tempsEnDate(temps: tuple) -> tuple:
    annees = temps[0] // 365
    jours = temps[0] % 365
    return (1970 + annees, 1 + jours, temps[1], temps[2], temps[3])


# afficheDate(date: tuple = ()) : Cela signifie que la fonction
# prend un paramètre date de type tuple. Ce paramètre peut être
# omis et dans ce cas il prendra la valeur par défaut () qui est
# un tuple vide.
def afficheDate(date: tuple = ()):
    """ Affiche la date passée en paramètre. Si aucune date n'est passée,
    affiche la date du jour."""
    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Annee", date[0], "Jour", date[1], str(date[2]) + ":" + str(date[3])
                            + ":" + str(date[4]))


# temps = secondeEnTemps(86401)
# afficheTemps(temps)
# afficheDate(tempsEnDate(temps))
# afficheDate()

# print(time.time())
# afficheDate()


def bisextile(jour):
    annee = 1970
    while(jour >= 365):
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            print("L'année " + str(annee) + " est bisextile")
            jour -= 366
        else:
            jour -= 365
        annee += 1


# bisextile(20000)


def nombreBisextile(jour: int) -> int:
    annee = 1970
    compteur_bisextile = 0
    while(jour >= 365):
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            compteur_bisextile += 1
            jour -= 366
        else:
            jour -= 365
        annee += 1
    return compteur_bisextile


def tempsEnDateBisextile(temps):
    jour, heure, minute, seconde = temps
    jour = jour - nombreBisextile(jour)
    temps_ajuste = (jour, heure, minute, seconde)
    return tempsEnDate(temps_ajuste)


afficheDate(tempsEnDateBisextile(secondeEnTemps(int(time.time()))))


