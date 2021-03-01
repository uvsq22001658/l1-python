carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

# carre_pas_mag = carre_mag.copy() # Ne fonctionne pas, voir pourquoi avec http://pythontutor.com/
carre_pas_mag = [list(i) for i in carre_mag]
carre_pas_mag[3][2] = 7


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)
    print()


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si
    toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre[0])
    for ligne in carre:
        if sum(ligne) != somme:
            return -1
    return somme


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si
    toutes les colonnes ont la même somme, et -1 sinon """
    # On crée la liste des nombre contenus dans la première colonne.
    # Puis on fait pareil pour les autres colonnes et on compare.
    colonne_1 = [ligne[0] for ligne in carre]
    somme = sum(colonne_1)
    for num_colonne in range(1, len(carre)):
        colonne = [ligne[num_colonne] for ligne in carre]
        if sum(colonne) != somme:
            return -1
    return somme


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si
    les 2 diagonales ont la même somme, et -1 sinon """
    # Il n'y a que deux diagonales. On crée la liste des nombres
    # contenus dans chacune et on teste l'égalité.
    taille = len(carre)
    diagonale_1 = [carre[i][i] for i in range(taille)]
    diagonale_2 = [carre[i][taille - i - 1] for i in range(taille)]
    somme_1 = sum(diagonale_1)
    if sum(diagonale_2) != somme_1:
        return -1
    return somme_1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) \
        and testLignesEgales(carre) == testDiagonalesEgales(carre) \
        and testLignesEgales(carre) != -1


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si carre contient toutes les valeurs de 1 à n^2 où n est la
    taille du carré, et False sinon """
    # Méthode appliquée : Créer une liste contenant tous les nombres de 1 à
    # n2 +1 et parcourir tout le carré en les retirant de la liste au fur et à mesure
    n = len(carre)
    nombres = list(range(1, n * n + 1))
    for i in range(n):
        for j in range(n):
            if carre[i][j] in nombres:
                nombres.remove(carre[i][j])
    return len(nombres) == 0


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
