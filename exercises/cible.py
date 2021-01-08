import tkinter as tk
racine = tk.Tk()
taille_canvas = 500
mon_canvas = tk.Canvas(racine, width=taille_canvas,
                       height=taille_canvas, bg="black")
mon_canvas.grid()

nb_cercles = 30
epaisseur = (taille_canvas // 2) // nb_cercles

couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]

for i in range(nb_cercles):
    mon_canvas.create_oval(i * epaisseur, i * epaisseur,
                           taille_canvas - i * epaisseur,
                           taille_canvas - i * epaisseur,
                           fill=couleurs[i % len(couleurs)], width=0)

racine.mainloop()
