####################
# Projet de crytanalyse, IN202
# Julie VALBERT, 22001658, LDDBI
####################

####################
# Variables

t1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
t2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
t3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"

####################
# Fonctions

def frequence(message_chiffre): """Retourne la fréquence de chaque lettre dans un texte"""
    resultat = []
    for c in message_chiffre:
        if 97 <= ord(c) <= 122:
            exist = True
            for i in range(len(resultat)):
                if resultat[i][0] == c:
                    exist = False
            if exist:
                resultat.append([c, round(message_chiffre.count(c)/len(message_chiffre)*100, 2)])
    return resultat


def rang(lettre): """Retourne le rang de la lettre dans l'alphabet (entre 1 et 26) en fonction de son code ASCII"""
    if 97 <= ord(lettre) <= 122:
        return ord(lettre) - 97
    else:
        return 0


def decalage(lettre_message, lettre_cle): """Retourne une nouvelle lettre après un décalage de rang d'une lettre créé avec une lettre clé"""
    if 97 <= ord(lettre_message) <= 122:
        return chr((rang(lettre_message) + rang(lettre_cle)) % 26 + 97)
    else:
        return lettre_message


def dechiffrer(message_chiffre,cle): """Retourne le texte décrypté à partir du texte crypté et de la clé"""
    taille_cle = len(cle)
    res = ""
    for i in range(len(message_chiffre)):
        res += decalage(message_chiffre[i], chr(26 - rang(cle[i % taille_cle]) + 97))
    return res


def substitution(message_chiffre): """Substitue les lettres pour déchiffrer le texte 2"""
    nouveau_message = ""
    for c in message_chiffre:
        if c == "x": # "x" est le caractère le plus fréquent, on suppose qu'il s'agit du "e"
            nouveau_message += "e"
        elif c == "g": # "g" apparaît en début de petits mots suivis d'un "e", on suppose que c'est "l"
            nouveau_message += "l"
        elif c == "i": # "i" apparaît parfois en double, après "le" et en fin de mot, on suppose que c'est "s"
            nouveau_message += "s"
        elif c == "u": # on suppose que "leuuoes" est le mot "lettres", donc "u" est "t"
            nouveau_message += "t"
        elif c == "o": # on suppose que "leuuoes" est le mot "lettres", donc "o" est "r"
            nouveau_message += "r"
        elif c == "y": # on suppose que "seyles" est le mot "seules", donc "y" est "u"
            nouveau_message += "u"
        elif c == "c": # "c" apparaît souvent dans "ce" ou "cu" donc on suppose que "c" est "d"
            nouveau_message += "d"
        elif c == "n": # on suppose que "les lettres de n n a" est "les lettres de a à ?", donc "n" est "a"
            nouveau_message += "a"
        elif c == "s": # on suppose que "ssdt" est le mot "sont", donc "s" est "o"
            nouveau_message += "o"
        elif c == "d": # on suppose que "ssdt" est le mot "sont", donc "d" est "n"
            nouveau_message += "n"
        elif c == "k": # on suppose que "taklle knvonnue" est "taille inconnue", donc "k" est "i"
            nouveau_message += "i"
        elif c == "v": # on suppose que "taklle knvonnue" est "taille inconnue", donc "v" est "c"
            nouveau_message += "c"
        elif c == "q": # on suppose que "qroclain wiclier" est "prochain fichier", donc "q" est "p"
            nouveau_message += "p"
        elif c == "w": # on suppose que "qroclain wiclier" est "prochain fichier", donc "w" est "f"
            nouveau_message += "f"
        elif c == "l": # on suppose que "qroclain wiclier" est "prochain fichier", donc "l" est "h"
            nouveau_message += "h"
        elif c == "f": # on suppose que "fot de passe" est "mot de passe", donc "f" est "m"
            nouveau_message += "m"
        elif c == "m": # on suppose que "messame oriminal" est "message original", donc "m" est "g"
            nouveau_message += "g"
        else:
            nouveau_message += c 
    return nouveau_message


####################
# Programme principal

# Déchiffrage du texte 1

f1 = frequence(t1)
print(f1)
# Le "d" a la fréquence la plus élevée, donc on suppose qu'il correspond au "e"
# Le "k" est souvent au début de mots de deux lettres, donc on suppose qu'il s'agit du "l"
# On suppose donc qu'il y a un décalage de -1, on essaye alors de déchiffrer le texte 1 avec "z" pour clé
texte_1 = dechiffrer(t1, "z")
print(texte_1)


# Déchiffrage du texte 2

# Grâce au déchiffrage du texte 1, on sait que le texte a un codepar substitution alphabétique
# Chaque lettre est remplacée par une autre
# On utilise la fonction frequence
f2 = frequence(t2)
print(f2)
# Puis on crée et on utilise la fonction substitution, dans laquelle le raisonnement est expliqué
texte_2 = substitution(t2)
print(texte_2)


# Déchiffrage du texte 3

# Grâce au déchiffrage du texte 2, on sait que la clé est de taille inconnue
# On sait aussi que certaines lettres ne sont pas codées, celles qui se trouvent à la fin de l'alphabet
# On remarque que certains mots ne sont composés que d'une seule lettre : "e" et "c"
# Les mots de 1 lettre courants en Français sont "y" et "a" (et "à")
# On suppose que "y" n'est pas codée car elle se trouve à la fin de l'alphabet
# Donc les mots de 1 lettre seraient "a"
# On compte le nombre de caractères entre "c" et "c" : il y en a 20
# Les caractères "c" et "c" sont identiques, donc il y a un nombre entier de clés entre les deux
# On en déduit que la taille de la clé est un diviseur de 20
# La clé est donc de taille 1, 2, 4, 5, 10 ou 20
# On compte le nombre de caractères entre "e" et "c" : il y en a 38
# Les caractères "e" et "c" sont différents, donc il y a un nombre flottant de clés entre les 2
# On en déduit que la taille de la clé n'est pas un diviseur de 38
# Donc la clé est de taille 4, 5, 10 ou 20
# On essaye avec une clé de taille 4
# On a supposé que "c" en positions 45 et 65 seraient "a", donc il y aurait eu un décalage de 3
# La 1ère lettre de la clé serait donc "c"
# On a aussi supposé que "e" et position 7 serait "a", donc il y aurait eu un décalage de 5
# La 3ème lettre (7 = 4 + 3) de la clé serait donc "e"
# On essaye le clé "clef" et on est capable de déchiffrer le texte mais des caractères ne sont pas bien déchiffrés
# Un caractère sur quatre est incohérent
# On devine que "brapo" est "bravo" donc le "p" en position 4 est un v
# Dans le texte chiffré, le "p" est un "u"
# Il doit devenir un "v", donc la 4ème lettre de la clé doit créer un décalage de -1 lors du chiffrage
# La quatrième lettre de la clé est donc "z"
# On en conclut que la clé est "clez" et on utilise la fonction dechiffrer


texte_3 = dechiffrer(t3, "clez")
print(texte_3)
