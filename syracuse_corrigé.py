def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste.append(n)
    return liste


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max):
        syracuse(i)
    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le nombre d'étapes pour aller de n à 1 
    dans la suite de syracuse"""
    return len(syracuse(n)) - 1


print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max + 1)]


print(tempsVolListe(100))

temps = tempsVolListe(10000)
temps_max = max(temps)
print(temps.index(temps_max) + 1, temps_max)


def alt_max(n):
    """Retourne l'altitude maximale de l'entier n"""
    return max(syracuse(n))


def alt_max_liste(n_max):
    """Retourne la liste des altitudes maximales des entiers de 1 à n_max"""
    return [alt_max(i) for i in range(1, n_max + 1)]


altitudes = alt_max_liste(10000)
altitude_max = max(altitudes)
print(altitudes.index(altitude_max) + 1, altitude_max)
