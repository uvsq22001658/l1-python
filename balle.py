import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
nb_rebond = 0
identifiant = 0

###################
# Fonctions


def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global balle
    global nb_rebond
    global identifiant
    while nb_rebond <= 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        identifiant = canvas.after(20, mouvement)
        canvas.move(mur_1, 1, 0)
        canvas.move(mur_2, 1, 0)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    global nb_rebond
    nb_rebond += 1
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= xa or x1 >= xc:
        balle[1] = -balle[1]
    if y0 <= ya or y1 >= yc:
        balle[2] = -balle[2]


######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()

mur_1 = canvas.create_line(1, 0, 1, 400, fill="white")
mur_2 = canvas.create_line(150, 0, 150, 400, fill="white")
xa, ya, xb, yb = canvas.coords(mur_1)
xc, yc, xd, yd = canvas.coords(mur_2)

balle = creer_balle()
mouvement()
racine.mainloop()
