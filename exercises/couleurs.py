import tkinter as tk
import random as rd 

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, background="black", width=256, height=256)


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes
  r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


# def get_color(r, g, b):
#    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(x, y, color):
    mon_canvas.create_line(x, y, x + 1, y, fill=color)
    return


# draw_pixel(128, 128, "white")

def ecran_aleatoire():
    for i in range(256):
       for j in range(256):
            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)
            draw_pixel(i, j, get_color(r, g, b))
    return


def degrade_gris():
    for i in range(256):
        mon_canvas.create_line(i, 0, i, 255, fill=get_color(i, i, i))
    return


def degrade_2D():
    for i in range(256):
       for j in range(256):
            r = i
            g = 0
            b = j
            draw_pixel(i, j, get_color(r, g, b))
    return


bouton_aléatoire = tk.Button(racine, text="Aléatoire", foreground="blue", command=ecran_aleatoire)
bouton_dégradé_gris = tk.Button(racine, text="Dégradé gris", foreground="blue", command=degrade_gris)
bouton_dégradé_2D = tk.Button(racine, text="Dégradé 2D", foreground="blue", command=degrade_2D)

bouton_aléatoire.grid(row=1, column=0)
bouton_dégradé_gris.grid(row=2, column=0)
bouton_dégradé_2D.grid(row=3, column=0)
mon_canvas.grid(row=1, column=1, rowspan=3)

racine.mainloop()
