import tkinter as tk
import random as rd

racine = tk.Tk()

canvas = tk.Canvas(racine, height=400, width=600, bg="black")
canvas.grid(row=0, column=0)


def creer_balle():
    """Crée la balle et retourne une liste contenant l'identifiant de la balle
    et deux entiers choisis au hasard entre 1 et 7"""
    cercle = canvas.create_oval(280, 180, 320, 220, fill="blue")
    a = rd.randint(1, 7)
    b = rd.randint(1, 7)
    return [cercle, a, b]


def mouvement(balle):
    global identifiant
    canvas.move(balle[0], balle[1], balle[2])
    identifiant = canvas.after(20, mouvement, balle)


def demarrer():
    global balle
    global bouton_demarrer
    global actif
    global identifiant
    if actif:
        actif = False
        bouton_demarrer.config(text="Démarrer")
        canvas.after_cancel(identifiant)
    else:
        actif = True
        bouton_demarrer.config(text="Arrêter")
        mouvement(balle)


def rebond1(balle):
    coordonnees = canvas.coords(balle[0])[0]
    if coordonnees[0] <= 0:
        
    

balle = creer_balle()
actif = False
identifiant = 0

bouton_demarrer = tk.Button(racine, text="Démarrer", command=demarrer)
bouton_demarrer.grid(row=1, column=0)

racine.mainloop()
