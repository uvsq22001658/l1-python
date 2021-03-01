import tkinter as tk


def fermer_fenetre():
    racine.destroy()
    return


racine = tk.Tk()
racine.title("Rappel du premier Semestre")
texte = tk.Label(racine, text="J'adore Python !")
texte.pack()
bouton = tk.Button(racine, text="QUITTER", bg="blue", fg="yellow", command=fermer_fenetre)
bouton.pack()

racine.mainloop()
