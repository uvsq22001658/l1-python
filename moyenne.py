fic_in = open("notes", "r")
fic_out = open("moyenne", "w")

ligne = fic_in.readline()
fic_out.write(ligne[:-1])
fic_out.write(" moyenne\n")

for ligne in fic_in:
    mots = ligne.split()
    moy = (int(mots[1]) + int(mots[2]) + int(mots[3])) / 3
    fic_out.write(ligne[:-1])
    fic_out.write(" " + str(moy))
    fic_out.write("\n")

fic_out.close()
fic_in.close()