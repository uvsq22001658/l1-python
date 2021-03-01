#chiffre et déchiffre avec une clef k 
#(entier pris entre 0 et 25)

def chiffreCesar(clef, clair):
	#ici on suppose que clair ne contient que des A - Z
	"""clef est un entier compris entre 0 et 25, clair est une chaine ce caractère. fonction qui va chiffrer une chaine de caractere choisi"""
	chiffre = ""
	for c in clair:
		tmp = ord(c) + clef
		if (tmp > 90):
			tmp = ord(c) - 26 + clef
		chiffre = chiffre + chr(tmp)
	return chiffre

def dechiffreCesar(clef, chiffre):
	clair = ""
	for c in chiffre:
		tmp = ord(c) - clef
		if (tmp < 65):
			tmp = ord(c) + 26 - clef
		clair += chr(tmp)
	return clair

def decrypterCesar(chiffre):
	L = [0 for i in range(26)]
	for c in chiffre:
		L[ord(c)-65] = L[ord(c)-65] + 1
	ind_max = 0
	for i in range(len(L)):
		if L[ind_max] < L[i]:
			ind_max = i
	clef = (ind_max - 4)%26
	return dechiffreCesar(clef,chiffre)

texte_clair = open("clair.txt", "r")
contenu = texte_clair.readlines()
contenu2 = []
for s in contenu:
	contenu2.append(chiffreCesar(16,s))
#ord() donnait le code ASCII +"3"
f = open("chiffre.txt",'w')
for s in contenu2:
	f.write(s)
f.close()

ch2 = "SUSYUIJKDJUNJUXOFUHSEDVYTUDJYUBBUCEJTUFQIIUUIJNAFBEJYVDAIGEU"
print(decrypterCesar(ch2))