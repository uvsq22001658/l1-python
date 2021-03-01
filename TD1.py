import tkinter as tk

nb_clic = 0


def fermer_fenetre():
    racine.destroy()
    return


# def cpt(event):
#     global nb_clic
#     affiche['text']=str(nb_clic)
#     nb_clic += 1
#     return


def couleur(event):
    affiche['text']=event.widget['bg']
    # print(event.widget['bg'])
    return



racine = tk.Tk()
racine.title("Rappel du premier Semestre")
affiche = tk.Label(racine, text="J'adore Python !")
affiche.grid()
bouton = tk.Button(racine, text="QUITTER", bg="blue", fg="yellow", command=fermer_fenetre)
bouton.grid()
canvas = tk.Canvas(racine, width=300, height=300, bg="red")
canvas.grid(row=0, column=1)
canvas_2 = tk.Canvas(racine, width=300, height=300, bg="black")
canvas_2.grid(row=1, column=1)
# canvas.bind('<Button-1>', cpt)
canvas.bind('<Double-1>', couleur)
canvas_2.bind('<Double-1>', couleur)

racine.mainloop()
