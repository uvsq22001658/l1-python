import tkinter as tk


def num_1():
    texte['text'] = "Bouton1"
    return


def num_2():
    texte['text'] = "Bouton2"
    return


def affiche():
    texte['text'] = saisie.get()
    return


racine = tk.Tk()
texte = tk.Label(racine, text="texte")
texte.grid(row=0, column=1, columnspan=3)

Bouton_1 = tk.Button(racine, text="Bouton1", command=num_1)
Bouton_1.grid(row=2, column=1)
Bouton_2 = tk.Button(racine, text="Bouton2", command=num_2)
Bouton_2.grid(row=2, column=2)
Bouton_3 = tk.Button(racine, text="Bouton3", command=affiche)
Bouton_3.grid(row=2, column=3)
saisie = tk.Entry()
saisie.grid(row=1, column=1, columnspan=3)

racine.mainloop()
