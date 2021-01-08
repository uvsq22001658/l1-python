import tkinter as tk
import random as rd
racine = tk.Tk()
racine.title("Mon dessin")
mon_canvas = tk.Canvas(racine, width=500, height=500, background="black")
mon_canvas.grid(row=2, column=1, rowspan=3, columnspan=2)

couleur_courante = "blue"
objets = []

centre_x = rd.randint(50, 450)
centre_y = rd.randint(50, 450)


def cercle_bleu():
    centre_x = rd.randint(50, 450)
    centre_y = rd.randint(50, 450)
    oval = mon_canvas.create_oval(centre_x - 50, centre_y - 50,
                           centre_x + 50, centre_y + 50, fill=couleur_courante)
    objets.append(oval)
    return


def carre_rouge():
    centre_x = rd.randint(50, 450)
    centre_y = rd.randint(50, 450)
    carre = mon_canvas.create_rectangle(centre_x - 50, centre_y - 50,
                                centre_x + 50, centre_y + 50, fill=couleur_courante)
    objets.append(carre)
    return


def croix_jaune():
    centre_x = rd.randint(50, 450)
    centre_y = rd.randint(50, 450)
    ligne_1 = mon_canvas.create_line(centre_x, centre_y - 50,
                           centre_x, centre_y + 50, fill=couleur_courante)
    ligne_2 = mon_canvas.create_line(centre_x - 50, centre_y,
                           centre_x + 50, centre_y, fill=couleur_courante)
    objets.extend([ligne_1, ligne_2])
    return


def choisir_couleur():
    global couleur_courante
    couleur_courante = input("Choisir une couleur\n")
    return


def undo():
    if len(objets) > 0 :
        dernier_objet = objets[len(objets) - 1]
        if mon_canvas.type(dernier_objet) == "line":
            mon_canvas.delete(dernier_objet)
            del objets[len(objets) - 1]
            dernier_objet = objets[len(objets) - 1]
        mon_canvas.delete(dernier_objet)
        del objets[len(objets) - 1]
    return


bouton_choisir_une_couleur = tk.Button(racine, text="Choisir une couleur",
                                       command=choisir_couleur)
bouton_cercle = tk.Button(racine, text="Cercle", command=cercle_bleu)
bouton_carre = tk.Button(racine, text="Carré", command=carre_rouge)
bouton_croix = tk.Button(racine, text="Croix", command=croix_jaune)
bouton_undo = tk.Button(racine, text="Undo", command=undo)

bouton_choisir_une_couleur.grid(row=1, column=1)
bouton_cercle.grid(row=2, column=0)
bouton_carre.grid(row=3, column=0)
bouton_croix.grid(row=4, column=0)
bouton_undo.grid(row=1, column=2)

racine.mainloop()
